import base64
import json
import hmac
import hashlib
import config

header = {
    "alg": "HS256",
    "typ": "JWT"
}

secret = config.get_settings().secret_key

#Create and return the JWT token
def generate(payload):
    
    #make the payload json
    payload = json.dumps(payload)
    
    #make json of header and encode it base 64
    encoded_header = base64.b64encode(json.dumps(header).encode())
    #encode base 64 the payload
    encoded_payload = base64.b64encode(payload.encode())
    
    #create a temp variable made by concatenation of header and payload
    temp = encoded_header.decode() + "." + encoded_payload.decode()
    #create the signature by crypting hmac256 our temp variable with our secret
    signature = hmac.new(secret.encode(), temp.encode(), hashlib.sha256).hexdigest()
    #create the token by concatenating plain base64 header, plain base64 payload and Hmac256 cypted header and payload
    result = encoded_header.decode() + "." + encoded_payload.decode() + "." + signature

    print("header: "+encoded_header.decode())
    print("payload: "+encoded_payload.decode())
    print("signature: "+signature)

    return (result)

#Check validity of token
def decode(token):
    
    #split by "."
    token_list = token.split(".")

    #if JWt is valid return payload otherwise raise exception
    if (check_validity(token_list[0].encode(), token_list[1].encode(), token_list[2].encode(), secret)):
        print("NO tampering detected")
        # header = base64.b64decode(token_list[0])
        payload = base64.b64decode(token_list[1])
        # signature = base64.b64decode(token_list[2])
        return (payload)
    else:
        raise InvalidToken("Tampering detected")

#return True if JWT check is valid, otherwise return False
def check_validity(encoded_header, encoded_payload, old_signature, secret):
    
    #re-create our temp made of payload and header with plain header and payload received
    temp = encoded_header.decode() + "." + encoded_payload.decode()
    
    #re-create the signature by encoding the new temp Hmac256 with our secret
    signature = hmac.new(secret.encode(), temp.encode(), hashlib.sha256).hexdigest()
    
    #if old signature and new signature match it means that no tampering has been made
    if (old_signature.decode() == signature):
        print("Signature matching")
        return True
    else:
        print("Signature NOT matching")
        print("original: "+str(old_signature))
        print("new: "+str(signature))
        return False

# create an exception class
class InvalidToken(Exception):
    pass
