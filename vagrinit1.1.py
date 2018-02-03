#!/usr/bin/env python3
# This module generates a vagrant init file based on arguments passed in to the module.


import sys
import argparse

def WrVagrInit(count , machname ):
    """Create a Vagrantinit files based on arguments"""

    with open("Vagrantfile", 'w') as f:
        f.write('# -*- mode: ruby -*-\n')
        f.write('# vi: set ft=ruby :\n')
        f.write('\n')
        f.write('Vagrant.configure("2") do |config|\n\n')
        i = 1
        while i <= int(count):
            vmname = 'vm' + str(i)
            prefix = vmname + '.vm.'
            ipbase = '10.0.0.'
            f.write('config.vm.define "' + vmname + '" do |' + vmname + '|\n')
            f.write('      ' + prefix + 'box = "' + machname + '"\n')
            f.write('      ' + prefix + 'network :private_network, ip: "' + ipbase + str(i+10) + '"\n') 
            f.write('      ' + prefix + 'hostname = "' + vmname + '"\n')
            f.write('end\n');
            i = i + 1

        f.write('end')

 
def main():
    parser = argparse.ArgumentParser(description = "Create a Vagrant initialization file based on user arguments.")
    parser.add_argument("machnum", help = "The number of virtual machines you want to spin up", type=int)
    parser.add_argument("machname", help = "The type of virtual machine you want to create")
    args = parser.parse_args()
    WrVagrInit(args.machnum, args.machname)

if __name__ == "__main__":
    main()
