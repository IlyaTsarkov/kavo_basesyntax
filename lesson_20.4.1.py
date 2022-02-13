def decorator_func_with_arg(tag='h1'):
    def decorator_func(func):
        def wrapper(ex_str):
            res = func(f"<{tag}> {ex_str} </{tag}>")
            return res

        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__

        return wrapper

    return decorator_func


@decorator_func_with_arg(tag='p')
def main_def(ex):
    """Обертывает строку в html тэг"""
    return ex


print(main_def.__name__)
print(main_def.__doc__)



