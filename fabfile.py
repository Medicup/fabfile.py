#!/usr/bin/env python
from __future__ import print_function
from fabric.api import env, sudo, run , roles, hide
import os.path

env.combine_stderr = True
env.output_prefix = False
env.user = 'stitched'
env.skip_bad_hosts = True

env.roledefs = {
'local': ['localhost'],
  'wb': [ 'wb201.bluerage.lan', 'wb202.bluerage.lan' ],
  'ns': [ 'ns01.bluerage.lan'],
  'db': [ 'db211.bluerage.lan', 'db212.bluerage.lan', 'db213.bluerage.lan'],
  'testwb': ['172.16.210.81', '172.16.210.82'],
  'testdb': ['172.16.210.83', '172.16.210.84', '172.16.210.85']
}

def deploy():
  programs = ['vim', 'dnsutils', 'ccze', 'iftop', 'htop', 'curl', 'openssh-server', 'openssh-client', 'iptables-persistent', 'python-pip', 'git']

  for program in programs:
    sudo('apt-get install -y %s' % (program))
  run('git clone https://github.com/Medicup/debian_script_setup.git')

def update():
  updates = ['update', 'upgrade', 'remove', 'autoclean']

  for update in updates:
    print('Initiating %s function... ' % (update))
    with hide ('output'):
      sudo('apt -y %s' % (update))

  if os.path.isfile('/var/run/reboot-required') == True:
    print("reboot is required")
  else:
    print("Congratulations, no reboot required")
