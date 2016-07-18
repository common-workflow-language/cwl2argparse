import argparse

description="""
    bowtie.cwl is developed for CWL consortium

Usage: 
bowtie [options]* <ebwt> {-1 <m1> -2 <m2> | --12 <r> | <s>} [<hit>]

  <m1>    Comma-separated list of files containing upstream mates (or the
          sequences themselves, if -c is set) paired with mates in <m2>
  <m2>    Comma-separated list of files containing downstream mates (or the
          sequences themselves if -c is set) paired with mates in <m1>
  <r>     Comma-separated list of files containing Crossbow-style reads.  Can be
          a mixture of paired and unpaired.  Specify "-"for stdin.
  <s>     Comma-separated list of files containing unpaired reads, or the
          sequences themselves, if -c is set.  Specify "-"for stdin.
  <hit>   File to write hits to (default: stdout)
Input:
  -q                 query input files are FASTQ .fq/.fastq (default)
  -f                 query input files are (multi-)FASTA .fa/.mfa
  -r                 query input files are raw one-sequence-per-line
  -c                 query sequences given on cmd line (as <mates>, <singles>)
  -C                 reads and index are in colorspace
  -Q/--quals <file>  QV file(s) corresponding to CSFASTA inputs; use with -f -C
  --Q1/--Q2 <file>   same as -Q, but for mate files 1 and 2 respectively
  -s/--skip <int>    skip the first <int> reads/pairs in the input
  -u/--qupto <int>   stop after first <int> reads/pairs (excl. skipped reads)
  -5/--trim5 <int>   trim <int> bases from 5' (left) end of reads
  -3/--trim3 <int>   trim <int> bases from 3' (right) end of reads
  --phred33-quals    input quals are Phred+33 (default)
  --phred64-quals    input quals are Phred+64 (same as --solexa1.3-quals)
  --solexa-quals     input quals are from GA Pipeline ver. < 1.3
  --solexa1.3-quals  input quals are from GA Pipeline ver. >= 1.3
  --integer-quals    qualities are given as space-separated integers (not ASCII)
  --large-index      force usage of a 'large' index, even if a small one is present
Alignment:
  -v <int>           report end-to-end hits w/ <=v mismatches; ignore qualities
    or
  -n/--seedmms <int> max mismatches in seed (can be 0-3, default: -n 2)
  -e/--maqerr <int>  max sum of mismatch quals across alignment for -n (def: 70)
  -l/--seedlen <int> seed length for -n (default: 28)
  --nomaqround       disable Maq-like quality rounding for -n (nearest 10 <= 30)
  -I/--minins <int>  minimum insert size for paired-end alignment (default: 0)
  -X/--maxins <int>  maximum insert size for paired-end alignment (default: 250)
  --fr/--rf/--ff     -1, -2 mates align fw/rev, rev/fw, fw/fw (default: --fr)
  --nofw/--norc      do not align to forward/reverse-complement reference strand
  --maxbts <int>     max # backtracks for -n 2/3 (default: 125, 800 for --best)
  --pairtries <int>  max # attempts to find mate for anchor hit (default: 100)
  -y/--tryhard       try hard to find valid alignments, at the expense of speed
  --chunkmbs <int>   max megabytes of RAM for best-first search frames (def: 64)
Reporting:
  -k <int>           report up to <int> good alignments per read (default: 1)
  -a/--all           report all alignments per read (much slower than low -k)
  -m <int>           suppress all alignments if > <int> exist (def: no limit)
  -M <int>           like -m, but reports 1 random hit (MAPQ=0); requires --best
  --best             hits guaranteed best stratum; ties broken by quality
  --strata           hits in sub-optimal strata aren't reported (requires --best)
Output:
  -t/--time          print wall-clock time taken by search phases
  -B/--offbase <int> leftmost ref offset = <int> in bowtie output (default: 0)
  --quiet            print nothing but the alignments
  --refout           write alignments to files refXXXXX.map, 1 map per reference
  --refidx           refer to ref. seqs by 0-based index rather than name
  --al <fname>       write aligned reads/pairs to file(s) <fname>
  --un <fname>       write unaligned reads/pairs to file(s) <fname>
  --max <fname>      write reads/pairs over -m limit to file(s) <fname>
  --suppress <cols>  suppresses given columns (comma-delim'ed) in default output
  --fullref          write entire ref name (default: only up to 1st space)
Colorspace:
  --snpphred <int>   Phred penalty for SNP when decoding colorspace (def: 30)
     or
  --snpfrac <dec>    approx. fraction of SNP bases (e.g. 0.001); sets --snpphred
  --col-cseq         print aligned colorspace seqs as colors, not decoded bases
  --col-cqual        print original colorspace quals, not decoded quals
  --col-keepends     keep nucleotides at extreme ends of decoded alignment
SAM:
  -S/--sam           write hits in SAM format
  --mapq <int>       default mapping quality (MAPQ) to print for SAM alignments
  --sam-nohead       supppress header lines (starting with @) for SAM output
  --sam-nosq         supppress @SQ header lines for SAM output
  --sam-RG <text>    add <text> (usually "lab=value") to @RG line of SAM header
Performance:
  -o/--offrate <int> override offrate of index; must be >= index's offrate
  -p/--threads <int> number of alignment threads to launch (default: 1)
  --mm               use memory-mapped I/O for index; many 'bowtie's can share
  --shmem            use shared mem for index; many 'bowtie's can share
Other:
  --seed <int>       seed for random number generator
  --verbose          verbose output (for debugging)
  --version          print version information and quit
  -h/--help          print this usage message

"""
parser = argparse.ArgumentParser(description=description)
arg_ebwt = parser.add_argument("arg_ebwt",
 type=str, help="""The basename of the index to be searched. The basename is the name of any of the index files up to but not including the final .1.ebwt / .rev.1.ebwt / etc. bowtie looks for the specified index first in the current directory, then in the indexes subdirectory under the directory where the bowtie executable is located, then looks in the directory specified in the BOWTIE_INDEXES environment variable.
""",)
arg_filelist = parser.add_argument("arg_filelist",
 type=list, help="""{-1 <m1> -2 <m2> | --12 <r> | <s>}
<m1>    Comma-separated list of files containing upstream mates (or the
      sequences themselves, if -c is set) paired with mates in <m2>
<m2>    Comma-separated list of files containing downstream mates (or the
      sequences themselves if -c is set) paired with mates in <m1>
<r>     Comma-separated list of files containing Crossbow-style reads.  Can be
      a mixture of paired and unpaired.  Specify "-"for stdin.
<s>     Comma-separated list of files containing unpaired reads, or the
      sequences themselves, if -c is set.  Specify "-"for stdin.
""",)
arg_filelist_mates = parser.add_argument("--filelist_mates",
 type=list,)
