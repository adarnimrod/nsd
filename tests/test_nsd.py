from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


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


def test_nsd_config(Command, File, SystemInfo):
    if SystemInfo.type == 'openbsd':
        assert Command('nsd-checkconf /var/nsd/etc/nsd.conf')
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert Command('nsd-checkconf /etc/nsd/nsd.conf')


def test_nsd_directories(File, SystemInfo, Sudo):
    if SystemInfo.type == 'openbsd':
        with Sudo():
            assert File('/var/nsd/zones').is_directory
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert File('/etc/nsd').is_directory


def test_nsd_socket(Socket):
    assert Socket('udp://0.0.0.0:53').is_listening


def test_nsd_test_zone(Command):
    assert '127.0.0.2' in Command('dig @127.0.0.1 a.testzone').stdout


def test_nsd_alias(File, SystemInfo, User):
    if SystemInfo.type == 'openbsd':
        assert User('_nsd').exists
        assert File('/etc/mail/aliases').contains('_nsd: root')
    elif SystemInfo.type == 'linux' and SystemInfo.distribution in ['debian',
                                                                    'ubuntu']:
        assert User('nsd').exists
        assert File('/etc/aliases').contains('nsd: root')
