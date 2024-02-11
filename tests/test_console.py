#!/usr/bin/python3
"""the consol test cases"""
import unittest
from console import HBNBCommand


class HBNBCommand_prompting(unittest.TestCase):
    """the prompt test class"""
    def test_prompt_type(self):
        """the prompt type test"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)