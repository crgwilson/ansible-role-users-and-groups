import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('group, exists', [
    ('sudo', True),
    ('testaddgroup', True),
    ('testdeletegroup', False)
])
def test_default_user_groups(host, group, exists):
    g = host.group(group)
    assert g.exists == exists


@pytest.mark.parametrize('user, groups, shell', [
    ('testbashuser', ['testbashuser', 'sudo', 'testaddgroup'], '/bin/bash'),
    ('testcshuser', None, '/bin/csh')
])
def test_default_users(host, user, groups, shell):
    u = host.user(user)
    assert u.group == user
    assert u.shell == shell
    assert u.home == '/home/' + user
    if groups:
        assert u.groups == groups

    d = host.file('/home/' + user + '/.ssh')
    assert d.is_directory
    assert d.user == user
    assert d.group == user
    assert d.mode == 0o700


def test_default_ssh_key(host):
    f = host.file('/home/testbashuser/.ssh/test')
    assert f.is_file
    assert f.user == 'testbashuser'
    assert f.group == 'testbashuser'
    assert f.mode == 0o600


def test_default_authorized_keys(host):
    d = host.file('/home/testbashuser/.ssh/authorized_keys')
    assert d.is_file
    assert d.user == 'testbashuser'
    assert d.group == 'testbashuser'
    assert d.mode == 0o600
