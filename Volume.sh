#!/bin/bash

change_volume() {
    amixer -q -c 0 sset 'Master' "$1%"
    echo "Volume has been set to $1%"
}

#change_volume $1

get_volume() {
    text=$(awk -F"[]%[]" '/Mono/ {print $2}' <(amixer -c 0 sget 'Master'))
    echo "$text"
}

output_volume() {
    echo "Volume amount $(get_volume)"
}

#output_volume

set_down_volume() {
    while true; do
        if [ $(get_volume) -gt 80 ]; then
            change_volume 50
        fi
        sleep 1
    done
}

#set_down_volume

rangebox_volume() {
    New_Volume=$(dialog --rangebox Volume 5 60 0 100 $(get_volume) 2>&1 >/dev/tty)
    change_volume $New_Volume
}

rangebox_volume