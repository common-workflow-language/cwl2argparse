import argparse


def picard_MergeSamFiles():
    description="""
        picard-MergeSamFiles.cwl is developed for CWL consortium

    """
    parser = argparse.ArgumentParser(description=description)
    arg_java_arg = parser.add_argument("arg_java_arg_1",
 type=str, default="-Xmx4g",)
    arg_outputFileName_mergedSam = parser.add_argument("arg_outputFileName_mergedSam",
 type=str, help="""SAM or BAM file to write merged result to Required
""",)
    arg_inputFileName_mergedSam = parser.add_argument("arg_inputFileName_mergedSam",
 type=list, help="""SAM or BAM input file Default value null. This option must be specified at least 1 times
""",)
    arg_readSorted = parser.add_argument("--ASSUME_SORTED",
 action="store_true", help="""If true, assume that the input files are in the same sort order as the requested output sort order, even if their headers say otherwise. Default value false. This option can be set to 'null' to clear the default value. Possible values {true, false}
""",)
    arg_mergeSequenceDictionaries = parser.add_argument("--MERGE_SEQUENCE_DICTIONARIES",
 action="store_true", help="""Merge the sequence dictionaries Default value false. This option can be set to null to clear the default value. Possible values {true, false}
""",)
    arg_useThreading = parser.add_argument("--USE_THREADING",
 action="store_true", help="""Option to create a background thread to encode, compress and write to disk the output file. The threaded version uses about 20% more CPU and decreases runtime by ~20% when writing out a compressed BAM file. Default value false. This option can be set to 'null' to clear the default value. Possible values {true, false}
""",)
    arg_comment = parser.add_argument("--COMMENT",
 type=str, help="""Comment(s) to include in the merged output files header. Default value null. This option may be specified 0 or more times
""",)
    arg_tmpdir = parser.add_argument("arg_tmpdir",
 type=str, help="""Default value null. This option may be specified 0 or more times.
""",)
    arg_mergeSam_output = parser.add_argument("arg_mergeSam_output",
 type=argparse.FileType(),)

    return parser