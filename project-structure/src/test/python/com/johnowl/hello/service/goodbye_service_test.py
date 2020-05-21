from src.main.python.com.johnowl.hello.service.goodbye_service import GoodbyeService
import unittest


class HelloServiceTest(unittest.TestCase):

    def test_when_call_say_message_should_return_hello_world(self):
        service = GoodbyeService()
        message = service.say_goodbye()
        self.assertEqual(message, 'Bye! Bye!')

