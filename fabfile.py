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
  'testdb': ['172.16.210.83', '172.16.210.84', '172.16.210.85'],
  'all' : ['wb201.bluerage.lan', 'wb202.bluerage.lan', 'db211.bluerage.lan', 'db212.bluerage.lan', 'db213.bluerage.lan', 'ns01.bluerage.lan', 'localhost'],
  'testall' : ['172.16.210.81', '172.16.210.82', '172.16.210.83', '172.16.210.84', '172.16.210.85']
}

def deploy():
  run('git clone https://github.com/Medicup/debian_script_setup.git')
  run(' cd debian_script_setup')
  sudo('chmod 755 debian_script_setup/reset_master.py')
  run('cp debian_script_setup/reset_master.py reset_master.py')
  run('cp debian_script_setup/master master')
  sudo('./reset_master.py')
  sudo('./master')
  sudo('rm reset_master.py master')

def update():
  updates = ['update', 'upgrade', 'autoremove', 'autoclean']

  for update in updates:
    print('Initiating %s function... ' % (update))
    with hide ('output'):
      sudo('apt -y %s' % (update))

  if os.path.isfile('/var/run/reboot-required') == True:
    print("reboot is required")
  else:
    print("Congratulations, no reboot required")
