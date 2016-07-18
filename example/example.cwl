#!/usr/bin/env cwl-runner
# This tool description was generated automatically by argparse2cwl ver. 0.2.7
# To generate again: $ example.py -b python -go --map_ids --generate_cwl_tool
# Help: $ example.py  --help_arg2cwl

cwlVersion: "cwl:v1.0"

class: CommandLineTool
baseCommand: ['python']

description: |
  Process some integers.here's some epilog text

inputs:
  example.py:
    type: File
    default:
      class: File
      path: example.py
    inputBinding:
      position: 0


  keyword:
    type:
      type: array
      items: string
  
    description: action keyword
    inputBinding:
      position: 1


  integers:
    type:
      type: array
      items: int
  
    description: an integer for the accumulator
    inputBinding:
      position: 2


  foo:
    type: ["null", string]
    description: foo help
    inputBinding:
      prefix: --foo 


  bar:
    type:
    - "null"
    - type: array
      items: string
  
    default: [1, 2, 3]
    description: BAR!
    inputBinding:
      prefix: --bar 


  store_true:
    type: ["null", boolean]
    default: False
    description: Store a true
    inputBinding:
      prefix: --true 


  store_false:
    type: ["null", boolean]
    default: True
    description: Store a false
    inputBinding:
      prefix: --false 


  append:
    type:
    - "null"
    - type: array
      items: string
  
    description: Append a value
    inputBinding:
      prefix: --append 


  nargs2:
    type:
    - "null"
    - type: array
      items: string
  
    description: nargs2
    inputBinding:
      prefix: --nargs2 


  mode:
    type:
    - "null"
    - type: enum
      symbols: ['rock', 'paper', 'scissors']
    default: scissors
  
    inputBinding:
      prefix: --mode 


outputs:
    []
