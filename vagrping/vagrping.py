#!/usr/bin/env python3
# This program automatically pings all the guests in a vagrant environment consisting of multiple boxes. 
# We read in a JSON file created when vagrinit4 runs and walk over the IPs.
# Can issue a command to a guest to ping another guest with this command : vagrant ssh <guest1> -c 1 'ping <guest 2>'

import os
import json


def PingGuest(machname, iplist):
    """ping each guest from the specified guest"""
    pingsuccess = 0
    num_of_ips = len(iplist)
    print("*** " + machname + " is currently attempting to ping all guests on the private Vagrant network. ***")
    for eachip in iplist:
        #use system command to ping
        response = os.system("vagrant ssh " + str(machname) + " -c 'ping -c 1 " + str(eachip) + "' > /dev/null 2>&1")
        if response == 0:
            pingsuccess += 1
        else:
            print('***ERROR: Vagrant machine {0} was unable to ping guest with IP {1}'.format(machname, eachip))

    if pingsuccess == num_of_ips:
        print(machname + ' has successfuly pinged all guests on the private Vagrant network.')
    else:
        print ('>>> ERROR: ' + machname + ' was not able to ping one or more machines on the private Vagrant network. <<<')

def PingEachGuest():
    """loop through our list of machines and for each one ping all the other guests"""

    #open json file with IP data
    with open('iphost.json', 'r') as ipfile:
        #get dictionary data
        ipdata = json.load(ipfile)

        #loop through machines
        for guestname in ipdata:
            #for each machine...
            iplist = ipdata[guestname]

            #ping all the other machines
            PingGuest(guestname, iplist)

if __name__ == "__main__":
    import argparse
    PingEachGuest()
