from .utils import check_equal


class CZMLHelper:
    def __init__(self, name, prefix, parameters):
        self.name = name
        self.prefix = prefix
        self.parameters = parameters

    def __str__(self):
        output_string = f""
        for p in self.parameters:
            if isinstance(p, CZMLElement):
                output_string += str(p.helper(prefix=self.name))
            else:
                manda = "mandatory" if "mandatory" in p.keys() and p['mandatory'] else "optional"
                pref1 = self.prefix + "_" if self.prefix is not None else ""
                pref2 = self.name + "_" if self.name != "" and p['key'] != self.name else ""
                includes = "" if "include" not in p.keys() else ", includes " + p["include"]
                excludes = "" if "exclude" not in p.keys() else ", excludes " + p["exclude"]
                output_string += f"\n{pref1}{pref2}{p['key']} ({manda}, {p['type']}{includes}{excludes});\t {p['help']}"
        return output_string


class CZMLElement:
    name = ""

    def __init__(self):
        self.parameters = []
        if self.name != "":
            self.parameters += [
                {"key": self.name,
                 "type": "boolean",
                 "help": f"Set {self.name} to True to enable {self.name} definition."}
            ]
        self._dict = {}

    def helper(self, prefix=""):
        prefix = None if prefix == "" else prefix
        return CZMLHelper(self.name, prefix, self.parameters)

    def _build_dict(self, **kwargs):
        raise NotImplementedError

    def _prep_kwargs(self, **kwargs):
        if self.name != "":
            kwargs = {k.replace(self.name + "_", ""): v for k, v in kwargs.items() if k.startswith(self.name)}
        return kwargs

    def dict(self, **kwargs):
        kwargs = self._prep_kwargs(**kwargs)

        if self.name != "":
            if check_equal(kwargs, self.name, True):
                self._build_dict(**kwargs)
        else:
            self._build_dict(**kwargs)

        if self.name != "" and self._dict != {}:
            return {self.name: self._dict}
        return self._dict
