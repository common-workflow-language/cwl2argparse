import argparse


def GATK_HaplotypeCaller():
    description="""
        GATK-RealignTargetCreator.cwl is developed for CWL consortium
Call germline SNPs and indels via local re-assembly of haplotypes

    """
    parser = argparse.ArgumentParser(description=description)
    arg_java_arg = parser.add_argument("arg_java_arg",
       type=str,       default="-Xmx4g",)
    arg_reference = parser.add_argument("arg_reference",
       type=argparse.FileType(),)
    arg_inputBam_HaplotypeCaller = parser.add_argument("arg_inputBam_HaplotypeCaller",
       type=argparse.FileType(),       help="""bam f produced after printReads""",)
    arg_dbsnp = parser.add_argument("arg_dbsnp",
       type=argparse.FileType(),       help="""latest_dbsnp.vcf set of known indels""",)
    arg_outputfile_HaplotypeCaller = parser.add_argument("-o_1",
       type=str,       help="""name of the output f from HaplotypeCaller""",)
    arg_useFilteredReadsForAnnotations = parser.add_argument("--useFilteredReadsForAnnotations",
       action="store_true",       help="""Use the contamination-filtered read maps for the purposes of annotating variants""",)
    arg_useAllelesTrigger = parser.add_argument("--useAllelesTrigger",
       action="store_true",       help="""Use additional trigger on variants found in an external alleles f""",)
    arg_stand_emit_conf = parser.add_argument("--standard_min_confidence_threshold_for_emitting",
       type=float,       help="""The minimum phred-scaled confidence threshold at which variants should be emitted (and filtered with LowQual if less than the calling threshold)""",)
    arg_stand_call_conf = parser.add_argument("--standard_min_confidence_threshold_for_calling",
       type=float,       help="""The minimum phred-scaled confidence threshold at which variants should be called""",)
    arg_sample_ploidy = parser.add_argument("--sample_ploidy",
       type=int,       help="""Use additional trigger on variants found in an external alleles f""",)
    arg_sample_name = parser.add_argument("--sample_name",
       type=str,       help="""Use additional trigger on variants found in an external alleles f""",)
    arg_globalMAPQ = parser.add_argument("--phredScaledGlobalReadMismappingRate",
       type=int,       help="""The global assumed mismapping rate for reads""",)
    arg_pcr_indel_model = parser.add_argument("--pcr_indel_model",
       type=str,       help="""The PCR indel model to use""",)
    arg_output_mode = parser.add_argument("--output_mode",
       type=str,       help="""The PCR indel model to use""",)
    arg_numPruningSamples = parser.add_argument("--numPruningSamples",
       type=int,       help="""Number of samples that must pass the minPruning threshold""",)
    arg_minReadsPerAlignmentStart = parser.add_argument("--minReadsPerAlignmentStart",
       type=int,       help="""Minimum number of reads sharing the same alignment start for each genomic location in an active region""",)
    arg_minPruning = parser.add_argument("--minPruning",
       type=int,       help="""Minimum support to not prune paths in the graph""",)
    arg_minDanglingBranchLength = parser.add_argument("--minDanglingBranchLength",
       type=int,       help="""Minimum length of a dangling branch to attempt recovery""",)
    arg_min_base_quality_score = parser.add_argument("--min_base_quality_score",
       type=int,       help="""Minimum base quality required to consider a base for calling""",)
    arg_maxReadsInRegionPerSample = parser.add_argument("--maxReadsInRegionPerSample",
       type=int,       help="""Maximum reads in an active region""",)
    arg_maxNumHaplotypesInPopulation = parser.add_argument("--maxNumHaplotypesInPopulation",
       type=int,       help="""Maximum number of haplotypes to consider for your population""",)
    arg_max_alternate_alleles = parser.add_argument("--max_alternate_alleles",
       type=int,       help="""Maximum number of alternate alleles to genotype""",)
    arg_kmerSize = parser.add_argument("--kmerSize",
       type=list,       help="""Kmer size to use in the read threading assembler""",)
    arg_input_prior = parser.add_argument("--input_prior",
       type=list,       help="""Input prior for calls""",)
    arg_ERCIS = parser.add_argument("--indelSizeToEliminateInRefModel",
       type=int,       help="""The size of an indel to check for in the reference model""",)
    arg_indel_heterozygosity = parser.add_argument("--indel_heterozygosity",
       type=float,       help="""Heterozygosity for indel calling""",)
    arg_heterozygosity = parser.add_argument("--heterozygosity",
       type=float,       help="""Heterozygosity for indel calling""",)
    arg_GVCFGQBands = parser.add_argument("--GVCFGQBands",
       type=list,       help="""Input prior for calls""",)
    arg_group = parser.add_argument("--group",
       type=list,       help="""Input prior for calls""",)
    arg_graphOutput = parser.add_argument("--graphOutput",
       type=argparse.FileType(),       help="""Write debug assembly graph information to this f""",)
    arg_genotyping_mode = parser.add_argument("--genotyping_mode",
       type=str,       help="""The --genotyping_mode argument is an enumerated type (GenotypingOutputMode), which can have one of the following values""",)
    arg_gcpHMM = parser.add_argument("--gcpHMM",
       type=int,       help="""Flat gap continuation penalty for use in the Pair HMM""",)
    arg_forceActive = parser.add_argument("--forceActive",
       action="store_true",       help="""If provided, all bases will be tagged as active""",)
    arg_excludeAnnotation = parser.add_argument("--excludeAnnotation",
       type=list,       help="""One or more specific annotations to exclude""",)
    arg_emitRefConfidence = parser.add_argument("--emitRefConfidence",
       type=str,       help="""Mode for emitting reference confidence scores""",)
    arg_dontTrimActiveRegions = parser.add_argument("--dontTrimActiveRegions",
       action="store_true",       help="""If specified, we will not trim down the active region from the full region (active + extension) to just the active interval for genotyping""",)
    arg_dontIncreaseKmerSizesForCycles = parser.add_argument("--dontIncreaseKmerSizesForCycles",
       action="store_true",       help="""Disable iterating over kmer sizes when graph cycles are detected""",)
    arg_doNotRunPhysicalPhasing = parser.add_argument("--doNotRunPhysicalPhasing",
       action="store_true",       help="""As of GATK 3.3, HaplotypeCaller outputs physical (read-based) information (see version 3.3 release notes and documentation for details). This argument disables that behavior.""",)
    arg_disableOptimizations = parser.add_argument("--disableOptimizations",
       action="store_true",       help="""Dont skip calculations in ActiveRegions with no variants""",)
    arg_debug = parser.add_argument("--debug",
       action="store_true",       help="""Print out very verbose debug information about each triggering active region""",)
    arg_contamination = parser.add_argument("--contamination_fraction_to_filter",
       type=argparse.FileType(),       help="""Tab-separated File containing fraction of contamination in sequencing data (per sample) to aggressively remove. Format should be "" (Contamination is double) per line; No header.""",)
    arg_consensus = parser.add_argument("--consensus",
       action="store_true",       help="""Print out very verbose debug information about each triggering active region""",)
    arg_comp = parser.add_argument("--comp",
       type=list,       help="""comp binds reference ordered data. This argument supports ROD files of the following types BCF2, VCF, VCF3""",)
    arg_bandPassSigma = parser.add_argument("--consensus_1",
       type=float,       help="""The sigma of the band pass filter Gaussian kernel; if not provided defaults to Walker annotated default""",)
    arg_bamWriterType = parser.add_argument("--bamWriterType",
       type=str,       help="""Which haplotypes should be written to the BAM.""",)
    arg_bamOutput = parser.add_argument("--bamOutput",
       type=argparse.FileType(),       help="""File to which assembled haplotypes should be written""",)
    arg_annotation = parser.add_argument("--annotation",
       type=list,       help="""One or more specific annotations to apply to variant calls""",)
    arg_annotateNDA = parser.add_argument("--annotateNDA",
       action="store_true",       help="""If provided, we will annotate records with the number of alternate alleles that were discovered (but not necessarily genotyped) at a given site""",)
    arg_allSitePLs = parser.add_argument("--allSitePLs",
       action="store_true",       help="""Annotate all sites with PLs""",)
    arg_allowNonUniqueKmersInRef = parser.add_argument("--allowNonUniqueKmersInRef",
       action="store_true",       help="""Allow graphs that have non-unique kmers in the reference""",)
    arg_alleles = parser.add_argument("--alleles",
       type=list,       help="""The set of alleles at which to genotype when --genotyping_mode is GENOTYPE_GIVEN_ALLELES""",)
    arg_activityProfileOut = parser.add_argument("--activityProfileOut",
       type=argparse.FileType(),       help="""Output the raw activity profile results in IGV format""",)
    arg_activeRegionOut = parser.add_argument("--activeRegionOut",
       type=argparse.FileType(),       help="""Output the active region to this IGV formatted f""",)
    arg_activeRegionMaxSize = parser.add_argument("--activeRegionMaxSize",
       type=int,       help="""The active region maximum size; if not provided defaults to Walker annotated default""",)
    arg_activeRegionExtension = parser.add_argument("--activeRegionExtension",
       type=int,       help="""The active region extension; if not provided defaults to Walker annotated default""",)
    arg_activeProbabilityThreshold = parser.add_argument("--activeProbabilityThreshold",
       type=float,       help="""Threshold for the probability of a profile state being active.""",)
    arg_output_HaplotypeCaller = parser.add_argument("arg_output_HaplotypeCaller",
       type=argparse.FileType(),)

    return parser