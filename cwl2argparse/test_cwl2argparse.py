import os
import subprocess
import unittest
from unittest import mock

import sys

from main import main


class GeneralTestCase(unittest.TestCase):

    def test_general(self):
        args = ["main.py", "example", "-d", "example", '-p', 'arg_']
        with self.assertRaises(SystemExit) as result:
            with unittest.mock.patch.object(sys, 'argv', args):
                main()
        self.assertEqual(result.exception.code, 0)
        path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'example'))
        for file in os.listdir(path):
            if file.endswith('.py'):
                exit_status = subprocess.call('python3 {0}'.format(os.path.join(path, file)), shell=True)
                self.assertEqual(exit_status, 2)
