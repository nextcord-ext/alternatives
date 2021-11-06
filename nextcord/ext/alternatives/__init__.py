import collections


_VersionInfo = collections.namedtuple("_VersionInfo", "year month day release serial")

version = "2021.1"
version_info = _VersionInfo(2021, 0, 1, "final", 0)
