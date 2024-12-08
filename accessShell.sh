#!/bin/bash

# Clone the repository
git clone https://github.com/foxytouxxx/freeroot.git

# Change directory to the cloned repo
cd freeroot

# Automate the "yes/no" prompts using echo and run root.sh in the same shell
echo -e "YES" 
bash -i root.sh

