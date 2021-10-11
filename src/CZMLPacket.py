from cesium.wrapper2 import format_interval
from .CZML3DModel import CZML3DModel
from .CZMLBillboard import CZMLBillboard
from .CZMLElement import CZMLElement
from .CZMLLabel import CZMLLabel
from .CZMLOrientation import CZMLOrientation
from .CZMLPath import CZMLPath
from .CZMLPoint import CZMLPoint
from .CZMLPolygon import CZMLPolygon
from .CZMLPolyline import CZMLPolyline
from .CZMLPosition import CZMLPosition
from .utils import name_to_id


class CZMLPacket(CZMLElement):
    def __init__(self, **kwargs):
        super(CZMLPacket, self).__init__(**kwargs)
        self.parameters += [
            {"key": "name",
             "type": "str",
             "mandatory": True,
             "help": "Reference name of the satellite."},
            {"key": "availability",
             "mandatory": True,
             "type": "tuple(datetime, datetime)",
             "help": "Interval of availability in datetime."},
            CZMLPolyline(),
            CZMLPath(),
            CZMLPosition(),
            CZML3DModel(),
            CZMLOrientation(),
            CZMLBillboard(),
            CZMLPoint(),
            CZMLLabel(),
            CZMLPolygon(),
        ]

    def _build_dict(self, **kwargs):
        name = str(kwargs["name"])
        idd = name_to_id(name)
        ts, te = kwargs["availability"]

        self._dict = {
            "id": idd,
            "name": name,
            "availability": format_interval(ts, te),
        }
        self._dict.update(CZMLPolyline(**kwargs).data)
        self._dict.update(CZMLPath(**kwargs).data)
        self._dict.update(CZMLPosition(**kwargs).data)
        self._dict.update(CZML3DModel(**kwargs).data)
        self._dict.update(CZMLOrientation(**kwargs).data)
        self._dict.update(CZMLBillboard(**kwargs).data)
        self._dict.update(CZMLPoint(**kwargs).data)
        self._dict.update(CZMLLabel(**kwargs).data)
        self._dict.update(CZMLPolygon(**kwargs).data)
