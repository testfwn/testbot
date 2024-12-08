#!/bin/bash

# Change to the 'freeroot' directory
cd freeroot

# Automate the "yes/no" prompt and run root.sh in the same shell
echo -e "YES" | bash -i root.sh

# Now run 'ls' as root using 'sudo' to avoid using 'su' and not needing a new terminal
su
ls
