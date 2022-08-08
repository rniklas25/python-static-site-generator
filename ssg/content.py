import re

from collections.abc import Mapping
from yaml import load, FullLoader

class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = cls.__regex.split(string=2)