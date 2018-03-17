#!/usr/bin/env bash

echo "Installing Git and setting it up..."
isUbuntu=`uname -a | grep -ic 'ubuntu'`
isDebian=`uname -a | grep -ic 'debian'`
if [[ $isUbuntu -gt 0 || $isDebian -gt 0 ]];
then
    echo "Detected Ubuntu or Debian Installation. Using apt-get..."
    if ! [ -x "$(command -v git)" ];
    then
        sudo apt-get update >/dev/null 2>%1
        sudo apt-get install -y git-all >/dev/null 2>&1
    else
        echo "Detected git is already installed. Skipping installation..."
    fi
else
    echo "Detected Centos or Red Hat Installation. Using yum..."
    if ! [ -x "$(command -v git)" ];
    then
        sudo yum install -y git >/dev/null 2>&1
    else
        echo "Detected git is already installed. Skipping installation..."
    fi
fi
