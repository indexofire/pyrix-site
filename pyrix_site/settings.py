# -*- coding: utf-8 -*-
import os
import socket
from django.utils import importlib


PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

HOSTMAP = {
    'local': 'mark-desktop',
    'server': 'hzcdclabs.org',
}
CURRENT_HOST = socket.gethostname()
DISPATCHER = []

def update_current_settings(setting_file):
    """
    Given a filename, this function will insert all variables and
    functions in ALL_CAPS into the global scope.
    """
    setting = importlib.import_module(setting_file)
    for k, v in setting.__dict__.items():
        if k.upper() == k:
            globals().update({k:v})

update_current_settings('setting.settings_base')

for k, v in HOSTMAP.items():
    if CURRENT_HOST == v:
        DISPATCHER.append(k)

for s in DISPATCHER:
    try:
        update_current_settings('setting.settings_%s' % s)
    except ImportError:
        print "Error importing %s" % s
