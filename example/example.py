import argparse


def example():
    description="""
        Process some integers.here's some epilog text

    """
    parser = argparse.ArgumentParser(description=description)
    arg_keyword = parser.add_argument("arg_keyword",
       type=list,       help="""action keyword""",)
    arg_nargs2 = parser.add_argument("--nargs2",
       type=list,       help="""nargs2""",)
    arg_example_py = parser.add_argument("arg_example_py",
       type=argparse.FileType(),       default={'class': 'File', 'path': 'example.py'},)
    arg_store_true = parser.add_argument("--true",
       action="store_true",       help="""Store a true""",)
    arg_foo = parser.add_argument("--foo",
       type=str,       help="""foo help""",)
    arg_integers = parser.add_argument("arg_integers",
       type=list,       help="""an integer for the accumulator""",)
    arg_store_false = parser.add_argument("--false",
       action="store_true",       help="""Store a false""",)
    arg_mode = parser.add_argument("--mode",
       default="scissors",       choices=['rock', 'paper', 'scissors'],)
    arg_append = parser.add_argument("--append",
       type=list,       help="""Append a value""",)
    arg_bar = parser.add_argument("--bar",
       type=list,       default=[1, 2, 3],       help="""BAR!""",)

    return parser