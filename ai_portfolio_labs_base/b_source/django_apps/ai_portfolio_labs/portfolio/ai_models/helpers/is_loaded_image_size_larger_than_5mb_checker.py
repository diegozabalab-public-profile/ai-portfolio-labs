import os
from pathlib import Path


# TODO: increase limit when running on a better server
def is_loaded_image_size_larger_than_5mb(
        input_image_path: Path,
        limit_size_in_cardinal_number: int = 5) \
        -> bool:
    if os.path.getsize(input_image_path) > (limit_size_in_cardinal_number * 1024 * 1024):
        return \
            True

    return \
        False
