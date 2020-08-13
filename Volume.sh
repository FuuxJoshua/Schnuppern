#!/bin/bash

change_volume() {
    amixer -q -c 0 sset 'Master' "$1%"
    echo "Volume has been set to $1%"
}

#change_volume $1

get_volume() {
    mixerOut=$(amixer -c 0 sget 'Master')
    text=$(echo "$mixerOut" | awk -F"[]%[]" '/Mono/ {print $2}' )
    echo $text | grep -E '[0-9]+'
}

output_volume() {
    echo "Volume amount $(get_volume)"
}

#output_volume

set_down_volume(){
    vol=$(get_volume)
    echo $vol
    if [ "$vol" -gt 80 ]; then
        #espeak -v "de"  "Das ist viel zu laut Joshua. Mach leise! Jetzt!"
        change_volume 70
    fi
}

monitor_volume() {
    while true; do
        set_down_volume
        sleep 1
    done
}

#set_down_volume

rangebox_volume() {
    New_Volume=$(dialog --rangebox Volume 5 60 0 100 $(get_volume) 2>&1 >/dev/tty)
    change_volume $New_Volume
}

#rangebox_volume

$1 $2