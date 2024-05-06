# window.py
#
# Copyright 2024 Unknown
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Gtk
from .StateManager import StateManager
from .connecteddevice import ConnectedDevice
from .nodevice import NoDevice

@Gtk.Template(resource_path='/com/xronlinux/BreezyDesktop/window.ui')
class BreezydesktopWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'BreezydesktopWindow'

    connected_device = Gtk.Template.Child()
    no_device = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.init_template()

        state_manager = StateManager.get_instance()
        state_manager.connect('device_update', self._handle_device_update)

        self._handle_device_update(state_manager, StateManager.device_name(state_manager.state))

    def _handle_device_update(self, state_manager, connected_device_name):
        if connected_device_name:
            self.connected_device.set_visible(True)
            self.no_device.set_visible(False)
            self.connected_device.set_device_name(connected_device_name)
        else:
            self.connected_device.set_visible(False)
            self.no_device.set_visible(True)
            