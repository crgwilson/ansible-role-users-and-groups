# Ansible role: Users and Groups

![Molecule Test](https://github.com/crgwilson/ansible-role-users-and-groups/workflows/Molecule%20Test/badge.svg)

Create arbitrary users and groups

* Create user groups
* Create users
* Insert SSH keys into user home directories
* Create user authorized keys

## Variables

### users_and_groups_groups

Dictionary defining groups to create

Example:

```yaml
users_and_groups_groups:
  group1:
    state: present
  group2:
    state: absent
```

### users_and_groups_users

Dictionary defining users to create

Example:

```yaml
users_and_groups_users:
  bob:
    shell: /bin/bash
    ssh_key: bobs_key.pem # file path for lookup
    authorized_key: bobs_authorized_key # file path for lookup
    groups:
      - bobs_group
      - sudo
```

## Testing

Unit tests for this project are setup using [Molecule](https://molecule.readthedocs.io/en/stable/) & [Docker](https://www.docker.com/).
Tests can be run using the below command:

```console
foo@bar:~$ molecule test --all
```
