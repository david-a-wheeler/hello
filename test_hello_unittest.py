#!/usr/bin/python3

import unittest, io, contextlib, os
import hello

class TestHello(unittest.TestCase):
    """Test our program"""

    def test_output(self):
        """Ensure program produces correct output"""
        f = io.StringIO() # Create pseudo-file where output will be sent
        with contextlib.redirect_stdout(f): # Redirect output
            hello.print_hello()
        self.assertEqual(f.getvalue(), 'Hello, world!' + os.linesep)

if __name__ == '__main__':
    unittest.main()
