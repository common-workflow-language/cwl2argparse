import importlib.util
import os
import sys
import unittest
from unittest import mock

from cwl2argparse.main import main


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
                spec = importlib.util.spec_from_file_location(file.replace('.py', ''), os.path.join(path, file))
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                function_name = list(filter(lambda x: not x.startswith('__') and x != 'argparse', dir(module)))
                function = getattr(module, function_name[0])
                with self.assertRaises(SystemExit) as cm:
                    function().parse_args()
                self.assertEqual(cm.exception.code, 2)
