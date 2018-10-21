#!/usr/bin/env python
# -*- coding: utf-8 -*-

import configparser
config = configparser.RawConfigParser()
config.read('config.cfg')

def conf_to_dict(section):
    try:
        dictory = {}
        for i in config.items(section):
                if len(i) == 2:
                    dictory[i[0]] = i[1]
        return dictory
    except configparser.MissingSectionHeaderError:
        return True
    except configparser.NoSectionError:
        return False

def list_section():
    return config.sections()

DEFAULT = config.defaults()
# print(type(int(DEFAULT['wait_time'])))
