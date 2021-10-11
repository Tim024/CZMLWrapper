from .CZMLElement import CZMLElement
from .exceptions import InputException


class CZMLOrientation(CZMLElement):
    name = "orientation"

    def __init__(self):
        super(CZMLOrientation, self).__init__()
        self.parameters += [
            {"key": "onVelocity",
             "type": "bool",
             "help": "Set the orientation relative to the velocity of the object.",
             "include": "position"
             },
        ]

    def _build_dict(self, **kwargs):
        if "onVelocity" in kwargs.keys() and kwargs["onVelocity"]:
            self._dict = {
                "velocityReference": "#position"
            }
        else:
            InputException("Undefined orientation.. only velocity for now")
