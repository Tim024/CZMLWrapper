from .CZMLElement import CZMLElement
from .CZMLMaterial import CZMLMaterial
from .CZMLPosition import CZMLPositions
from .CZMLShow import CZMLShow


class CZMLPolyline(CZMLElement):
    name = "polyline"

    def __init__(self):
        super(CZMLPolyline, self).__init__()
        self.parameters += [
            {"key": "arcType",
             "type": "str",
             "help": "Arc type of the polyline (NONE, RHUMB, GEODESIC, default:GEODESIC)."},
            {"key": "width",
             "type": "float",
             "help": "Width of the line, default:5."},
            CZMLPositions(),
            CZMLMaterial(),
            CZMLShow(),
        ]

    def _build_dict(self, **kwargs):
        if "arcType" in kwargs:
            ac = kwargs["arcType"]
        else:
            ac = "GEODESIC"

        if "width" in kwargs:
            w = kwargs["width"]
        else:
            w = 1

        self._dict = {
            "arcType": ac,
            "width": w,
        }
        self._dict.update(CZMLMaterial().dict(**kwargs))
        self._dict.update(CZMLShow().dict(**kwargs))
        self._dict.update(CZMLPositions().dict(**kwargs))

