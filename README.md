# ansible-role-ufw #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-ufw/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-ufw/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-ufw/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-ufw/actions/workflows/codeql-analysis.yml)

An Ansible role for installing [Uncomplicated
Firewall](https://wiki.ubuntu.com/UncomplicatedFirewall?action=show&redirect=UbuntuFirewall)
(UFW).

## Requirements ##

None.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| ufw_logging | The logging state for ufw.  See options [here](https://docs.ansible.com/ansible/latest/modules/ufw_module.html#parameter-logging).  Quotes are needed around this value because the words `on` and `off` denote boolean values in Ansible. | `"on"` | No |
| ufw_state | The state of ufw.  See options [here](https://docs.ansible.com/ansible/latest/modules/ufw_module.html#parameter-state). | `enabled` | No |

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install ufw
      ansible.builtin.include_role:
        name: ufw
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
