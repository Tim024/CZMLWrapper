from .CZMLElement import CZMLElement
from .CZMLMaterial import CZMLMaterial

class CZMLPath(CZMLElement):
    name = "path"

    def __init__(self, **kwargs):
        super(CZMLPath, self).__init__(**kwargs)
        self.parameters += [
            {"key": "leadTime",
             "type": "int",
             "help": "Lead time of the path in seconds."},
            {"key": "trailTime",
             "type": "int",
             "help": "Trail time of the path in second."},
            CZMLMaterial()
        ]

    def _build_dict(self, **kwargs):
        if "leadTime" in kwargs.keys():
            leadTime = kwargs["leadTime"]
        else:
            leadTime = 0

        if "trailTime" in kwargs.keys():
            trailTime = kwargs["trailTime"]
        else:
            trailTime = 0

        self._dict = {
            "width": 1,
            "resolution": 100,
            "leadTime": leadTime,
            "trailTime": trailTime,
        }

        self._dict.update(CZMLMaterial(**kwargs).data)
