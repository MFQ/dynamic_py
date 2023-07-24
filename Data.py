from dataclasses import dataclass


@dataclass
class DataClass:
    def __init__(self, **kwargs):
        """
        This function will create a data class right from arbitrary attributes
        :param kwargs:
        """
        for key in kwargs.keys():
            if type(kwargs.get(key)) != dict:
                self.__setattr__(key, kwargs.get(key))
            else:
                self.__setattr__(key, DataClass(**kwargs.get(key)))
    @classmethod
    def from_dict(cls, input_dict: dict):
        """
        :type input_dict: object will be converted into data class will assign all of its attributes dynamically
        """
        _instance = cls()
        for key in input_dict.keys():
            if type(input_dict[key]) != dict:
                cls.__setattr__(_instance, key, input_dict[key])
            else:
                cls.__setattr__(_instance, key, cls.from_dict(input_dict[key]))
        return _instance

    def filter_attributes(self):
        """
        This function will filter out data attributes and return them as list of string
        :return: List[str]
        """
        attrs = []
        for attribute in self.__dir__():
            if "__" not in attribute and \
                    "from_dict" not in attribute and \
                    "to_dict" not in attribute and \
                    "filter_attributes" not in attribute and \
                    "fill_dict" not in attribute:
                attrs.append(attribute)
        return attrs

    def fill_dict(self, result: dict):
        """
        This function will recursively convert data class into Dicts with help of filter_attribute function and
        will return its result
        :param result:
        :return: object
        """
        attrs = self.filter_attributes()

        for attribute in attrs:
            if type(self.__getattribute__(attribute)) != type(self):
                result.setdefault(
                    attribute,
                    self.__getattribute__(attribute)
                )
            else:
                result.setdefault(
                    attribute,
                    self.__getattribute__(attribute).fill_dict({})
                )
        return result

    def to_dict(self):
        """
        This function is a driver function for fill_dict function. Which return a full nested dict for data class
        :return: object
        """
        result = {}
        self.fill_dict(result)
        return result
