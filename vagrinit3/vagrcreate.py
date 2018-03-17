# This module generates a vagrant init file based on arguments passed in to the module.
# This version utilitizes Classes and Object Orientation instead of traditional function structures.

class VagrantClass(object):
    """Create a Vagrantinit file based on a .json input file"""

    def __init__(self, filename):
        self.json_input_file = filename

    def VagrantCreate(self):
        import sys
        import json
        with open("Vagrantfile", 'w') as f:
            f.write('# -*- mode: ruby -*-\n')
            f.write('# vi: set ft=ruby :\n')
            f.write('\n')
            f.write('Vagrant::DEFAULT_SERVER_URL.replace(\'https://vagrantcloud.com\')\n\n')
            f.write('Vagrant.configure("2") do |config|\n\n')
            i = 1

            with open(self.json_input_file, 'r') as vagrinfofile:
                info_data = json.load(vagrinfofile)
                for box in info_data["boxes"]:
                    vmname = box["name"]
                    prefix = vmname + '.vm.'
                    machtype = box["machtype"]
                    ram = box["ram"]
                    ip = str(box["ip"])
                    f.write('config.vm.define "' + vmname + '" do |' + vmname + '|\n')
                    f.write('      ' + prefix + 'box = "' + machtype + '"\n')
                    f.write('      ' + prefix + 'network "private_network" , ip: "' + ip + '"\n') 
                    f.write('      ' + prefix + 'hostname = "' + vmname + '"\n')
                    f.write('      ' + prefix + 'provision "shell", path: "gitinstall.sh"\n')
                    f.write('      ' + prefix + 'provider "virtualbox" do |vram|\n')
                    f.write('          vram.memory = "' + str(ram) + '"\n')
                    f.write('      end\n');
                    f.write('end\n');
            f.write('end')
