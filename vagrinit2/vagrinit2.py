# This module generates a vagrant init file based on arguments passed in to the module.
# This version utilitizes Classes and Object Orientation instead of traditional function structures.

if __name__ == "__main__":
    import argparse
    from vagrcreate import VagrantClass
    parser = argparse.ArgumentParser(description = "Create a Vagrant initialization file based on user arguments.")
    parser.add_argument("machnum", help = "The number of virtual machines you want to spin up", type=int)
    parser.add_argument("machname", help = "The type of virtual machine you want to create")
    args = parser.parse_args()
    Vagr = VagrantClass(args)
    Vagr.VagrantCreate()
