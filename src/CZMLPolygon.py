from .CZMLMaterial import CZMLMaterial
from .CZMLPosition import CZMLPositions
from .CZMLElement import CZMLElement


class CZMLPolygon(CZMLElement):
    name = "polygon"

    def __init__(self, **kwargs):
        super(CZMLPolygon, self).__init__(**kwargs)
        self.parameters += [
            {"key": "perPositionHeight",
             "type": "boolean",
             "help": "Defines if we consider the height position."},
            CZMLPositions(),
            CZMLMaterial(),
        ]

    def _build_dict(self, **kwargs):
        perPositionHeight = True if "perPositionHeight" not in kwargs.keys() else kwargs["perPositionHeight"]

        self._dict = {
            "perPositionHeight": perPositionHeight,
        }
        self._dict.update(CZMLMaterial(**kwargs).data)
        self._dict.update(CZMLPositions(**kwargs).data)

