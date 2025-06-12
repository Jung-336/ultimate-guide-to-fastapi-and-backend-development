from datetime import datetime, timedelta
import jwt
from config import security_setting


def generate_access_token(
        data: dict,
        expiry: timedelta = timedelta(days=1)
) -> str:
    return jwt.encode(
            payload = {
                **data,
                "exp": datetime.now() + expiry
            },
            algorithm=security_setting.JWT_ALGORITHM,
            key=security_setting.JWT_SECRET
    )


def decode_access_token(token: str) -> dict | None:
    try:
        return jwt.decode(
            jwt=token,
            key=security_setting.JWT_SECRET,
            algorithms=[security_setting.JWT_ALGORITHM],
        )
    except jwt.PyJWTError as e:
        print("error trace: ", e)
        return None

