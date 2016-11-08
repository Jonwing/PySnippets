#! /usr/bin/env python
# -*- coding: utf-8 -*-


# 1. 装饰器方法
def singleton(class_):
    '''
    优点： 方便实用
    缺点： 实际上把MyClass变成了函数，导其类方法、静态方法不能访问；
          另外，它并不能保证单例，对于a=MyClass(),b=tpye(a)()就绕过了装饰器的实例检查，从而破坏了单例。
    '''
    instances = {}

    def instantiate(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return instantiate


@singleton
class MyClass0(object):
    pass


# 2. 基类
class Singleton0(object):
    '''
    优点： 不会有上面绕过的问题
    缺点： 在子类中 __new__可能被覆写， 也是毁了……
    '''
    instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls.instance, cls):
            cls.instance = object.__new__(cls, *args, **kwargs)
        return cls.instance


class MyClass1(Singleton0):
    pass


# 3. 元类
class Singleton1(type):
    '''
    不会被以此为元类的类改写，但需要注意多继承的时候，
    要确保把使用Singleton1作为元类的类放在最左边（MRO第一位）
    '''
    _instance = {}

    def __call__(cls, *args, **kwargs):
        meta = cls.__class__
        if cls not in meta._instance:
            meta._instance[cls] = super(Singleton1, cls).__call__(*args, **kwargs)
        return meta._instance[cls]


class MyClass2(object):
    __metaclass__ = Singleton1
