import threading 
from time import sleep
from collections import deque

#Round Robin basic scheduler in here kind off!!
class Scheduler:
    def __init__(self) -> None:
        self.call_queue = deque()

    def wait(self,fn) -> None:
        self.call_queue.append(fn)

    def run(self) -> None:
        while self.call_queue:
            task = self.call_queue.popleft()
            task()


sched = Scheduler()

def f1(x,stop):
    if x < stop:
        print("Hello my friends")
        sched.wait(lambda: f1(x+1,stop))

def f2(x,stop):
    if x < stop:
        print("Printing from another thread kind offf!!!")
        sched.wait(lambda: f2(x+1,stop))

if __name__ == "__main__":
    sched.wait(lambda: f1(0,4))
    sched.wait(lambda: f2(0,3))
    sched.run()
