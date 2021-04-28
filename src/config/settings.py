from typing import Dict
from pathlib import PurePath

from ._utils import yaml_to_dict

from pydantic import BaseSettings


class Settings(BaseSettings):
    """project settings"""
    # important directory path
    project_dir: PurePath = PurePath(__file__).parent.parent.parent
    source_dir: PurePath = project_dir / "src"
    config_dir: PurePath = source_dir / "config"
    classification_dir: PurePath = source_dir / "classification"
    detection_dir: PurePath = source_dir / "detection"
    logger_dir: PurePath = source_dir / "logger"

    # configs
    detection_config: Dict = yaml_to_dict(config_dir / "detection.yml")
    classification_config: Dict = yaml_to_dict(config_dir / "classification.yml")
    logger_config: Dict = yaml_to_dict(config_dir / "logger.yml")

    # seed
    seed: int = 666
    # deterministic will drop performance
    use_deterministic: bool = False

    @staticmethod
    def set_deterministic(seed: int) -> None:
        import os
        import random
        import torch
        import numpy as np

        # https://pytorch.org/docs/stable/notes/randomness.html
        def set_all_seeds() -> None:
            os.environ["PL_GLOBAL_SEED"] = str(seed)
            random.seed(seed)
            np.random.seed(seed)
            torch.manual_seed(seed)
            torch.cuda.manual_seed_all(seed)

        os.environ["PL_SEED_WORKERS"] = "1"
        os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":16:8"
        torch.backends.cudnn.benchmark = False
        torch.use_deterministic_algorithms(True)
        set_all_seeds()


settings = Settings()
if settings.use_deterministic:
    settings.set_deterministic(settings.seed)
