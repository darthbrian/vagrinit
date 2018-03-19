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
    arglist = ' '.join(iplist)
    for eachip in iplist:
        #use system command to ping
        response = os.system("nohup vagrant ssh {0} -c '/vagrant/guestping.py {0} --iplist {1}' > /dev/null 2>&1 &".format(machname, arglist))

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
