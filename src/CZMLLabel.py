from .CZMLElement import CZMLElement
from .CZMLShow import CZMLShow


class CZMLLabel(CZMLElement):
    name = "label"

    def __init__(self):
        super(CZMLLabel, self).__init__()
        self.parameters = [
            {"key": "font",
             "type": "str",
             "help": "Font of the label. Default to \"11pt Lucida Console\"."},
            {"key": "text",
             "type": "str",
             "mandatory": True,
             "help": "Text of the label."},
            {"key": "style",
             "type": "str",
             "help": "Style of the label. Can be FILL/FILL_AND_OUTLINE/OUTLINE"},
            {"key": "scale",
             "type": "float",
             "help": "Scale of the label."},
            {"key": "bgShow",
             "type": "boolean",
             "help": "If we show the background. Defaults to False."},
            {"key": "bgrgbaf",
             "type": "list[3]",
             "help": "Background color in RGBAF."},
            {"key": "bgPadding",
             "type": "list[2]",
             "help": "Background padding. Defaults to [7,5]."},
            {"key": "pixelOffset",
             "type": "list[2]",
             "help": "Offset in pixel from position to label."},
            {"key": "eyeOffset",
             "type": "list[3]",
             "help": "See https://github.com/AnalyticalGraphicsInc/czml-writer/wiki/EyeOffset."},
            {"key": "horizontalOrigin",
             "type": "str",
             "help": "Controls horizontal origin of the label relative to the position. Can be CENTER/LEFT/RIGHT"},
            {"key": "verticalOrigin",
             "type": "str",
             "help": "Controls vertical origin of the label relative to the position. Can be BOTTOM/LEFT/TOP/BASELINE"},
            {"key": "fillColor",
             "type": "list[3]",
             "help": "Fill color of the label in rgbaf."},
            {"key": "outlineColor",
             "type": "list[3]",
             "help": "Outline color of the label in rgbaf."},
            {"key": "outlineWidth",
             "type": "float",
             "help": "Outline width in pixels."},
            {"key": "translucencyByDistance",
             "type": "float",
             "help": "How the label's translucency should change based on the label's distance from the camera. This scalar value should range from 0 to 1."},
            {"key": "scaleByDistance",
             "type": "float",
             "help": "How the label's scale should change based on the label's distance from the camera. This scalar value will be multiplied by scale."},
            CZMLShow()
        ]

    def _build_dict(self, **kwargs):
        text = kwargs["text"]
        font = "12pt Lucida Console" if "font" not in kwargs.keys() else kwargs["font"]
        style = "FILL_AND_OUTLINE" if "style" not in kwargs.keys() else kwargs["style"]
        bgShow = False if "bgShow" not in kwargs.keys() else kwargs["bgShow"]
        scale = 1 if "scale" not in kwargs.keys() else kwargs["scale"]
        bgrgbaf = [1,1,0.6,1] if "bgrgbaf" not in kwargs.keys() else kwargs["bgrgbaf"]
        bgPadding = [7,5] if "bgPadding" not in kwargs.keys() else kwargs["bgPadding"]
        pixelOffset = [0,0] if "pixelOffset" not in kwargs.keys() else kwargs["pixelOffset"]
        eyeOffset = [0,0,0] if "eyeOffset" not in kwargs.keys() else kwargs["eyeOffset"]
        horizontalOrigin = "LEFT" if "horizontalOrigin" not in kwargs.keys() else kwargs["horizontalOrigin"]
        verticalOrigin = "CENTER" if "verticalOrigin" not in kwargs.keys() else kwargs["verticalOrigin"]
        fillColor = [1,1,0.9,1] if "fillColor" not in kwargs.keys() else kwargs["fillColor"]
        outlineColor = [0,0,0.1,1]if "outlineColor" not in kwargs.keys() else kwargs["outlineColor"]
        outlineWidth = 1 if "outlineWidth" not in kwargs.keys() else kwargs["outlineWidth"]
        scaleByDistance = 0 if "scaleByDistance" not in kwargs.keys() else kwargs["scaleByDistance"]
        translucencyByDistance = 0 if "translucencyByDistance" not in kwargs.keys() else kwargs["translucencyByDistance"]

        self._dict = {
            "fillColor": {
                "rgbaf": fillColor
            },
            "font": font,
            "horizontalOrigin": horizontalOrigin,
            "outlineColor": {
                "rgbaf": outlineColor
            },
            "outlineWidth": outlineWidth,
            "style": style,
            "text": text,
            "scale": scale,
            "verticalOrigin": verticalOrigin,
            # "scaleByDistance": scaleByDistance, # Not working for now
            # "translucencyByDistance": translucencyByDistance,
            # "pixelOffset": pixelOffset,
            # "eyeOffset": eyeOffset
        }
        self._dict.update(CZMLShow().dict(**kwargs))

