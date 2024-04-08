# uncompyle6 version 3.9.1
# Python bytecode version base 3.7.0 (3394)
# Decompiled from: Python 3.12.2 (main, Feb  6 2024, 20:19:44) [Clang 15.0.0 (clang-1500.1.0.2.5)]
# Embedded file name: output/Live/mac_universal_64_static/Release/python-bundle/MIDI Remote Scripts/_MxDCore/ControlSurfaceWrapper.py
# Compiled at: 2024-03-09 01:30:22
# Size of source mod 2**32: 12811 bytes
from __future__ import absolute_import, print_function, unicode_literals
import weakref, Live
from ableton.v2.base import EventObject, old_hasattr
from ableton.v2.control_surface import MessageScheduler, defaults

def is_real_control_surface(lom_object):
    return is_local_control_surface(lom_object) or isinstance(lom_object, Live.Application.ControlSurfaceProxy)


def is_local_control_surface(lom_object):
    import _Framework.ControlSurface as ControlSurface
    from ableton.v2.control_surface import SimpleControlSurface as ControlSurface2
    from ableton.v3.control_surface import ControlSurface as ControlSurface3
    return isinstance(lom_object, (ControlSurface, ControlSurface2, ControlSurface3))


def wrap(control_surface):
    if is_local_control_surface(control_surface):
        return LocalControlSurfaceWrapper(control_surface=control_surface)
    if isinstance(control_surface, Live.Application.ControlSurfaceProxy):
        return RemoteControlSurfaceWrapper(proxy=control_surface)


class WrapperRegistry(object):

    def __init__(self, *a, **k):
        (super(WrapperRegistry, self).__init__)(*a, **k)
        self._wrapper_registry = {}

    def wrap(self, obj):
        if is_real_control_surface(obj):
            try:
                return self._wrapper_registry[obj]
            except KeyError:
                wrapped = wrap(obj)
                self._wrapper_registry[obj] = wrapped
                try:
                    obj.add_disconnect_listener(self._WrapperRegistry__on_control_surface_disconnected)
                except AttributeError:
                    pass

                return wrapped

        return obj

    def clear(self):
        for wrapper in self._wrapper_registry.values():
            wrapper.disconnect()

        self._wrapper_registry = {}

    def __on_control_surface_disconnected(self, unwrapped_cs):
        try:
            unwrapped_cs.remove_disconnect_listener(self._WrapperRegistry__on_control_surface_disconnected)
            self._wrapper_registry[unwrapped_cs].disconnect()
            del self._wrapper_registry[unwrapped_cs]
        except KeyError:
            pass


class ControlSurfaceWrapper(object):

    def disconnect(self):
        raise NotImplementedError

    @property
    def canonical_parent(self):
        pass

    @property
    def type_name(self):
        raise NotImplementedError

    @property
    def control_names(self):
        raise NotImplementedError

    def has_control(self, control):
        raise NotImplementedError

    def get_control_by_name(self, control_name):
        raise NotImplementedError

    def grab_control(self, control):
        raise NotImplementedError

    def release_control(self, control):
        raise NotImplementedError


