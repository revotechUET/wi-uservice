def type_enforce(type, value):
    if type == int or type == float or type == str:
        return type(value)
    else:
        return value

class BaseValidator(object):
    # def __init__(self, **kwargs):
    #     self.props = None
    #     assert True, "Do not new a base and abstract class directly"        

    def doInit(self, **kwargs):
        assert self.props is not None, "Empty predefined property list. Predefined properties are not set"
        for prop in self.props:
            if prop["name"] in kwargs:
                setattr(self, 'prop_'+prop["name"], type_enforce(prop["type"], kwargs[prop["name"]]) )

    def __call__(self):
        assert self.props is not None, "Empty predefined property list. Predefined properties are not set"
        return_params = {}
        for prop in self.props:
            prop_name = "prop_"+prop["name"]
            assert hasattr(self, prop_name), "{} is missing".format(prop["name"])
            assert isinstance(type_enforce(prop["type"], getattr(self, prop_name)), prop["type"]),\
                "{prop} must be {prop_type}".format(prop=prop["name"], prop_type=str(prop["type"]))
            return_params[prop["name"]] = getattr(self, prop_name)

        return return_params
