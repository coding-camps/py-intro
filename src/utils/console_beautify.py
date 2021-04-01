# -*- coding: utf-8 -*-


from functools import wraps

# 全局变量
__counter_for_segment = 0  # segment 全局计数器
__counter_for_logger = 0  # logger 全局计数器
__sep_clr_purple = '\033[95m'  # 分隔行字体颜色，紫红色
__sep_clr_red = '\033[91m'  # 分割行字体颜色，红色
__sep_clr_end = '\033[0m'  # 字体颜色设置结束符


# 表示函数计数器的类
class __CounterForFunc(object):
    __func_map = dict()

    def __init__(self, func):
        self.__class__.__func_map[func] = 0

    def reset_all_counter(self):
        """ 重置所有函数的计数器 """
        for k in self.__class__.__func_map.keys():
            self.__class__.__func_map[k] = 0

    def increment_counter(self, func):
        """ 函数对应计数器自增"""
        self.__class__.__func_map[func] += 1

    def get_counter(self, func):
        """ 取得函数对应的计数器 """
        return self.__class__.__func_map[func]


# 不带参数的装饰器示例
def log_simple(func):
    """
    装饰器： 美化代码打印。
    格式：#<程序执行总次数> - [<执行函数的名称>]-<该函数执行次数> <输出30个等号（=）>
    """

    __counter_func = __CounterForFunc(func)  # 局部计数器

    def __check_counter():
        global __counter_for_logger  # 函数内部修改全局变量
        # nonlocal __counter_func  # 函数内部修改父级作用域的局部变量, 这里并未修改，因此可以不用
        if __counter_for_logger == 0:  # 如果全局计数器重置，则局部计数器自动重置
            __counter_func.reset_all_counter()
        __counter_func.increment_counter(func)
        __counter_for_logger += 1

    @wraps(func)  # make original '__name__' is still original name
    def wrapper(*args, **kwargs):
        __check_counter()
        line = __sep_clr_purple + '#' + str(__counter_for_logger) \
               + ' - [' + func.__name__ + ']-' + str(__counter_func.get_counter(func)) \
               + ' ' + ('=' * 30) + __sep_clr_end
        print(line)
        r = func(*args, **kwargs)
        print()
        return r

    return wrapper


# 带参数的装饰器示例
def log_advanced(sep: str = '=', n: int = 30):
    """
    装饰器，美化代码打印。

    格式：#<程序执行总次数> - [<执行函数的名称>]-<该函数执行次数> <n个sep组成的字符串>

    :param sep: 分割符号，默认值 '-'
    :param n: 分割符号数量，默认值 30
    """

    def decorator(func):
        __counter_func = __CounterForFunc(func)  # 局部计数器

        def __check_counter():
            global __counter_for_logger
            # nonlocal __counter_func
            if __counter_for_logger == 0:  # 如果全局计数器重置，则局部计数器自动重置
                __counter_func.reset_all_counter()
            __counter_for_logger += 1
            __counter_func.increment_counter(func)

        @wraps(func)
        def wrapper(*args, **kwargs):
            __check_counter()
            line = __sep_clr_purple + '#' + str(__counter_for_logger) \
                   + ' - [' + func.__name__ + ']-' + str(__counter_func.get_counter(func)) \
                   + ' ' + (sep * n) + __sep_clr_end
            print(line)
            r = func(*args, **kwargs)
            print()
            return r

        return wrapper

    return decorator


# 正常函数，不是装饰器
def new_segment(msg: str = None, sep: str = '=', sep_cnt: int = 60) -> None:
    """
    重置log计数器, 并打印

    打印格式：[##]<序号> [提示信息] < `sep_cnt` 个符号 `sep` >

    :param msg: 提示信息
    :param sep: 分隔符号
    :param sep_cnt: 分隔符号数量
    :return: 无
    """
    global __counter_for_logger
    __counter_for_logger = 0
    global __counter_for_segment
    __counter_for_segment += 1
    line = __sep_clr_red + '##' + str(__counter_for_segment)
    if msg is not None:
        line += ' [' + msg + ']'
    line += ' ' + sep * sep_cnt
    print(line + __sep_clr_end)
