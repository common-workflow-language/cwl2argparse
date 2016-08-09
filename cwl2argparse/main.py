import os

import argparse as ap
import sys

from cwl2argparse.cwl_argparse_translation import cwl2argparse


def main():
    help_text = """
        cwl2argparse generates an argparse definition from CWL tool arguments
        that can be pasted in a Python program and used
        Example: $ cwl2argparse FILES [FILES ...] <options>
        """
    parser = ap.ArgumentParser(description=help_text, formatter_class=ap.RawDescriptionHelpFormatter)
    parser.add_argument('files', nargs='+', help='CWL tool descriptions or directories with tools')
    parser.add_argument('-p', '--prefix', help='Prefix to be added to all argument variables')
    parser.add_argument('-d', '--dest', help='Directory to store resulting .py files')
    parser.add_argument('-q', '--quiet', action='store_true', help="Do not print generated code to system output")
    parser.add_argument('-y', action='store_true', help="Override existing files without confirmation")
    args = parser.parse_args()

    files = args.files
    dest = args.dest or os.getcwd()
    for f in files:
        if os.path.isfile(f):
            cwl2argparse(f, dest, args.quiet, args.y, args.prefix)
        elif os.path.isdir(f):
            for file in os.listdir(f):
                cwl2argparse(os.path.join(f, file), dest, args.prefix)
        else:
            print("Couldn't process {0}: neither file nor directory".format(f))
    print('Generated to {0}'.format(os.path.abspath(dest)))
    sys.exit(0)


if __name__ == '__main__':
    main()
