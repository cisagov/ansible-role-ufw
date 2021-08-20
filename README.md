# ansible-role-ufw #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-ufw/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-ufw/actions)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/cisagov/ansible-role-ufw.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-ufw/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/cisagov/ansible-role-ufw.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/cisagov/ansible-role-ufw/context:python)

An Ansible role for installing [Uncomplicated
Firewall](https://wiki.ubuntu.com/UncomplicatedFirewall?action=show&redirect=UbuntuFirewall)
(UFW).

## Requirements ##

None.

## Role Variables ##

- `logging` - The logging state for ufw.  See options
  [here](https://docs.ansible.com/ansible/latest/modules/ufw_module.html#parameter-logging).
- `state` - The state of ufw.  See options
  [here](https://docs.ansible.com/ansible/latest/modules/ufw_module.html#parameter-state).

<!--
| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| optional_variable | Describe its purpose. | `default_value` | No |
| required_variable | Describe its purpose. | n/a | Yes |
-->

## Dependencies ##

None.

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: yes
  become_method: sudo
  roles:
    - ufw
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

Shane Frasier - <jeremy.frasier@trio.dhs.gov>