class LocalControlSurfaceWrapper(ControlSurfaceWrapper):

    def __init__(self, control_surface=None, *a, **k):
        (super(ControlSurfaceWrapper, self).__init__)(*a, **k)
        self._control_surface = control_surface
        self._grabbed_controls = []

    @property
    def __doc__(self):
        return self._control_surface.__doc__

    def set_control_element(self, control, grabbed):
        if old_hasattr(control, "release_parameter"):
            control.release_parameter()
        control.reset()

    def disconnect(self):
        for control in self._grabbed_controls:
            with self._control_surface.component_guard():
                control.resource.release(self)

    def __getattr__(self, name):
        return getattr(self._control_surface, name)

    def __setattr__(self, name, value):
        if name not in ('_control_surface', '_grabbed_controls'):
            setattr(self._control_surface, name, value)
        else:
            super(ControlSurfaceWrapper, self).__setattr__(name, value)

    def __eq__(self, other):
        return self._control_surface == other

    def __hash__(self):
        return hash(self._control_surface)

    @property
    def type_name(self):
        return self._control_surface.__class__.__name__

    @property
    def control_names(self):
        return [control.name for control in self._control_surface.controls if old_hasattr(control, "name") if control.name]

    def has_control(self, control):
        return control in self._control_surface.controls

    def get_control_by_name(self, control_name):
        for control in self._control_surface.controls:
            if old_hasattr(control, "name") and control.name == control_name:
                return control

    def grab_control(self, control):
        if control not in self._grabbed_controls:
            with self._control_surface.component_guard():
                priority = self._control_surface.mxd_grab_control_priority() if old_hasattr(self._control_surface, "mxd_grab_control_priority") else 1
                control.resource.grab(self, priority=priority)
                if old_hasattr(control, "suppress_script_forwarding"):
                    control.suppress_script_forwarding = False
                self._grabbed_controls.append(control)

    def release_control(self, control):
        if control in self._grabbed_controls:
            with self._control_surface.component_guard():
                self._grabbed_controls.remove(control)
                control.resource.release(self)


class ControlProxyBase(EventObject):
    __events__ = ('value', )


class ControlProxy(ControlProxyBase):

    def __init__(self, name='', id=None, proxy=None, parent=None, *a, **k):
        (super(ControlProxy, self).__init__)(*a, **k)
        self._name = name
        self._id = id
        self._proxy = proxy
        self._parent = parent

    @property
    def canonical_parent(self):
        return self._parent

    @property
    def name(self):
        return self._name

    @property
    def id(self):
        return self._id

    def send_value(self, *a):
        self._proxy.send_value((self._id, a))

    def receive_value(self, value):
        (self.notify_value)(*value)

    def add_value_listener(self, listener):
        original_count = self.value_listener_count()
        super().add_value_listener(listener)
        if original_count == 0:
            if self.value_listener_count() > 0:
                self._proxy.subscribe_to_control(self._id)

    def remove_value_listener(self, listener):
        original_count = self.value_listener_count()
        super().remove_value_listener(listener)
        if self._proxy:
            if original_count > 0:
                if self.value_listener_count() == 0:
                    self._proxy.unsubscribe_from_control(self._id)


class RemoteControlSurfaceWrapper(ControlSurfaceWrapper):

    def __init__Parse error at or near `LOAD_DICTCOMP' instruction at offset 28

    @property
    def timer_instance(self):
        return self._timer._timer_instance

    def disconnect(self):
        self._timer.disconnect()
        self._proxy.enable_receive_midi(False)
        self._proxy.remove_control_values_arrived_listener(self._RemoteControlSurfaceWrapper__on_control_values_arrived)
        self._proxy.remove_midi_received_listener(self._RemoteControlSurfaceWrapper__on_midi_received)

    def __eq__(self, other):
        return self._proxy == other

    def __hash__(self):
        return hash(self._proxy)

    @property
    def type_name(self):
        return self._proxy.type_name

    @property
    def control_names(self):
        return tuple((c.name for c in self._proxy.control_descriptions))

    def _on_mxd_midi_scheduler_state_changed(self, new_state):
        self._proxy.enable_receive_midi(new_state in ('grabbed', 'wait', 'grabbed_wait'))

    def __on_control_values_arrived(self):
        for control_id, value in self._proxy.fetch_received_values():
            try:
                self._control_proxies_by_id[control_id].receive_value(value)
            except KeyError:
                pass

    def __on_midi_received(self):
        for message in self._proxy.fetch_received_midi_messages():
            self.mxd_midi_scheduler.handle_message(message)

    def has_control(self, control):
        return control in self._control_proxies.values()

    def get_control_by_name(self, control_name):
        return self._control_proxies.get(control_name)

    def grab_control(self, control):
        if control.id in self._control_proxies_by_id:
            self._proxy.grab_control(control.id)

    def release_control(self, control):
        if control.id in self._control_proxies_by_id:
            self._proxy.release_control(control.id)