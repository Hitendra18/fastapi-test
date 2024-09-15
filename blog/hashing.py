# from passlib.context import CryptContext

import bcrypt


# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hash:
    @staticmethod
    def encrypt(password: str):
        # return pwd_context.hash(password)
        # return bcrypt.hashpw(password.encode(encoding="utf-8"), bcrypt.gensalt()).hex()
        password_bytes = password.encode("utf-8")  # Convert string to bytes
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed.decode("utf-8")  # Return as a string

    @staticmethod
    def verify(secret: str, hashed_password):
        # return pwd_context.verify(secret, hashed_password)
        # return bcrypt.checkpw(secret.encode(encoding="utf-8"), hashed_password)
        plain_password_bytes = secret.encode("utf-8")  # Convert to bytes
        hashed_password_bytes = hashed_password.encode("utf-8")  # Convert to bytes
        return bcrypt.checkpw(plain_password_bytes, hashed_password_bytes)
