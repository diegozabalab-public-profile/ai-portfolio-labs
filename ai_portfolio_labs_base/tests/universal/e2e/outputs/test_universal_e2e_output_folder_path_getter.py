from pathlib import Path
from ai_portfolio_labs_base.b_source.common.my_folder_as_folder_path_getter import get_my_folder_as_file_system_folder


def get_test_universal_e2e_output_folder_path() \
        -> Path:
    my_folder_path = \
        get_my_folder_as_file_system_folder()
    
    return \
        my_folder_path
