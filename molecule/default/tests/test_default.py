"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["ufw"])
def test_packages(host, pkg):
    """Test that the appropriate packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize("svc", ["ufw"])
def test_services(host, svc):
    """Test that the expected services are enabled."""
    assert host.service(svc).is_enabled


def test_kali_ufw_unit_file(host):
    """Test that the Kali ufw.service unit file was patched correctly."""
    if host.system_info.distribution in [
        "kali",
    ]:
        f = host.file("/usr/lib/systemd/system/ufw.service")
        assert f.exists
        assert f.is_file
        assert not f.contains(r"^Wants=network-pre\.target$")
        assert f.contains(r"^DefaultDependencies=no$")
