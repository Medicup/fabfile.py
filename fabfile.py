#!/usr/bin/env python
from __future__ import print_function
from fabric.api import env, sudo, run
import os.path

env.output_prefix = False
env.user = 'stitched'
env.hosts = [ '172.16.210.81', '172.16.210.82' 
  '172.16.210.83', '172.16.210.84', '172.16.210.85']

def deploy():
  programs = ['vim', 'dnsutils', 'ccze', 'iftop',
    'htop', 'curl', 'openssh-server', 'openssh-client', 
    'iptables-persistent', 'python-pip', 'git']

  for program in programs:
    sudo('apt-get install -y %s' % (program))
  run('git clone https://github.com/Medicup/debian_script_setup.git')

def update():
  updates = ['update', 'upgrade', 'remove', 'autoclean']

  for update in updates:
    sudo('apt -y %s' % (update))

  if os.path.isfile('/var/run/reboot-required') == True:
    print("reboot is required")
  else:
    print("Congratulations, no reboot required")
