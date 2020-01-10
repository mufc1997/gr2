import json

from ptsemseg.loader.pascal_voc_loader import pascalVOCLoader


def get_loader(name):
    """
    Get_loader
    
    Params:
        name: the name of logger
    """
    return {
        "pascal": pascalVOCLoader,
    }[name]
