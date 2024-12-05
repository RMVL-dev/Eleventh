import inspect
from optparse import OptionParser


def introspection_info(obj):
    inspection_result = {}
    obj_type = type(obj)
    try:
        obj_module = obj.__module__
    except AttributeError:
        obj_module = inspect.getmodule(obj)
    obj_attrs = '...'
    if '__dict__' in dir(obj):
        obj_attrs = obj.__dict__
    obj_methods = dir(obj)
    inspection_result["type"] = obj_type
    inspection_result["attributes"] = obj_attrs
    inspection_result["methods"] = obj_methods
    inspection_result["module"] = obj_module
    return inspection_result


class SomeClass:

    def __init__(self):
        self.first = 1
        self.second = 2


object = SomeClass()

print(introspection_info(42))
