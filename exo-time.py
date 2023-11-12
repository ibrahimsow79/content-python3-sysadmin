#!/usr/bin/env python3.8

import time

start_time = time.localtime()
print(f"Timer started at {time.strftime('%X', start_time)}")

# Whait for user to stop timer 

input("Press 'Enter' to stop Timer")

stop_time = time.localtime()
difference = time.mktime(stop_time) - time.mktime(start_time)

print(f"Timer stopped at {time.strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
