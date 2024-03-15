#!/bin/bash

# download ycsb tarball
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.11.0/ycsb-0.11.0.tar.gz
tar xf ycsb-0.11.0.tar.gz
mv ycsb-0.11.0 YCSB