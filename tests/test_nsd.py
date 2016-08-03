def test_nsd(Command, Sudo):
    with Sudo():
        assert Command('nsd -v').rc == 0


def test_nsd_service(Service, Sudo):
    service = Service('nsd')
    with Sudo():
        assert service.is_running
        try:
            assert service.is_enabled
        except NotImplementedError:
            pass


def test_nsd_config(Command, File, Ansible):
    if Ansible('setup')['ansible_facts']['ansible_os_family'] == 'OpenBSD':
        assert Command('nsd-checkconf /var/nsd/etc/nsd.conf')
    elif Ansible('setup')['ansible_facts']['ansible_os_family'] == 'Debian':
        assert Command('nsd-checkconf /etc/nsd/nsd.conf')


def test_nsd_directories(File, Ansible, Sudo):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'OpenBSD':
        with Sudo():
            assert File('/var/nsd/etc/nsd.conf.d').is_directory
            assert File('/var/nsd/zones').is_directory
    elif ansible_os_family == 'Debian':
        assert File('/etc/nsd/nsd.conf.d').is_directory
        assert File('/etc/nsd').is_directory


def test_nsd_socket(Socket):
    assert Socket('udp://0.0.0.0:53').is_listening


def test_nsd_test_zone(Command):
    assert '127.0.0.2' in Command('dig @127.0.0.1 a.testzone').stdout


def test_nsd_alias(File, Ansible, User):
    ansible_os_family = Ansible('setup')['ansible_facts']['ansible_os_family']
    if ansible_os_family == 'Debian':
        assert User('nsd').exists
        assert File('/etc/aliases').contains('nsd: root')
    elif ansible_os_family == 'OpenBSD':
        assert User('_nsd').exists
        assert File('/etc/mail/aliases').contains('_nsd: root')
