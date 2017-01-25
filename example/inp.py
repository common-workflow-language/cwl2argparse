import argparse


def parser():
    description="""
        prints a string to a standard output
    """
    parser = argparse.ArgumentParser(description=description)
    example_flag = parser.add_argument("example_flag",
       type=bool,)
    example_file = parser.add_argument("--file",
       type=argparse.FileType(),)
    example_string = parser.add_argument("example_string",
       type=str,)
    example_int = parser.add_argument("example_int",
       type=list,       nargs="+",)

    return parser