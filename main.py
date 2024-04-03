from meowsync import Nsync
import time

sc = Nsync.Scheduler()

def f():
    for _ in range(15):
        print("AHH")
        yield

def g():
    for _ in range(5):
        print("UHH")
        yield sc.ev_sleep(3)

sc.add_task(f())
sc.add_task(g())


sc.event_loop_begin()
