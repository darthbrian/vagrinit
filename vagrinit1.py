# This module generates a vagrant init file based on arguments passed in to the module.

def WrVagrInit(count , machname ):
    """Create a Vagrantinit files based on arguments"""

    f = open('Vagrantfile', 'w')
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
        f.write('      ' + prefix + 'network :private_network, ip: "' + ipbase + str(i) + '"\n') 
        f.write('      ' + prefix + 'hostname = "' + vmname + '"\n')
        f.write('end\n');
        i = i + 1

    f.write('end')
    f.close()

 
if __name__ == "__main__":
    import sys
    a = 0
    for arg in sys.argv:
        a = a + 1
    if a < 3:
        print("not enough arguments")
        sys.exit()
    WrVagrInit(sys.argv[1], sys.argv[2])
