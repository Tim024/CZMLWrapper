from datetime import datetime

from .CZMLElement import CZMLElement
from .utils import format_interval


class CZMLShow(CZMLElement):
    name = "show"

    def __init__(self, **kwargs):
        super(CZMLShow, self).__init__(**kwargs)
        self.parameters += [
            {"key": "intervals",
             "mandatory": True,
             "type": "list[tuple[datetime,datetime]]",
             "help": "List of interval where to show the object."},
        ]

    def _build_dict(self, **kwargs):
        t0 = datetime(1973, 1, 1, 0, 0, 0)
        intervals = []
        for t1, t2 in kwargs["intervals"]:
            intervals.append({
                "interval": format_interval(t0, t1),
                "boolean": False
            })
            intervals.append({
                "interval": format_interval(t1, t2),
                "boolean": True
            })
            t0 = t2
        self._dict = intervals