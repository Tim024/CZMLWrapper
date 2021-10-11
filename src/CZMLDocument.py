from .CZMLElement import CZMLElement
from .utils import format_date, format_interval
import json


class CZMLDocument(CZMLElement):

    def __init__(self):
        super(CZMLDocument, self).__init__()
        self.parameters += [
            {"key": "name",
             "type": "str",
             "mandatory": True,
             "help": "Reference name of the satellite."},
            {"key": "interval",
             "mandatory": True,
             "type": "tuple(datetime, datetime)",
             "help": "Interval of availability in datetime."},
            {"key": "packets",
             "mandatory": True,
             "type": "list(CZMLElement)",
             "help": "List of CZML elements."},
        ]

    def _build_dict(self, **kwargs):
        name = kwargs["name"]
        self.export_name = name
        ts, te = kwargs["interval"]
        packets = kwargs["packets"]

        self._dict = [{
            "id": "document",
            "name": name,
            "version": "1.0",
            "clock": {
                "interval": format_interval(ts, te),
                "currentTime": format_date(ts),
                "multiplier": 77,
                "range": "LOOP_STOP",
                "step": "SYSTEM_CLOCK_MULTIPLIER"
            }
        }] + packets

    def export(self, **kwargs):
        return json.dumps(self.dict(**kwargs))