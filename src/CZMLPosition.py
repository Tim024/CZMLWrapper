from .CZMLElement import CZMLElement
from .exceptions import InputException
from .utils import format_date, name_to_id, check_equal


class CZMLPosition(CZMLElement):
    name = "position"

    def __init__(self):
        super(CZMLPosition, self).__init__()
        self.parameters += [
            {"key": "interpolation.",
             "type": "boolean",
             "help": "Set interpolation to Lagrange degree 2."},
            {"key": "frame",
             "type": "str",
             "help": "Set the reference frame of the position (INERTIAL or FIXED)."},
            {"key": "cartesian",
             "type": "list[array[3]]",
             "help": "List of positions in x,y,z coordinates in meters.",
             "exclude": "reference, cartographicDegrees"},
            {"key": "cartographicDegrees",
             "type": "list[list[3]]",
             "help": "List of positions in x,y,z lon,lat,height in deg,deg,meters.",
             "exclude": "cartesian, reference"},
            {"key": "reference",
             "type": "list[str]",
             "help": "List of names of objects.",
             "exclude": "cartesian, cartographicDegrees"},
            {"key": "dates",
             "type": "list[datetime]",
             "help": "Datetime of each position. Works best with interpolation.",
             "include": "cartesian, reference"},
        ]

    def _build_dict(self, **kwargs):
        if check_equal(kwargs, "interpolation", True):
            self._dict.update({"interpolationAlgorithm": "LAGRANGE", "interpolationDegree": 2})
        if "frame" in kwargs.keys():
            self._dict.update({"referenceFrame": kwargs["frame"]})
        if "cartesian" in kwargs.keys():
            if "dates" in kwargs.keys():
                if len(kwargs["dates"]) != len(kwargs["cartesian"]):
                    raise InputException("Length of dates and cartesian should be the same.")
                positions = []
                for i, p in enumerate(kwargs["cartesian"]):
                    positions.append(format_date(kwargs["dates"][i]))
                    positions.append(p[0])
                    positions.append(p[1])
                    positions.append(p[2])
                self._dict.update({"cartesian": positions})
            else:
                self._dict.update({"cartesian": kwargs["cartesian"]})
        elif "reference" in kwargs.keys():
            if "dates" in kwargs.keys():
                if len(kwargs["dates"]) != len(kwargs["reference"]):
                    raise InputException("Length of dates and references should be the same.")
                positions = []
                for i, p in enumerate(kwargs["reference"]):
                    positions.append(format_date(kwargs["dates"][i]))
                    positions.append(name_to_id(p) + "#position")
                self._dict.update({"references": positions})
            else:
                self._dict.update({"references": [name_to_id(p) + "#position" for p in kwargs["reference"]]})
        elif "cartographicDegrees" in kwargs.keys():
            if "dates" in kwargs.keys():
                if len(kwargs["dates"]) != len(kwargs["cartographicDegrees"]):
                    raise InputException("Length of dates and references should be the same.")
                positions = []
                for i, p in enumerate(kwargs["cartographicDegrees"]):
                    positions.append(format_date(kwargs["dates"][i]))
                    positions.append(p[0])
                    positions.append(p[1])
                    positions.append(p[2])
                self._dict.update({"cartographicDegrees": positions})
            else:
                self._dict.update({"cartographicDegrees": kwargs["cartographicDegrees"]})

class CZMLPositions(CZMLElement):
    name = "positions"

    def __init__(self):
        super(CZMLPositions, self).__init__()
        self.parameters += [
            {"key": "cartesian",
             "type": "list[array[3]]",
             "help": "List of positions in x,y,z coordinates in meters.",
             "exclude": "reference"},
            {"key": "reference",
             "type": "list[str]",
             "help": "List of names of objects.",
             "exclude": "cartesian"},
        ]

    def _build_dict(self, **kwargs):
        if "cartesian" in kwargs.keys():
            self._dict.update({"cartesian": kwargs["cartesian"]})
        elif "reference" in kwargs.keys():
            self._dict.update({"references": [name_to_id(p) + "#position" for p in kwargs["reference"]]})


