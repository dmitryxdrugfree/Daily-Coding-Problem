"""
Daily Coding Problem: Problem #10
"""

import time

def scheduler(f, n_time):
	time.sleep(n_time/1000)
	return f()

def run_scheduler():
    try:
        while True:
            print(scheduler(lambda: "Time to work!", 1000))
    except KeyboardInterrupt:        
        print("Notification is Off")

run_scheduler()