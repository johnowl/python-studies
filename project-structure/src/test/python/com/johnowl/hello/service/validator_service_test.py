from src.main.python.com.johnowl.hello.service.validator_service import ValidatorService
from src.main.python.com.johnowl.hello.service.validator_service import ValidationError
import unittest


class HelloServiceTest(unittest.TestCase):

    def test_when_validate_without_body_and_with_valid_data_should_return_true(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54a4",  # random uuid v4
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # empty string hash
        }
        result = service.is_valid(headers)
        self.assertEqual(result, True)

    def test_when_validate_without_body_and_with_invalid_application_id_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54",  # invalid uuid v4
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # empty string hash
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "application_id_invalid")
        self.assertEqual(result.message, "Application-Id inválido.")

    def test_when_validate_without_body_and_with_invalid_digest_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54a4",  # random uuid v4
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b856"  # invalid hash
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "digest_invalid")
        self.assertEqual(result.message, "Digest inválido.")

    def test_when_validate_without_body_and_with_invalid_format_digest_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54a4",  # random uuid v4
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb924?7ae41e4649b934ca495991b7852b856"  # invalid format hash
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "digest_invalid")
        self.assertEqual(result.message, "Digest inválido.")

    def test_when_validate_with_valid_data_should_return_true(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54a4",  # random uuid v4
            "Digest": "sha256=5e2bf57d3f40c4b6df69daf1936cb766f832374b4fc0259a7cbff06e2f70f269"  # valid hash
        }
        result = service.is_valid(headers, body="lorem ipsum")
        self.assertTrue(result)

    def test_when_validate_without_body_and_with_empty_application_id_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "",
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # empty string hash
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "application_id_not_found")
        self.assertEqual(result.message, "Application-Id não encontrado.")

    def test_when_validate_without_body_and_with_empty_digest_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54",  # invalid uuid v4
            "Digest": ""  # empty string hash
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "digest_not_found")
        self.assertEqual(result.message, "Digest não encontrado.")

    def test_when_validate_without_body_and_without_digest_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54"  # invalid uuid v4
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "digest_not_found")
        self.assertEqual(result.message, "Digest não encontrado.")

    def test_when_validate_without_body_and_without_application_id_should_return_error(self):
        service = ValidatorService()
        headers = {
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # empty string hash
        }
        result = service.is_valid(headers)
        self.assertIsInstance(result, ValidationError)
        self.assertEqual(result.kind, "application_id_not_found")
        self.assertEqual(result.message, "Application-Id não encontrado.")