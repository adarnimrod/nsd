def test_nsd(Command, Service, Ansible):
    assert Command('nsd -v').rc == 0
    assert Service('nsd').is_running
    if Ansible('setup')['ansible_facts']['ansible_os_family'] == 'OpenBSD':
        assert Command('nsd-checkconf /var/nsd/etc/nsd.conf')
    elif Ansible('setup')['ansible_facts']['ansible_os_family'] == 'Debian':
        assert Command('nsd-checkconf /etc/nsd/nsd.conf')
        assert Service('nsd').is_enabled
    assert '127.0.0.2' in Command('dig @127.0.0.1 a.testzone').stdout
