def enforce_non_empty_list(func):
    
    def wrapper(input_list, *args, **kwargs):
        if not isinstance(input_list, list):
            raise TypeError("Input must be a list.")
        if len(input_list) < 1:
            raise ValueError("List must contain at least one element.")
        return func(input_list, *args, **kwargs)

    return wrapper
