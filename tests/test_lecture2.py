import math
import unittest
from io import StringIO
from unittest.mock import patch


class TestGreeting(unittest.TestCase):
    @patch('builtins.input', return_value='Viivi Virta')
    @patch('sys.stdout', new_callable=StringIO)
    def test_greet_user(self, mock_stdout, mock_input):
        # Import the code to be tested
        import task1
        # Check the output
        self.assertEqual(mock_stdout.getvalue(), "Hello, Viivi Virta!\n")

if __name__ == '__main__':
    unittest.main()

