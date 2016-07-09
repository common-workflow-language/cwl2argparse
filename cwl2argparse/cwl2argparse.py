import re

import argparse
import os
import string

import yaml
from yaml import scanner
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

from cwl_classes import Tool


class Argument:
    def __init__(self, arg):
        self.dest = Argument._get_dest(arg)
        self.help = arg.description
        self.option_string = Argument._get_option_string(arg)
        self.default = Argument._get_default(arg)
        self.action = Argument._get_actions(arg)
        self.type = Argument._get_type(arg)
        self.nargs = Argument._get_nargs(arg)
    
    @staticmethod
    def _get_dest(arg):
        s = arg.id.strip(string.punctuation)
        if arg.prefix:
            s = arg.prefix + s
        return re.sub(r'[{0}]'.format(string.punctuation), '_', s)

    @staticmethod
    def _get_option_string(arg):
        if arg.optional:
            if hasattr(arg, 'input_binding'):
                # TODO: handle conflicting prefixes
                if arg.input_binding.prefix:
                    name = arg.input_binding.prefix.strip(string.punctuation)
                    if len(name) == 1:
                        return '-' + name
                    else:
                        return '--' + name
                else:
                    return '--' + arg.id
        else:
            return Argument._get_dest(arg)
    
    @staticmethod
    def _get_type(arg):
        CWL_TO_PY_TYPES = {
            'string': 'str',
            'int': 'int',
            'boolean': 'bool',
            'double': 'float',
            'float': 'float',
            'array': 'list',
            'File': 'argparse.FileType()',
        }
        arg_type = CWL_TO_PY_TYPES[arg.get_type()]
        if arg_type is list and type(arg_type) is list:
            return None
        else:
            return arg_type

    @staticmethod
    def _get_choices(arg):
        if arg.get_type == 'enum':
            # TODO
            return arg.symbols

    @staticmethod
    def _get_default(arg):
        if arg.default:
            if type(arg.default) is str:
                return "\"" + arg.default + "\""    # for proper rendering in j2 template
            else:
                return arg.default


    @staticmethod
    def _get_actions(arg):
        if arg.optional and arg.type == 'boolean':
            return 'store_true'
    
    @staticmethod
    def _get_nargs(arg):
        if arg.type == 'array':
           if arg.optional:
               return '*'
           else:
                return '+'

    

def cwl2argparse(file, dest, prefix=None):
    if not file.endswith('.cwl'):
        print('{0} is not a CWL tool definition'.format(file))
        return None
    try:
        tool = Tool(file)
    except yaml.scanner.ScannerError:
        print('File {0} is corrupted or not a CWL tool definition')
        return None
    args = []
    tool.inputs.update(tool.outputs)
    for arg in tool.inputs.values():
        arg.prefix = prefix
        args.append(Argument(arg))
    path = os.path.abspath(os.path.dirname(__file__))
    env = Environment(loader=FileSystemLoader(path),
                      trim_blocks=True,
                      lstrip_blocks=True)
    template = env.get_template('argparse.j2')
    result = template.render(tool=tool, args=args)
    filename = file.split('/')[-1].replace('.cwl', '.py')
    with open(os.path.join(dest, filename), 'w') as f:
        f.write(result)
    print(filename)
    print(result)
