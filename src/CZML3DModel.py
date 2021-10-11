from .CZMLShow import CZMLShow
from .CZMLElement import CZMLElement


class CZML3DModel(CZMLElement):
    name = "model"

    def __init__(self):
        super(CZML3DModel, self).__init__()
        self.parameters += [
            {"key": "gltf",
             "type": "str",
             "mandatory": True,
             "help": "URL of the GLTF file."},
            {"key": "scale",
             "type": "float",
             "help": "Scale of the model."},
            {"key": "minimumPixelSize",
             "type": "int",
             "help": "Minimum size of the model (depending on the zoom)."},
            CZMLShow(),
        ]

    def _build_dict(self, **kwargs):
        gltf_url = kwargs["gltf"]
        scale = 1 if "scale" not in kwargs.keys() else kwargs["scale"]
        minimumPixelSize = 50 if "minimumPixelSize" not in kwargs.keys() else kwargs["minimumPixelSize"]

        self._dict = {
            "gltf": gltf_url,
            "scale": scale,
            "minimumPixelSize": minimumPixelSize,
        }
        self._dict.update(CZMLShow().dict(**kwargs))
