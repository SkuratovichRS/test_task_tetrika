from functools import wraps


def strict(func: callable) -> callable:
    annotations_types = [annotation_type for annotation_type in func.__annotations__.values()]
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> callable:
        if args:
            for i, arg in enumerate(args):
                if not isinstance(arg, annotations_types[i]):
                    raise TypeError("Wrong argument type")
        if kwargs:
            for key, value in kwargs.items():
                if not isinstance(value, func.__annotations__[key]):
                    raise TypeError("Wrong argument type")
        return func(*args, **kwargs)

    return wrapper
