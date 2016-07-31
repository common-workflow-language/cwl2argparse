# cwl2argparse
cwl2argparse generates an argparse definition from CWL tool arguments that can be pasted in a Python program and used

`search.cwl`

    #!/usr/bin/env cwl-runner
    cwlVersion: "cwl:draft-3"
    class: CommandLineTool
    baseCommand: ['search.py']
    
    description: |
      Toy program to search inverted index and print out each line the term appears
    inputs:
      - id: mainfile
      type: File
      description: Text file to be indexed
      inputBinding:
        position: 1
    
    - id: term
      type: string
      description: Term for search
      inputBinding:
        position: 2
    
    outputs:
        []

Result
`search.py`

    import argparse
    
    
    def search():
        description="""
            Toy program to search inverted index and print out each line the term appears
        """
        
        parser = argparse.ArgumentParser(description=description)
        arg_mainfile = parser.add_argument("arg_mainfile",
            type=argparse.FileType(),       help="""Text file to be indexed""",)
        arg_term = parser.add_argument("arg_term",
            type=str,       help="""Term for search""",)
    
        return parser



## Installation ##

    $ pip install cwl2argparse
  
## Running ##

    cwl2argparse FILES [FILES ...] [options]
    
Options:
* `FILES` - a list of CWL tool descriptions or directories with tools
*   `-p`, `--prefix` - Prefix to be added to all argument variables in resulting Python code.

For instance, providing `arg_` as a prefix will result in generating the next lines for the example above:

        arg_mainfile = parser.add_argument("mainfile",
            type=argparse.FileType(),help="""Text file to be indexed""",)
        arg_term = parser.add_argument("term",
            type=str,help="""Term for search""",)
  
  
* `-d`, `--dest` - Destination directory to store resulting .py files
