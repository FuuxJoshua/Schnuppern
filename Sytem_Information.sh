
    cpu_now=($(head -n1 /proc/stat))
    cpu_sum="${cpu_now[@]:1}"
    cpu_sum=$((${cpu_sum// /+}))
    cpu_delta=$((cpu_sum - cpu_last_sum))
    cpu_idle=$(( cpu_now[4] - cpu_last[4]))
    cpu_used=$((cpu_delta - cpu_idle))
    cpu_usage=$((100 * cpu_used / cpu_delta))
    cpu_last=("${cpu_now[@]}")
    cpu_last_sum=$cpu_sum
    echo $cpu_usage