arg_filename = parser.add_argument("arg_filename",
 type=str,)
arg_q = parser.add_argument("-q",
 action="store_true", help="""query input files are FASTQ .fq/.fastq (default)
""",)
arg_f = parser.add_argument("-f",
 action="store_true", help="""query input files are (multi-)FASTA .fa/.mfa
""",)
arg_r = parser.add_argument("-r",
 action="store_true", help="""query input files are raw one-sequence-per-line
""",)
arg_c = parser.add_argument("-c",
 action="store_true", help="""query sequences given on cmd line (as <mates>, <singles>)
""",)
arg_C = parser.add_argument("-C",
 action="store_true", help="""reads and index are in colorspace
""",)
arg_Q = parser.add_argument("-Q",
 type=argparse.FileType(), help="""--quals <file>  QV file(s) corresponding to CSFASTA inputs; use with -f -C
""",)
arg_Q1 = parser.add_argument("--Q1",
 action="store_true", help="""--Q2 <file>   same as -Q, but for mate files 1 and 2 respectively
""",)
arg_s = parser.add_argument("-s",
 type=int, help="""--skip <int>    skip the first <int> reads/pairs in the input
""",)
arg_u = parser.add_argument("-u",
 type=int, help="""--qupto <int>   stop after first <int> reads/pairs (excl. skipped reads)
""",)
arg_5 = parser.add_argument("-5",
 type=int, help="""--trim5 <int>   trim <int> bases from 5' (left) end of reads
""",)
arg_3 = parser.add_argument("-3",
 type=int, help="""--trim3 <int>   trim <int> bases from 3' (right) end of reads
""",)
arg_phred33_quals = parser.add_argument("--phred33-quals",
 action="store_true", help="""input quals are Phred+33 (default)
""",)
arg_phred64_quals = parser.add_argument("--phred64-quals",
 action="store_true", help="""input quals are Phred+64 (same as --solexa1.3-quals)
""",)
arg_solexa_quals = parser.add_argument("--solexa-quals",
 action="store_true", help="""input quals are from GA Pipeline ver. < 1.3
""",)
arg_solexa1_3_quals = parser.add_argument("--solexa1.3-quals",
 action="store_true", help="""input quals are from GA Pipeline ver. >= 1.3
""",)
arg_integer_quals = parser.add_argument("--integer-quals",
 action="store_true", help="""qualities are given as space-separated integers (not ASCII)
""",)
arg_large_index = parser.add_argument("--large-index",
 action="store_true", help="""force usage of a 'large' index, even if a small one is present
Alignment:
""",)
arg_v = parser.add_argument("-v",
 type=int, help="""<int>           report end-to-end hits w/ <=v mismatches; ignore qualities
or
""",)
arg_n = parser.add_argument("-n",
 type=int, help="""--seedmms <int> max mismatches in seed (can be 0-3, default: -n 2)
""",)
arg_e = parser.add_argument("-e",
 type=int, help="""--maqerr <int>  max sum of mismatch quals across alignment for -n (def: 70)
""",)
arg_l = parser.add_argument("-l",
 type=int, help="""--seedlen <int> seed length for -n (default: 28)
""",)
arg_nomaqround = parser.add_argument("--nomaqround",
 action="store_true", help="""disable Maq-like quality rounding for -n (nearest 10 <= 30)
""",)
arg_I = parser.add_argument("-I",
 type=int, help="""--minins <int>  minimum insert size for paired-end alignment (default: 0)
""",)
arg_X = parser.add_argument("-X",
 type=int, help="""--maxins <int>  maximum insert size for paired-end alignment (default: 250)
""",)
arg_fr = parser.add_argument("--fr",
 action="store_true", help="""--rf/--ff     -1, -2 mates align fw/rev, rev/fw, fw/fw (default: --fr)
""",)
arg_nofw = parser.add_argument("--nofw",
 action="store_true", help="""--norc      do not align to forward/reverse-complement reference strand
""",)
arg_maxbts = parser.add_argument("--maxbts",
 type=int, help="""<int>     max # backtracks for -n 2/3 (default: 125, 800 for --best)
""",)
arg_pairtries = parser.add_argument("--pairtries",
 type=int, help="""<int>  max # attempts to find mate for anchor hit (default: 100)
""",)
arg_y = parser.add_argument("-y",
 action="store_true", help="""--tryhard       try hard to find valid alignments, at the expense of speed
""",)
arg_chunkmbs = parser.add_argument("--chunkmbs",
 type=int, help="""<int>   max megabytes of RAM for best-first search frames (def: 64)
Reporting:
""",)
arg_k = parser.add_argument("-k",
 type=int, help="""<int>           report up to <int> good alignments per read (default: 1)
""",)
arg_a = parser.add_argument("-a",
 action="store_true", help="""--all           report all alignments per read (much slower than low -k)
""",)
arg_m = parser.add_argument("-m",
 type=int, help="""<int>           suppress all alignments if > <int> exist (def: no limit)
""",)
arg_M = parser.add_argument("-M",
 type=int, help="""<int>           like -m, but reports 1 random hit (MAPQ=0); requires --best
""",)
arg_best = parser.add_argument("--best",
 action="store_true", help="""hits guaranteed best stratum; ties broken by quality
""",)
arg_strata = parser.add_argument("--strata",
 action="store_true", help="""hits in sub-optimal strata aren't reported (requires --best)
Output:
""",)
arg_t = parser.add_argument("-t",
 action="store_true", help="""--time          print wall-clock time taken by search phases
""",)
arg_B = parser.add_argument("-B",
 type=int, help="""--offbase <int> leftmost ref offset = <int> in bowtie output (default: 0)
""",)
arg_quiet = parser.add_argument("--quiet",
 action="store_true", help="""print nothing but the alignments
""",)
arg_refout = parser.add_argument("--refout",
 action="store_true", help="""write alignments to files refXXXXX.map, 1 map per reference
""",)
arg_refidx = parser.add_argument("--refidx",
 action="store_true", help="""refer to ref. seqs by 0-based index rather than name
""",)
arg_al = parser.add_argument("--al",
 action="store_true", help="""<fname>       write aligned reads/pairs to file(s) <fname>
""",)
arg_un = parser.add_argument("--un",
 action="store_true", help="""<fname>       write unaligned reads/pairs to file(s) <fname>
""",)
arg_max = parser.add_argument("--max",
 action="store_true", help="""<fname>      write reads/pairs over -m limit to file(s) <fname>
""",)
arg_suppress = parser.add_argument("--suppress",
 action="store_true", help="""<cols>  suppresses given columns (comma-delim'ed) in default output
""",)
arg_fullref = parser.add_argument("--fullref",
 action="store_true", help="""write entire ref name (default: only up to 1st space)
Colorspace:
""",)
arg_snpphred = parser.add_argument("--snpphred",
 type=int, help="""<int>   Phred penalty for SNP when decoding colorspace (def: 30)
or
""",)
arg_snpfrac = parser.add_argument("--snpfrac",
 action="store_true", help="""<dec>    approx. fraction of SNP bases (e.g. 0.001); sets --snpphred
""",)
arg_col_cseq = parser.add_argument("--col-cseq",
 action="store_true", help="""print aligned colorspace seqs as colors, not decoded bases
""",)
arg_col_cqual = parser.add_argument("--col-cqual",
 action="store_true", help="""print original colorspace quals, not decoded quals
""",)
arg_col_keepends = parser.add_argument("--col-keepends",
 action="store_true", help="""keep nucleotides at extreme ends of decoded alignment
SAM:
""",)
arg_sam = parser.add_argument("-S",
 action="store_true", help="""--sam           write hits in SAM format
""",)
arg_mapq = parser.add_argument("--mapq",
 type=int, help="""<int>       default mapping quality (MAPQ) to print for SAM alignments
""",)
arg_sam_nohead = parser.add_argument("--sam-nohead",
 action="store_true", help="""supppress header lines (starting with @) for SAM output
""",)
arg_sam_nosq = parser.add_argument("--sam-nosq",
 action="store_true", help="""supppress @SQ header lines for SAM output
""",)
arg_sam_RG = parser.add_argument("--sam-RG",
 type=str, help="""<text>    add <text> (usually "lab=value") to @RG line of SAM header
Performance:
""",)
arg_o = parser.add_argument("-o",
 type=int, help="""--offrate <int> override offrate of index; must be >= index's offrate
""",)
arg_p = parser.add_argument("-p",
 type=int, help="""--threads <int> number of alignment threads to launch (default: 1)
""",)
arg_mm = parser.add_argument("--mm",
 action="store_true", help="""use memory-mapped I/O for index; many 'bowtie's can share
""",)
arg_shmem = parser.add_argument("--shmem",
 action="store_true", help="""use shared mem for index; many 'bowtie's can share
Other:
""",)
arg_seed = parser.add_argument("--seed",
 type=int, help="""<int>       seed for random number generator
""",)
arg_verbose = parser.add_argument("--verbose",
 action="store_true", help="""verbose output (for debugging)
""",)
arg_output = parser.add_argument("arg_output",
 type=argparse.FileType(),)
arg_output_bowtie_log = parser.add_argument("arg_output_bowtie_log",
 type=argparse.FileType(),)

args = parser.parse_args()