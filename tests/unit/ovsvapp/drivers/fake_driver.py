# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

from neutron.plugins.ovsvapp.drivers import driver as network_driver
from neutron.plugins.ovsvapp.drivers import driver \
    as network_driver_callback


class FakeInvalidDriver(object):
    pass


class FakeNetworkDriver(network_driver.NetworkDriver):
    pass


class MockNetworkDriver(network_driver.NetworkDriver):

    def __init__(self):
        super(MockNetworkDriver, self).__init__()
        self.methods = {}

    def create_network(self, network, virtual_switch):
        kwargs = {}
        kwargs["network"] = network
        kwargs["virtual_switch"] = virtual_switch
        self.methods["create_network"] = kwargs

    def create_port(self, network, port, virtual_nic):
        kwargs = {}
        kwargs["network"] = network
        kwargs["port"] = port
        kwargs["virtual_nic"] = virtual_nic
        self.methods["create_port"] = kwargs

    def post_create_port(self, port):
        kwargs = {}
        kwargs["port"] = port
        self.methods["post_create_port"] = kwargs

    def update_port(self, network=None, port=None, virtual_nic=None):
        kwargs = {}
        kwargs["network"] = network
        kwargs["port"] = port
        kwargs["virtual_nic"] = virtual_nic
        self.methods["update_port"] = kwargs
        return True

    def delete_network(self, network, virtual_switch=None):
        kwargs = {}
        kwargs["network"] = network
        kwargs["virtual_switch"] = virtual_switch
        self.methods["delete_network"] = kwargs

    def post_delete_vm(self, vm):
        kwargs = {}
        kwargs["vm"] = vm
        self.methods["post_delete_vm"] = kwargs

    def monitor_events(self):
        self.methods["monitor_events"] = {}

    def stop(self):
        self.methods["stop"] = {}

    def reset(self):
        self.methods = {}


class MockCallback(network_driver_callback.NetworkDriverCallback):

    def __init__(self):
        self.events = []

    def process_event(self, event):
        self.events.append(event)

    def notify_driver_ready(self):
        self.events.append("notify_driver_ready")
