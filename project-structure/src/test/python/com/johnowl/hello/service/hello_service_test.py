from src.main.python.com.johnowl.hello.service.hello_service import HelloService
import unittest


class HelloServiceTest(unittest.TestCase):

    def test_when_call_say_hello_should_return_hello_world(self):
        service = HelloService()
        message = service.say_hello()
        self.assertEqual(message, 'Hello world')

