import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_docker_is_installed(host):
    docker = host.package("docker-ce")
    assert docker.is_installed
    assert '19.03.5' in docker.version


def test_daemon_file(host):
    f = host.file('/etc/docker/daemon.json')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_metrics_available(host):
    status_code = host.run("curl -LI http://127.0.0.1:9100/metrics -o /dev/null -w '%{http_code}\n' -s")  # noqa

    assert status_code.stdout == '200\n'
