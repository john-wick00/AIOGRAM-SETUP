import os
from typing import Tuple, List

def get_all_modules(dirname: str) -> Tuple[List[str]]:
    modules_path = []
    module_names = []
    for root, _, files in os.walk(dirname):
        for file in files:
            if os.path.splitext(file)[1] == ".py" and file != "__init__.py":
                modules_path.append(os.path.join(root, file))
                module_names.append(file[:-3])

    return module_names, modules_path

ALL_MODULES, MODULES_PATH = get_all_modules(os.path.dirname(__file__))
