# -*- coding: utf-8 -*-
# Python imports
from base64 import b64encode as _base64, b64decode as _unbase64
from six import text_type


# 3rd Party imports

# App imports


def encode_base64(s):
    return _base64(s.encode('utf-8')).decode('utf-8')


def decode_base64(s):
    return _unbase64(s).decode('utf-8')


def object_global_id(obj):
    return encode_base64(':'.join([obj._meta.model_name, text_type(obj.id)]))


def object_from_global_id(s):
    _type, _id = decode_base64(s).split(':', 1)
    return _type, _id
