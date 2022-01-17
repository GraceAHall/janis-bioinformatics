from datetime import datetime
from distutils import extension
from janis_core import (
    ToolInput,
    ToolOutput,
    ToolArgument,
    InputSelector,
    Filename,
)
from janis_core.operators.operator import IndexOperator

from janis_unix.tools.unixtool import UnixTool
from janis_bioinformatics.data_types import FastqGzPair, FastqGz


class LocaliseFastqGzPair(UnixTool):
    def tool(self):
        return "LocaliseFastqGzPair"

    def friendly_name(self):
        return "LocaliseFastqGzPair"

    def base_command(self):
        return None

    def inputs(self):
        return [
            ToolInput(
                "fastq",
                FastqGzPair,
                position=2,
            ),
            ToolInput(
                "outputRead1",
                Filename(
                    prefix=IndexOperator(InputSelector("reads"), 0), extension=".gz"
                ),
            ),
            ToolInput(
                "outputRead2",
                Filename(
                    prefix=IndexOperator(InputSelector("reads"), 1), extension=".gz"
                ),
            ),
        ]

    def outputs(self):
        return [
            ToolOutput(
                "out",
                FastqGzPair,
                selector=[
                    InputSelector("outputRead1"),
                    InputSelector("outputRead2"),
                ],
            )
        ]

    def arguments(self):
        return [
            ToolArgument("cp", position=1, shell_quote=False),
            ToolArgument(".", position=3, shell_quote=False),
        ]

    def tool_provider(self):
        return "Peter MacCallum Cancer Centre"

    def version(self):
        return "v0.1.0"

    def bind_metadata(self):
        self.metadata.dateCreated = datetime(2022, 1, 7)
        self.metadata.dateUpdated = datetime(2022, 1, 7)
        self.metadata.contributors = ["Jiaan Yu"]
        self.metadata.documentation = """\
Localise Arrary of FastqGZ pairs
        """
