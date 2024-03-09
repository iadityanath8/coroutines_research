import time
from threading import Thread
import heapq
from time import sleep
from collections import deque

# Basic Example of Generators
def c1():   
    result = 0
    v = 0 
    while True:
        value = yield v
        result += value
        v = result

#Scheduler for Yield async methods

class YScheduler:
    
    def __init__(self) -> None:
        self.task_queue = deque()
        self.sleeping = []
        self.current = None     # current executing coroutine
        self.id = 0

    def wait(self,coro) -> None:
        self.task_queue.append(coro)
    
    def ev_sleep(self,duration) -> None:
        self.id += 1
        deadline = duration + time.time()
        heapq.heappush(self.sleeping,(deadline,self.id,self.current))
        self.current = None    #till now this coroutine will not exceute in here 
    
    # Event Loop
    def event_loop_begin(self):
        while self.task_queue or self.sleeping:
            if not self.task_queue:
                dead,_,coro = heapq.heappop(self.sleeping)
                delta = dead - time.time()

                if delta > 0:
                    sleep(delta)
                
                self.wait(coro)
                
            self.current = self.task_queue.popleft()
            try:
                next(self.current)
                if self.current:
                    self.wait(self.current)
            
            except StopIteration:
                print("Done Event Loop")
                pass

#Going asyncrhrounous using Yield and Generators

def s1():
    sleep(1)
    for _ in range(4):
        print("printing from somewhere")

def s2():
    sleep(0.9)
    for _ in range(5):
        print("printing someother values in here")

#replacing these examples for the yield 
sched = YScheduler()

def s1_Y():
    for _ in range(4):
        print("printing from somewhere")
        sched.ev_sleep(0.9)
        yield
        

def s2_Y():
    for _ in range(5):        
        print("printing someother values in here")
        sched.ev_sleep(1)        
        yield 


if __name__ == "__main__":
    sched.wait(s1_Y()) 
    sched.wait(s2_Y())
    sched.event_loop_begin()



