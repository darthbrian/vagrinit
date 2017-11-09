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




#Vagrant.configure("2") do |config|

#  config.vm.define "web" do |web|
#        web.vm.box = "ubuntu/trusty64"
#        web.vm.network :private_network, ip: "10.0.0.10"
#        web.vm.hostname = "web"
#  end
#  config.vm.define "db" do |db|
#        db.vm.box = "ubuntu/trusty64"
#        db.vm.network :private_network, ip: "10.0.0.11"
#        db.vm.hostname = "db"
#  end
#  config.vm.define "gtw1" do |gtw1|
#        gtw1.vm.box = "ubuntu/trusty64"
#        gtw1.vm.network :private_network, ip: "10.0.0.12"
#        gtw1.vm.hostname = "gtw1"
#  end
#end
