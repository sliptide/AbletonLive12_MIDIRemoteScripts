# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/Launchkey_Mini_MK3/__init__.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 859 bytes
from __future__ import absolute_import, print_function, unicode_literals
from ableton.v2.control_surface.capabilities import CONTROLLER_ID_KEY, NOTES_CC, PORTS_KEY, REMOTE, SCRIPT, SYNC, controller_id, inport, outport
from .launchkey_mini_mk3 import Launchkey_Mini_MK3

def get_capabilities():
    return {CONTROLLER_ID_KEY: (controller_id(vendor_id=4661,
                          product_ids=[258],
                          model_name=["Launchkey Mini MK3"])), 
     
     PORTS_KEY: [
                 inport(props=[NOTES_CC, REMOTE]),
                 inport(props=[NOTES_CC, SCRIPT]),
                 outport(props=[SYNC, REMOTE]),
                 outport(props=[NOTES_CC, SCRIPT])]}


def create_instance(c_instance):
    return Launchkey_Mini_MK3(c_instance=c_instance)
