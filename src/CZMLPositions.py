from .CZMLElement import CZMLElement
from .exceptions import InputException
from .utils import format_date, name_to_id, check_equal


class CZMLPositions(CZMLElement):
    name = "positions"

    def __init__(self, **kwargs):
        super(CZMLPositions, self).__init__(**kwargs)
        self.parameters += [
            {"key": "cartesian",
             "type": "list]",
             "help": "List of positions in x,y,z coordinates in meters. Example: [x1,y1,z1,x2,y2,z2...etc]",
             "exclude": "reference"},
            {"key": "reference",
             "type": "list[str]",
             "help": "List of names of objects.",
             "exclude": "cartesian"},
            {"key": "cartographicDegrees",
             "type": "list",
             "help": "List of positions in lon,lat,height in deg,deg,meters. Example: [l1,l1,h1,l2,l2,h2...etc]."
                     "",
             "exclude": "cartesian, reference"},
            # {"key": "availability",
            #  "mandatory": False,
            #  "type": "list[tuple(datetime, datetime)]",
            #  "help": "Interval of availability in datetime. If this parameter is specfied, the positions are expected"
            #          " to be a list of list, of the same length as availbability. The positions specified"},
            # {"key": "interval",
            #  "mandatory": True,
            #  "type": "tuple(datetime, datetime)",
            #  "help": "Interval of availability in datetime."},
        ]

    def _build_dict(self, **kwargs):
        if "cartesian" in kwargs.keys():
            self._dict.update({"cartesian": kwargs["cartesian"]})
        elif "reference" in kwargs.keys():
            self._dict.update({"references": [name_to_id(p) + "#position" for p in kwargs["reference"]]})
        elif "cartographicDegrees" in kwargs.keys():
            self._dict.update({"cartographicDegrees": kwargs["cartographicDegrees"]})
