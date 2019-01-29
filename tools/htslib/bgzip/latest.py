from bioinformatics.tools.htslib.bgzip.base import BGZipBase
from bioinformatics.tools.htslib.latest import HTSLibLatest


class BGZipLatest(HTSLibLatest, BGZipBase):
    pass


if __name__ == "__main__":
    print(BGZipLatest().help())
