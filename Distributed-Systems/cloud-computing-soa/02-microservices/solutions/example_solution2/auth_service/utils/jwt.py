from auth_service.schemas.token import TokenPayload
from auth_service.settings import settings
from auth_service.const import JWT_HEADER

import base64
from datetime import datetime, timedelta
import json
import hmac
import hashlib
from typing import Optional


class JWT:
    @staticmethod
    def _get_secret_key() -> str:
        print('JWT Encode secret key', settings.SECRET_KEY)
        return settings.SECRET_KEY

    @staticmethod
    def get_header() -> dict:
        return JWT_HEADER

    @staticmethod
    def get_payload(user) -> TokenPayload:
        """
        Function to build payload from user id, expiry time
        :param user: user id (int)
        :return: TokenPayload object
        """
        try:
            expire = datetime.utcnow() + timedelta(
                minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
            )
            print(f'''
                    JWT Payload extraction:
                    user:{user}, {type(user)}
                    expire:{expire}, {type(expire)}
                ''')
            return TokenPayload(user=user, exp=int(expire.timestamp()))
        except Exception as e:
            print(f"Exception while getting JWT payload, {e}")
            return None

    @staticmethod
    def get_signature(encoded_header, encoded_payload, encoded_secret_key):
        """
        Function to get signature from JWT
        :param encoded_header: base64 encoded bytes of header
        :param encoded_payload: base64 encoded bytes of payload
        :param encoded_secret_key: base64 encoded secret key
        :return:
        """
        try:
            x = encoded_header.decode('utf-8')
            y = encoded_payload.decode('utf-8')
            message = f"{x}.{y}".encode('utf-8')

            # call HMAC signature generation with sha256 algo
            signature = hmac.new(msg=message, key=encoded_secret_key, digestmod=hashlib.sha256)
            signature = signature.hexdigest()
            
            return signature
        except Exception as e:
            print(f"Exception while getting JWT signature, {e}")
            return None

    @staticmethod
    def base64_encode(serializable_object):
        """
        Function to base64 encode serializable object
        :param serializable_object:
        :return: base64 encoded bytes
        """
        encoded = base64.urlsafe_b64encode(serializable_object.encode("utf-8"))
        # remove any extra = inserted
        return encoded.rstrip(b"=")

    @staticmethod
    def base64_decode(base64_encoded: str):
        """
        Function to base64 decode input string
        :param base64_encoded: str
        :return: decoded bytes
        """
        # pad the encoded value before decoding, to ensure len is multiple of 4
        while len(base64_encoded) % 4:
            base64_encoded = base64_encoded + "="
        return base64.urlsafe_b64decode(base64_encoded.encode("utf-8"))

    @staticmethod
    def encode(user) -> Optional[str]:
        """
        Function to encode and find JWT
        :param user: User ID (int)
        :return: encoded string
        """
        try:
            header_json = json.dumps(JWT_HEADER)
            payload_json = json.dumps(JWT.get_payload(user).dict())
            secret_key = JWT._get_secret_key()

            encoded_header = JWT.base64_encode(header_json)
            encoded_payload = JWT.base64_encode(payload_json)
            encoded_secret_key = JWT.base64_encode(secret_key)
            
            signature = JWT.get_signature(encoded_header, encoded_payload, encoded_secret_key)
            
            return f"{encoded_header.decode('utf-8')}.{encoded_payload.decode('utf-8')}.{signature}"
        except Exception as e:
            print(f"Exception occurred while encoding JWT:, {e}")
            return None

    @staticmethod
    def verify_token(token, secret_key) -> Optional[TokenPayload]:
        """
        Function to verify JWT token
        :param token: JWT token string
        :param secret_key: JWT secret key string
        :return: TokenPayload object if token is valid, None otherwise
        """
        try:
            # remove the bearer part from token
            if not token.token.startswith("Bearer "):
                print('Bearer token not found')
                return None
            token = token.token.split(' ')[1]

            # find if the expected signature is same as the one we get from token and secret key provided
            # get current header, payload, signature
            encoded_header, encoded_payload, signature = str(token).split(".")

            # get the expected signature
            encoded_secret_key = JWT.base64_encode(secret_key)
            arg1 = encoded_header.encode('utf-8')
            arg2 = encoded_payload.encode('utf-8')
            expected_signature = JWT.get_signature(arg1, arg2, encoded_secret_key)

            if signature != expected_signature:
                print("JWT signature verification failed")
                return None

            payload_json = JWT.base64_decode(encoded_payload)
            payload_json = json.loads(payload_json)
            token_payload = TokenPayload(**payload_json)

            # find the time difference, based on current time, expiry
            dt_object = datetime.utcfromtimestamp(token_payload.exp)
            current_time = datetime.utcnow()
            difference_in_minutes = int((dt_object - current_time).total_seconds() / 60)
            if difference_in_minutes > settings.ACCESS_TOKEN_EXPIRE_MINUTES:
                print(f'JWT expired')
                return None
            return token_payload
        except Exception as e:
            print(f'Exception while verifying JWT token, {e}')
            return None