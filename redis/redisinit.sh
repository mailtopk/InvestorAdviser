#!/bin/sh

is_redis_running(){
    redis-cli ping
}

redis-server --append yes &

until is_redis_running | grep -q PONG; do
    echo "Redis server starting..."
    sleep 1
done

redis-cli SET example_init_data "Initial data here"

wait