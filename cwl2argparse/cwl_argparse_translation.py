import re

import os
import string

import sys
import yaml
from yaml import scanner
from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

from cwl2argparse.cwl_classes import Tool

argument_names = []


class Argument:
    def __init__(self, arg):
        self.dest = Argument._get_dest(arg)
        self.help = arg.description
        self.option_string = Argument._check_conflicting_prefixes(Argument._get_option_string(arg))
        self.default = Argument._get_default(arg)
        self.action = Argument._get_actions(arg)
        self.type = Argument._get_type(arg)
        self.nargs = Argument._get_nargs(arg)
        self.choices = Argument._get_choices(arg)
        if self.action:
            self.type = self.default = None
    
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
                if arg.input_binding.prefix:
                    name = arg.input_binding.prefix.strip(string.punctuation)
                    if len(name) == 1:
                        return '-' + name
                    else:
                        return '--' + name
                else:
                    return '--' + arg.id.strip(string.punctuation)
        else:
            return Argument._get_dest(arg)

    @staticmethod
    def _check_conflicting_prefixes(name):
        global argument_names
        if name in argument_names:
            # if the name already exists, add '_N' to it, where N is an order number of this name
            # example: if argument 'foo' already exists, an argument 'foo_1' is created
            # if 'foo_1' exists, 'foo_2' is created
            same_names = list(filter(lambda x: x.startswith(name), argument_names))
            return name + '_{0}'.format(len(same_names))
        else:
            argument_names.append(name)
            return name


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
            'stdout': 'argparse.FileType()',
            'stderr': 'argparse.FileType()',
            'enum': None,
        }
        arg_type = CWL_TO_PY_TYPES[arg.get_type()]
        if arg_type is list and type(arg_type) is list:
            return None
        else:
            return arg_type

    @staticmethod
    def _get_choices(arg):
        if arg.get_type() == 'enum':
            if type(arg.type) is list and arg.type[0] == 'null':
                return arg.type[1]['symbols']
            elif type(arg.type) is dict:
                return arg.type['symbols']

    @staticmethod
    def _get_default(arg):
        if arg.default:
            if type(arg.default) is str:
                return "\"" + arg.default + "\""    # for proper rendering in j2 template
            else:
                return arg.default


    @staticmethod
    def _get_actions(arg):
        if arg.optional and arg.get_type() == 'boolean':
            return 'store_true'
    
    @staticmethod
    def _get_nargs(arg):
        if arg.type == 'array':
           if arg.optional:
               return '*'
           else:
                return '+'


def write_code_to_file(filepath, code):
    with open(filepath, 'w') as f:
        f.write(code)


def cwl2argparse(file, dest, quiet=False, no_confirm=False, prefix=None):
    if not file.endswith('.cwl'):
        sys.exit('{0} is not a CWL tool definition'.format(file))
    try:
        tool = Tool(file)
    except yaml.scanner.ScannerError:
        sys.exit('File {0} is corrupted or not a CWL tool definition')
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
    function_name = file.split('/')[-1].replace('.cwl', '').replace('-', '_')
    result = template.render(tool=tool, args=args, function_name=function_name)
    filename = file.split('/')[-1].replace('.cwl', '.py')
    filepath = os.path.join(dest, filename)
    if no_confirm is False and os.path.exists(filepath):
        override = input('Filepath {0} already exists, override existing file? y/n '.format(filepath))
        if override in {'y', 'Y'}:
            write_code_to_file(filepath, result)
        else:
            print('File not overridden')
    else:
        write_code_to_file(filepath, result)
    if quiet is False:
        print(filename)
        print(result)
