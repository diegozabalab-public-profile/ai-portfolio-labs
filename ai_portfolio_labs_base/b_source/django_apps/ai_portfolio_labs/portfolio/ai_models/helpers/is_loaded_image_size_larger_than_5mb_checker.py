import os
from pathlib import Path


# TODO: increase limit when running on a better server
def is_loaded_image_size_larger_than_5mb(
        input_image_path: Path) \
        -> bool:
    if os.path.getsize(input_image_path) > 5 * 1024 * 1024:
        return \
            False

    return \
        True
