import unittest
import sys
from io import StringIO
from nba_stats.main import greet, main


class TestHelloScript(unittest.TestCase):
    def test_greet_outputs_expected_text(self):
        """Test that greet() prints the expected output."""
        captured_output = StringIO()
        sys.stdout = captured_output
        greet()
        sys.stdout = sys.__stdout__
        
        output = captured_output.getvalue().strip()
        self.assertIn("Hello, world!", output)
        self.assertIn("Hello, world two!", output)
    
    def test_main_executes_without_error(self):
        """Test that main() executes without raising an exception."""
        captured_output = StringIO()
        sys.stdout = captured_output
        try:
            main()
        finally:
            sys.stdout = sys.__stdout__
        
        self.assertIsNotNone(captured_output.getvalue())


if __name__ == '__main__':
    unittest.main()
