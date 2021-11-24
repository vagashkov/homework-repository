"""
Написать декоратор который позволит сохранять информацию из
исходной функции (__name__ and __doc__), а так же сохранит саму
исходную функцию в атрибуте __original_func
print_result изменять нельзя, за исключением добавления вашего
декоратора на строку отведенную под него - замените комментарий
До применения вашего декоратор будет вызываться AttributeError
при custom_sum.__original_func
Это корректное поведение
После применения там должна быть исходная функция
Ожидаемый результат:
 'This function can sum any objects which have __add___'
print(custom_sum.__doc__)  #
print(custom_sum.__name__)  # 'custom_sum'
print(custom_sum.__original_func)  # <function custom_sum at <some_id>>
"""

import functools


def my_update_wrapper(wrapper, wrapped):
    """ Custom wrapper that can store information
    about wrapped object"""
    wrapper.__name__ = wrapped.__name__
    wrapper.__doc__ = wrapped.__doc__
    wrapper.__wrapped__ = wrapped
    wrapper.__original_func = wrapped
    return wrapper


def my_wraps(wrapped):
    return functools.partial(my_update_wrapper, wrapped=wrapped)


def print_result(func):
    """ Here we apply our custom wrapper """
    @my_wraps(func)
    def wrapper(*args, **kwargs):
        """Function-wrapper which print result of an original function"""
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)
