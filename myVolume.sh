#!/bin/bash

amixer -c 0 sset 'Master' $1
echo "Volume has been set to $1%"
