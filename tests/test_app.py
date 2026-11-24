import io
import runpy
import unittest
from contextlib import redirect_stdout

from app import greet


class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("World"), "Hello, World from Batoul Hachem!")
        self.assertEqual(greet("Jenkins"), "Hello, Jenkins from Batoul Hachem!")

    def test_cli(self):
        output = io.StringIO()
        with redirect_stdout(output):
            runpy.run_module("app", run_name="__main__")
        self.assertEqual(output.getvalue(), "Hello, World from Batoul Hachem!\n")
