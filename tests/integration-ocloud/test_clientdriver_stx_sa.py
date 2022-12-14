# Copyright (C) 2021 Wind River Systems, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# import sys
# import logging
import pytest

from o2common.config import config
from o2ims.adapter.clients.ocloud_sa_client import StxSaClientImp
from cgtsclient.client import get_client


@pytest.fixture
def real_stx_aio_client():
    os_client_args = config.get_stx_access_info()
    config_client = get_client(**os_client_args)
    yield config_client

# pytestmark = pytest.mark.usefixtures("mappers")


def test_get_instanceinfo(real_stx_aio_client):
    # logger = logging.getLogger(__name__)
    stxclientimp = StxSaClientImp(real_stx_aio_client)
    assert stxclientimp is not None
    systeminfo = stxclientimp.getInstanceInfo()
    assert systeminfo is not None
    assert systeminfo.id is not None
    assert systeminfo.name is not None
    assert systeminfo.content is not None


def test_get_pserverlist(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hosts = stxSaClientImp.getPserverList()
    assert hosts is not None
    assert len(hosts) > 0


def test_get_pserver(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hosts = stxSaClientImp.getPserverList()
    assert hosts is not None
    assert len(hosts) > 0
    host1 = hosts[0]
    host2 = stxSaClientImp.getPserver(host1.id)
    assert host1 != host2
    assert host1.id == host2.id


def test_get_k8s_list(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    k8slist = stxSaClientImp.getK8sList()
    assert k8slist is not None
    assert len(k8slist) > 0
    k8s1 = k8slist[0]
    k8s2 = stxSaClientImp.getK8sDetail(k8s1.name)
    assert k8s1 != k8s2
    assert k8s1.name == k8s2.name
    assert k8s1.id == k8s2.id


def test_get_cpu_list(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hostlist = stxSaClientImp.getPserverList()
    assert len(hostlist) > 0

    cpulist = stxSaClientImp.getCpuList(hostid=hostlist[0].id)
    assert len(cpulist) > 0
    cpu1 = cpulist[0]
    cpu2 = stxSaClientImp.getCpu(cpu1.id)
    assert cpu1 != cpu2
    assert cpu1.id == cpu2.id


def test_get_mem_list(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hostlist = stxSaClientImp.getPserverList()
    assert len(hostlist) > 0

    memlist = stxSaClientImp.getMemList(hostid=hostlist[0].id)
    assert len(memlist) > 0
    mem1 = memlist[0]
    mem2 = stxSaClientImp.getMem(mem1.id)
    assert mem1 != mem2
    assert mem1.id == mem2.id


def test_get_eth_list(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hostlist = stxSaClientImp.getPserverList()
    assert len(hostlist) > 0

    ethlist = stxSaClientImp.getEthernetList(hostid=hostlist[0].id)
    assert len(ethlist) > 0
    eth1 = ethlist[0]
    eth2 = stxSaClientImp.getEthernet(eth1.id)
    assert eth1 != eth2
    assert eth1.id == eth2.id


def test_get_if_list(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hostlist = stxSaClientImp.getPserverList()
    assert len(hostlist) > 0

    iflist = stxSaClientImp.getIfList(hostid=hostlist[0].id)
    assert len(iflist) > 0
    if1 = iflist[0]
    if2 = stxSaClientImp.getIf(if1.id)
    assert if1 != if2
    assert if1.id == if2.id


def test_get_if_port_list(real_stx_aio_client):
    stxSaClientImp = StxSaClientImp(real_stx_aio_client)
    assert stxSaClientImp is not None
    hostlist = stxSaClientImp.getPserverList()
    assert len(hostlist) > 0

    iflist = stxSaClientImp.getIfList(hostid=hostlist[0].id)
    assert len(iflist) > 0

    portlist = stxSaClientImp.getPortList(interfaceid=iflist[0].id)
    assert len(portlist) > 0
    port1 = portlist[0]
    port2 = stxSaClientImp.getPort(port1.id)
    assert port1 != port2
    assert port1.id == port2.id
