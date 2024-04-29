from .CZMLMaterial import CZMLMaterial
from .CZMLPositions import CZMLPositions
from .CZMLElement import CZMLElement
from .CZMLShow import CZMLShow


class CZMLCylinder(CZMLElement):
    name = "cylinder"

    def __init__(self, **kwargs):
        super(CZMLCylinder, self).__init__(**kwargs)
        self.parameters += [
            {
                "key": "length",
                "type": "float",
                "help": "Length of the cylinder, in meters.",
                "mandatory": "True",
            },
            {
                "key": "topRadius",
                "type": "float",
                "help": "Top radius of the cylinder, in meters.",
                "mandatory": "True",
            },
            {
                "key": "bottomRadius",
                "type": "float",
                "help": "Bottom radius of the cylinder, in meters.",
                "mandatory": "True",
            },
            CZMLMaterial(),
        ]

    def _build_dict(self, **kwargs):
        self._dict = {
            "length": kwargs["length"],
            "topRadius": kwargs["topRadius"],
            "bottomRadius": kwargs["bottomRadius"],
        }
        self._dict.update(CZMLMaterial(**kwargs).data)
