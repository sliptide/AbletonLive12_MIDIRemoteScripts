# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_APC/DeviceBankButtonElement.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 797 bytes
from __future__ import absolute_import, print_function, unicode_literals
import _Framework.ComboElement as ComboElement

class DeviceBankButtonElement(ComboElement):

    def on_nested_control_element_received(self, control):
        super(DeviceBankButtonElement, self).on_nested_control_element_received(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(1)

    def on_nested_control_element_lost(self, control):
        super(DeviceBankButtonElement, self).on_nested_control_element_lost(control)
        if control == self.wrapped_control:
            self.wrapped_control.set_channel(0)
