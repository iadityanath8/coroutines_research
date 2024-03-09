import threading 
import time
from time import sleep
from collections import deque

#Round Robin basic scheduler in here kind off!!
class Scheduler:
    def __init__(self) -> None:
        self.call_queue = deque()
        self.wait_list = []

    def wait(self,fn) -> None:
        self.call_queue.append(fn)
    
    def wait_until(self,fn,until) -> None:
        now = time.time()
        upto = now + until
        self.wait_list.append((upto,fn))
        self.wait_list = sorted(self.wait_list)

    def run(self) -> None:
        while self.call_queue or self.wait_list:
            
            if not self.call_queue:
                deadline, task = self.wait_list.pop(0)
                delta = deadline - time.time()
                
                if delta > 0:
                    sleep(delta)
                    self.call_queue.append(task)

            while self.call_queue:
                task = self.call_queue.popleft()
                task()


sched = Scheduler()

def f1(x,stop):
    if x < stop:
        print("Hello my friends")
        sched.wait(lambda: f1(x + 1,stop))


def f2(x,stop):
    if x < stop:
        print("Printing from another thread kind offf!!!")
        sched.wait_until(lambda: f2(x + 1,stop),3)


if __name__ == "__main__":
    sched.wait(lambda: f1(0,4))
    sched.wait(lambda: f2(0,3))
    sched.run()

