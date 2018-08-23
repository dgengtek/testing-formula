def test_testing():
    assert True

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_ssh_is_installed(host):
    sshd = host.package("openssh-server")
    assert sshd.is_installed
    #assert sshd.version.startswith("1.2")


def test_sshd_running_and_enabled(host):
    sshd = host.service("sshd")
    assert sshd.is_running
    assert sshd.is_enabled
