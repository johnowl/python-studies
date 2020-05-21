import hashlib
import re


class ValidatorService:

    def __init__(self):
        self.__uuidv4_regex = re.compile('^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$', re.I)
        self.__digest_regex = re.compile('^sha256=[a-f0-9]{64}$', re.I)

    def is_valid(self, headers: dict, body: str = ""):

        application_id = headers.get("Application-Id", "")
        digest = headers.get("Digest", "")

        if application_id == "":
            return ValidationError("application_id_not_found", "Application-Id não encontrado.")

        if digest == "":
            return ValidationError("digest_not_found", "Digest não encontrado.")

        if not self.__uuidv4_regex.match(application_id):
            return ValidationError("application_id_invalid", "Application-Id inválido.")

        if not self.__digest_regex.match(digest):
            return ValidationError("digest_invalid", "Digest inválido.")

        body_byte_array = bytearray(body, "utf-8")
        if hashlib.sha256(body_byte_array).hexdigest() != digest[7:]:
            return ValidationError("digest_invalid", "Digest inválido.")

        return True


class ValidationError:
    def __init__(self, kind: str, message: str):
        self.kind = kind
        self.message = message
