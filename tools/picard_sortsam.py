from Pipeline.bioinformatics.data_types.bai import Bai
from Pipeline.bioinformatics.data_types.bam import Bam
from Pipeline import Filename, String, Int, CommandTool, ToolOutput, ToolInput, Boolean, ToolArgument
from Pipeline.bioinformatics.data_types.bampair import BamPair
from Pipeline.bioinformatics.data_types.sam import Sam


class PicardSortSam(CommandTool):
    inputSam = ToolInput("inputSam", Sam(), position=4, prefix="INPUT=", separate_value_from_prefix=False,
                         doc="The BAM or SAM file to sort.")
    validation_stringency = ToolInput("validation_stringency", String(), prefix="VALIDATION_STRINGENCY=", position=10,
                                      separate_value_from_prefix=False)

    out = ToolOutput("out", Bam(), glob="$(inputs.outputFilename)")                                # Bam file
    index = ToolOutput("index", Bai(), glob='$(inputs.outputFilename.replace(".bam", ".bai"))')    # Bai Index
    pair = ToolOutput("pair", BamPair(), glob="$(inputs.outputFilename)", doc=".bam + .bai as secondary")


    @staticmethod
    def tool():
        return "picard-sortsam"

    @staticmethod
    def base_command():
        return "java"

    @staticmethod
    def docker():
        return "biocontainers/picard:v2.3.0_cv3"

    @staticmethod
    def doc():
        return "picard-SortSam.cwl is developed for CWL consortium. Generates a sorted file."

    def arguments(self):
        return [
            ToolArgument("/opt/conda/share/picard-2.3.0-0/picard.jar", position=2, prefix="-jar"),
            ToolArgument("SortSam", position=3)
        ]

    outputFilename = ToolInput("outputFilename", Filename(extension=".bam"), position=5, prefix="OUTPUT=",
                                       separate_value_from_prefix=False, doc="The sorted BAM or SAM output file.")

    createIndex = ToolInput("createIndex", String(), default="true", position=8, prefix="CREATE_INDEX=",
                            separate_value_from_prefix=False,
                            doc="Whether to create a BAM index when writing a coordinate-sorted BAM file. "
                                "Default value True. This option can be set to 'null' to clear the default value. "
                                "Possible values {true, false}")

    soCoordinate = ToolInput("soInput", String(), default="coordinate", position=6, prefix="SORT_ORDER=",
                             separate_value_from_prefix=False,
                             doc="Sort order of output file Required. "
                                 "Possible values {unsorted, queryname, coordinate, duplicate}")

    javaArg = ToolInput("javaArg", String(), default="-Xmx2g", position=1)
    maxRecordsInRam = ToolInput("maxRecordsInRam", Int(optional=True), prefix="MAX_RECORDS_IN_RAM=", position=13,
                                separate_value_from_prefix=False)

    tmpdir = ToolInput("tmpdir", Filename(extension="\\"), prefix="TMP_DIR=", position=7,
                       separate_value_from_prefix=False,
                       doc="This option may be specified 0 or more times.")


if __name__ == "__main__":
    print(PicardSortSam().help())