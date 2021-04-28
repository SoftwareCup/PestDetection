from typing import Dict
from pathlib import PurePath
import yaml


def yaml_to_dict(yaml_path: PurePath) -> Dict:
    """load from yaml file and return dict

    Args:
        yaml_path (PurePath): path of yaml file

    Returns:
        Dict: dict of yaml file
    """
    return yaml.load(open(yaml_path, 'r', encoding="utf8"))
