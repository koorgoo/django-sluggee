# -*- coding: utf-8 -*-
from functools import wraps
from django.utils.text import slugify as _slugify
from .translit import RU_EN
from .six import u


def slugify(value):
    new_value = u('')
    for c in u(value).lower():
        new_value += RU_EN.get(c, c)
    return _slugify(new_value)
