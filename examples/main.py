import meowsync


def f():
    for i in range(10):
        print("Hello from function f")
        yield 

def g():
    for i in range(5):
        print("Bonjour mein friund")
        yield


sched = meowsync.Scheduler()
sched.add_task(f())
sched.add_task(g())
sched.event_loop_begin()
