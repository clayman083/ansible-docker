Docker
=========

[![Build Status](https://github.com/clayman74/ansible-docker/workflows/Tests/badge.svg)](https://github.com/clayman74/ansible-docker)

This role installs and configures the Docker.

Requirements
------------

This role requires Ansible 1.4 or higher and platform requirements are listed in the metadata file.

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - role: clayman74.docker

Swarm
-----

This role allows you to create a Docker Swarm from multiple hosts

Example playbook:

    - hosts: swarm
      become: true

      vars:
        swarm_tokens_path: "{{ inventory_dir }}/.credentials/services/swarm"

      tasks:
        - name: Add exporter to Consul Catalog
          import_role:
            name: clayman74.docker
            tasks_from: swarm
          tags:
            - swarm


Example inventory:

    localhost ansible_connection=local

    [swarm:children]
    swarm-master
    swarm-managers
    swarm-workers

    [swarm-master]
    alpha ansible_host=192.168.100.10

    [swarm-managers]
    bravo ansible_host=192.168.100.11
    delta ansible_host=192.168.100.12

    [swarm-workers]
    whiskey ansible_host=192.168.100.13
    yankee ansible_host=192.168.100.14
    zulu ansible_host=192.168.100.15

    [swarm:vars]
    ansible_user=vagrant

    [swarm-master:vars]
    swarm_master=true
    swarm_manager=true

    [swarm-managers:vars]
    swarm_manager=true
    swarm_remote_addrs=['192.168.100.10']

    [swarm-workers:vars]
    swarm_worker=true
    swarm_remote_addrs=['192.168.100.10', '192.168.100.11', '192.168.100.12']


License
-------

MIT

Author Information
------------------

Kirill Sumorokov
