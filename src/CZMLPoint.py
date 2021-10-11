from .CZMLElement import CZMLElement
from .CZMLPosition import CZMLPosition
from .CZMLShow import CZMLShow


class CZMLPoint(CZMLElement):
    name = "point"

    def __init__(self):
        super(CZMLPoint, self).__init__()
        self.parameters += [
            {"key": "rgbaf",
             "type": "list[3]",
             "mandatory": True,
             "help": "Color rgba as float."},
            {"key": "pixelSize",
             "type": "int",
             "help": "Size of the point when zooming."},
            CZMLShow()
        ]

    def _build_dict(self, **kwargs):
        rgbaf = kwargs["rgbaf"] if "rgbaf" in kwargs.keys() else [1, 0, 0, 1]
        pixelSize = 15 if "pixelSize" not in kwargs.keys() else kwargs["pixelSize"]

        self._dict = {
            "color": {
                "rgbaf": rgbaf,
            },
            "pixelSize": pixelSize,
        }
        self._dict.update(CZMLShow().dict(**kwargs))

