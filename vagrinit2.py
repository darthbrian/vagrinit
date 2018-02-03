# This module generates a vagrant init file based on arguments passed in to the module.
# This version utilitizes Classes and Object Orientation instead of traditional function structures.

import argparse

class VagrantClass(object):
    """Create a Vagrantinit file based on arguments"""

    def __init__(self, vagrargs):
        self.count = vagrargs.machnum
        self.machname = vagrargs.machname

    def VagrantCreate(self):
        import sys
        with open("Vagrantfile", 'w') as f:
            f.write('# -*- mode: ruby -*-\n')
            f.write('# vi: set ft=ruby :\n')
            f.write('\n')
            f.write('Vagrant.configure("2") do |config|\n\n')
            i = 1
            while i <= int(self.count):
                vmname = 'vm' + str(i)
                prefix = vmname + '.vm.'
                ipbase = '10.0.0.'
                f.write('config.vm.define "' + vmname + '" do |' + vmname + '|\n')
                f.write('      ' + prefix + 'box = "' + self.machname + '"\n')
                f.write('      ' + prefix + 'network :private_network, ip: "' + ipbase + str(i+10) + '"\n') 
                f.write('      ' + prefix + 'hostname = "' + vmname + '"\n')
                f.write('end\n');
                i = i + 1

            f.write('end')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Create a Vagrant initialization file based on user arguments.")
    parser.add_argument("machnum", help = "The number of virtual machines you want to spin up", type=int)
    parser.add_argument("machname", help = "The type of virtual machine you want to create")
    args = parser.parse_args()
    Vagr = VagrantClass(args)
    Vagr.VagrantCreate()
