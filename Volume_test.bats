#!/usr/bin/env bats

setup(){
  . ./Volume.sh
}

@test "get_and_set_volume" {
  change_volume 50
  volume=$(get_volume)
  [ "$volume" == "51" ]
}

@test "set_down_volume" {
  change_volume 90
  set_down_volume
  volume=$(get_volume)
  [ "$volume" == "51" ]
}
