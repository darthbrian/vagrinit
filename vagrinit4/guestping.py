#!/usr/bin/env python
# This program will be called remotely from the host so that it can ping all its neighbors. 
# We write the data to an output file.

import os
import json


def PingGuest(machname, iplist):
    """ping each guest from the specified guest"""
    #Open our output file
    with open(machname + 'ping.out', 'w') as outfile:
        pingsuccess = 0
        num_of_ips = len(iplist)
        outfile.write("*** " + machname + " is currently attempting to ping all guests on the private Vagrant network. ***\n")
        for eachip in iplist:
            #use system command to ping
            #response = os.system("vagrant ssh " + str(machname) + " -c 'ping -c 1 " + str(eachip) + "' > /dev/null 2>&1")
            response = os.system("ping -c 1 " + str(eachip) + " > /dev/null 2>&1")
            if response == 0:
                pingsuccess += 1
                outfile.write('{0} has successfully pinged IP {1}\n'.format(machname, str(eachip)))
            else:
                outfile.write('***ERROR: Vagrant machine {0} was unable to ping guest with IP {1}\n'.format(machname, eachip))

        if pingsuccess == num_of_ips:
            outfile.write(machname + ' has successfully pinged all guests on the private Vagrant network.\n')
        else:
            outfile.write('>>> ERROR: ' + machname + ' was not able to ping one or more machines on the private Vagrant network. <<<\n')

#def PingEachGuest():
#    """loop through our list of machines and for each one ping all the other guests"""
#
#    #open json file with IP data
#    with open('iphost.json', 'r') as ipfile:
#        #get dictionary data
#        ipdata = json.load(ipfile)
#
#        #loop through machines
#        for guestname in ipdata:
#            #for each machine...
#            iplist = ipdata[guestname]
#
#            #ping all the other machines
#            PingGuest(guestname, iplist)

if __name__ == "__main__":
    import argparse
    """The list of machines to ping are passed in as arguments. We parse them out via argparse and the 'pinglist' argument."""
    parser = argparse.ArgumentParser()
    parser.add_argument("machname", help = "The name of virtual machine that is doing the pinging")
    parser.add_argument('--iplist', nargs='+', type=str, default=[], help='The list of IPs to ping')
    args = parser.parse_args()
    pinglist = args.iplist
    print(pinglist)
#    PingEachGuest()
    PingGuest(args.machname, pinglist)
