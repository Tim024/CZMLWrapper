from .CZMLElement import CZMLElement
from .CZMLShow import CZMLShow


class CZMLBillboard(CZMLElement):
    name = "billboard"

    def __init__(self):
        super(CZMLBillboard, self).__init__()
        self.parameters += [
            {"key": "image",
             "type": "str",
             "help": "Base 64 string of the image (PNG format). By default outputs a little satellite."}
        ]

    def _build_dict(self, **kwargs):
        image = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAADJSURBVDhPnZHRDcMgEEMZjVEYpaNklIzSEfLfD4qNnXAJSFWfhO7w2Zc0Tf9QG2rXrEzSUeZLOGm47WoH95x3Hl3jEgilvDgsOQUTqsNl68ezEwn1vae6lceSEEYvvWNT/Rxc4CXQNGadho1NXoJ+9iaqc2xi2xbt23PJCDIB6TQjOC6Bho/sDy3fBQT8PrVhibU7yBFcEPaRxOoeTwbwByCOYf9VGp1BYI1BA+EeHhmfzKbBoJEQwn1yzUZtyspIQUha85MpkNIXB7GizqDEECsAAAAASUVORK5CYII="
        if "image" in kwargs.keys():
            image = kwargs["image"]
        self._dict = {
            "eyeOffset": {
                "cartesian": [
                    0, 0, 0
                ]
            },
            "image": f"data:image/png;base64,{image}",
            "pixelOffset": {
                "cartesian2": [
                    0, 0
                ]
            },
            "scale": 1.0,
            "horizontalOrigin": "CENTER",
            "verticalOrigin": "CENTER",
            "show": True
        }
