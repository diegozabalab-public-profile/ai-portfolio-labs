import inspect
from pathlib import Path


def get_my_folder_as_file_system_folder() \
        -> Path:
    my_current_call_stack = (
        inspect.stack())

    if is_stack_length_less_than_two(current_call_stack=my_current_call_stack):
        raise FileNotFoundError

    my_calling_function_folder_path = (
        __get_my_calling_function_folder_from_stack(
            current_call_stack=my_current_call_stack))

    return (
        my_calling_function_folder_path)


def is_stack_length_less_than_two(
        current_call_stack: list) \
        -> bool:
    current_call_stack_length = (
        len(current_call_stack))

    stack_length_is_less_than_two = (
            current_call_stack_length < 2)

    return (
        stack_length_is_less_than_two)


def __get_my_calling_function_folder_from_stack(
        current_call_stack: list) \
        -> Path:

    calling_frame = (
        current_call_stack)[1]

    caller_function_file_path_string = (
        calling_frame.filename)

    caller_function_file_path = (
        Path(caller_function_file_path_string))

    absolute_path = (
        caller_function_file_path.parent)

    return (
        absolute_path)
