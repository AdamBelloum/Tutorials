from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import httpx

app = FastAPI()

ALLOWED_HEADERS = ['content-type', 'host', 'accept', 'accept-encoding', 'connection', 'authorization']

SERVICES = {
    "url_shortener_service": "http://url-shortener-service:8000",
    "auth_service": "http://auth-service:8001",
}

async def forward_request(service_url: str, method: str, path: str, body=None, headers=None):
    async with httpx.AsyncClient() as client:
        url = f"{service_url}{path}"

        request_params = {
            "method": method,
            "url": url,
            "headers": headers,
        }
        if body and method in ["POST", "PUT", "PATCH"]:
            request_params["json"] = body
        response = await client.request(**request_params)
        return response

@app.api_route("/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"])
async def gateway(service: str, path: str, request: Request):
    if service not in SERVICES:
        raise HTTPException(status_code=404, detail="Service not found")

    # get service url
    service_url = SERVICES[service]
    print(f"Call to the service: {service_url}")

    # request body
    try:
        body = await request.json() if request.method in ["POST", "PUT", "PATCH"] else None
    except Exception as e:
        print(f"Error extracting request body: {e}")
        body = None

    # request header
    headers = {k: v for k, v in dict(request.headers).items() if k.lower() in ALLOWED_HEADERS}

    # forward request
    response = await forward_request(service_url, request.method, f"/{path}", body, headers)

    # parse response body
    try:
        content = response.json() if response.content else {}
    except ValueError:
        content = None
    return JSONResponse(status_code=response.status_code, content=content)