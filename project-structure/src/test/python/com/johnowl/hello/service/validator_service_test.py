from src.main.python.com.johnowl.hello.service.validator_service import ValidatorService
import unittest


class HelloServiceTest(unittest.TestCase):

    def test_when_call_say_hello_should_return_hello_world(self):
        service = ValidatorService()
        headers = {
            "Application-Id": "273ab84d-0c7d-434a-a9f7-3004eabf54a4",  # random uuid v4
            "Digest": "sha256=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"  # empty string hash
        }
        result = service.is_valid(headers)
        self.assertEqual(result, True)
