from .CZMLElement import CZMLElement


class CZMLMaterial(CZMLElement):
    name = "material"

    def __init__(self, **kwargs):
        super(CZMLMaterial, self).__init__(**kwargs)
        self.parameters += [
            {"key": "color_rgbaf",
             "type": "array[3]",
             "help": "Color of the material."}
        ]

    def _build_dict(self, **kwargs):
        if "color_rgbaf" in kwargs.keys():
            material_color_rgbaf = kwargs["color_rgbaf"]
        else:
            material_color_rgbaf = [1, 0, 0, 0.5]
        self._dict = {
            "solidColor": {
                "color": {
                    "rgbaf": material_color_rgbaf,
                }
            }
        }
