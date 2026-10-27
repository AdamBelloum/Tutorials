"use strict";

const http = require("node:http");
const assert = require("node:assert/strict");
const { once } = require("node:events");

const originalListen = http.Server.prototype.listen;
let server;

// Test-only interception: force loopback and an ephemeral port.
http.Server.prototype.listen = function (...args) {
    server = this;
    const callback = args.find(value => typeof value === "function");
    return originalListen.call(this, 0, "127.0.0.1", callback);
};

async function main() {
    try {
        require("./index.js");
        assert.ok(server, "Wrapper must create an HTTP server");
        if (!server.listening) await once(server, "listening");

        const base = `http://127.0.0.1:${server.address().port}`;
        const cases = [
            {
                label: "valid weather JSON", method: "POST",
                type: "application/json",
                body: '{"city":"Amsterdam","temperature_c":12.5,"condition":"Cloudy"}',
                status: 200,
                json: {
                    city: "Amsterdam", temperature_c: 12.5, condition: "Cloudy",
                    message: "Weather in Amsterdam: 12.5°C, Cloudy."
                }
            },
            {
                label: "invalid city", method: "POST",
                type: "application/json",
                body: '{"city":"","temperature_c":12.5,"condition":"Cloudy"}',
                status: 400, json: { error: "invalid_city" }
            },
            {
                label: "string temperature", method: "POST",
                type: "application/json",
                body: '{"city":"Amsterdam","temperature_c":"12.5","condition":"Cloudy"}',
                status: 400, json: { error: "invalid_temperature" }
            },
            {
                label: "invalid condition", method: "POST",
                type: "application/json",
                body: '{"city":"Amsterdam","temperature_c":12.5,"condition":""}',
                status: 400, json: { error: "invalid_condition" }
            },
            {
                label: "JSON array", method: "POST",
                type: "application/json", body: '[]',
                status: 400, json: { error: "expected_json_object" }
            },
            {
                label: "plain text", method: "POST",
                type: "text/plain", body: "Amsterdam",
                status: 400, json: { error: "expected_json_object" }
            },
            {
                label: "GET", method: "GET",
                status: 405, json: { error: "method_not_allowed" },
                allow: "POST"
            },
            {
                label: "URL-encoded form", method: "POST",
                type: "application/x-www-form-urlencoded",
                body: "city=Amsterdam&temperature_c=12.5&condition=Cloudy",
                status: 400, json: { error: "invalid_temperature" }
            },
            {
                label: "malformed JSON", method: "POST",
                type: "application/json", body: '{"city":',
                status: 400, html: true
            }
        ];

        for (const item of cases) {
            const response = await fetch(base, {
                method: item.method,
                headers: item.type ? { "Content-Type": item.type } : {},
                body: item.body,
                signal: AbortSignal.timeout(5000)
            });
            const text = await response.text();
            const contentType = response.headers.get("content-type") || "";

            console.log(JSON.stringify({
                case: item.label,
                status: response.status,
                contentType,
                allow: response.headers.get("allow"),
                bodyPreview: text.slice(0, 200)
            }));

            assert.equal(response.status, item.status, item.label);
            if (item.json) {
                assert.match(contentType, /^application\/json\b/);
                assert.deepEqual(JSON.parse(text), item.json);
            }
            if (item.allow) {
                assert.equal(response.headers.get("allow"), item.allow);
            }
            if (item.html) {
                assert.match(contentType, /^text\/html\b/);

                if (process.env.NODE_ENV === "production") {
                    assert.match(text, /<pre>Bad Request<\/pre>/);
                    assert.doesNotMatch(
                        text,
                        /SyntaxError|JSON\.parse|node_modules|\/work\//,
                        "Production response must omit parser stack details"
                    );
                } else {
                    assert.match(
                        text,
                        /SyntaxError/,
                        "Development response exposes the parser error"
                    );
                }
            }
        }
        console.log("PASS: all 9 weather wrapper observations matched expectations.");
    } finally {
        http.Server.prototype.listen = originalListen;
        if (server && server.listening) {
            await new Promise((resolve, reject) => {
                server.close(error => error ? reject(error) : resolve());
                server.closeAllConnections();
            });
        }
    }
}

main().catch(error => {
    console.error(error);
    process.exitCode = 1;
});
