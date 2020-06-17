from abc import ABC
from typing import List, Dict, Any

from janis_core import (
    ToolInput,
    Filename,
    File,
    Int,
    String,
    Boolean,
    ToolOutput,
    Array,
    InputSelector,
    WildcardSelector,
    Stdout,
    ToolArgument,
)
from janis_bioinformatics.data_types import Vcf, CompressedVcf
from janis_bioinformatics.tools.vcftools.vcftoolstoolbase import VcfToolsToolBase
from janis_core import ToolMetadata


class VcfToolsvcftoolsBase(VcfToolsToolBase, ABC):
    def tool(self):
        return "VcfTools"

    @classmethod
    def vcftools_command(cls):
        return "vcftools"

    def inputs(self):
        return [
            # bcf is not supported yet
            ToolInput(
                "vcf",
                Vcf(),
                prefix="--vcf",
                doc="This option defines the VCF file to be processed. VCFtools expects files in VCF format v4.0, v4.1 or v4.2. The latter two are supported  with  some  small limitations. If the user provides a dash character '-' as a file name, the program expects a VCF file to be piped in through standard in.",
            ),
            ToolInput(
                "outputFilename",
                Filename(extension=".vcf"),
                prefix="--out",
                doc='<output_prefix>. This option defines the output filename prefix for all files generated by vcftools. For example, if <prefix> is set to output_filename, then all output files will be of the form output_filename.*** . If this option is omitted, all output files will have the prefix "out." in the current working directory.',
            ),
            *self.additional_inputs,
        ]

    def outputs(self):
        return [ToolOutput("out", Vcf, glob=InputSelector("outputFilename"))]

    def friendly_name(self):
        return "VcfTools"

    def bind_metadata(self):
        from datetime import date

        return ToolMetadata(
            contributors=["Jiaan Yu"],
            dateCreated=date(2020, 5, 22),
            dateUpdated=date(2020, 5, 22),
            institution="VCFtools",
            doi=None,
            citation=None,
            keywords=["vcftools"],
            documentationUrl="https://vcftools.github.io/man_latest.html",
            documentation="""NAME
vcftools v0.1.16 − Utilities for the variant call format (VCF) and binary variant call format (BCF)

SYNOPSIS
vcftools [ --vcf FILE | --gzvcf FILE | --bcf FILE] [ --out OUTPUT PREFIX ] [ FILTERING OPTIONS ] [ OUTPUT OPTIONS ]

DESCRIPTION
vcftools is a suite of functions for use on genetic variation data in the form of VCF and BCF files. The tools provided will be used mainly to summarize data, run calculations on data, filter out data, and convert data into other useful file formats.
""".strip(),
        )

    additional_inputs = [
        ToolInput(
            "removeFileteredAll",
            Boolean(optional=True),
            prefix="--remove-filtered-all",
            position=1,
            shell_quote=False,
            doc="Removes all sites with a FILTER flag other than PASS.",
        ),
        ToolInput(
            "recode",
            Boolean(optional=True),
            prefix="--recode",
            position=1,
            shell_quote=False,
            doc="",
        ),
        ToolInput(
            "recodeINFOAll",
            Boolean(optional=True),
            prefix="--recode-INFO-all",
            position=1,
            shell_quote=False,
            doc="These options can be used with the above recode options to define an INFO key name to keep in the output  file.  This  option can be used multiple times to keep more of the INFO fields. The second option is used to keep all INFO values in the original file.",
        )
        # tbc
    ]
