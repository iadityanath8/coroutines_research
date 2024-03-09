import threading 
import time
import queue
import heapq
from time import sleep
from collections import deque

#Round Robin basic scheduler in here kind off!
class Scheduler:
    def __init__(self) -> None:
        self.call_queue = deque()
        self.wait_list = []
        self.id = 0

    def wait(self,fn) -> None:
        self.call_queue.append(fn)
    
    def wait_until(self,fn,until) -> None:
        self.id += 1
        now = time.time()
        upto = now + until
        heapq.heappush(self.wait_list,(upto,self.id,fn))

    def run(self) -> None:
        while self.call_queue or self.wait_list:
            
            if not self.call_queue:
                deadline,_, task = heapq.heappop(self.wait_list)
                delta = deadline - time.time()
                
                if delta > 0:
                    sleep(delta)
                
                self.call_queue.append(task)

            while self.call_queue:
                task = self.call_queue.popleft()
                task()


sched = Scheduler()
BUFFER_SIZE = 5
buffer = queue.Queue(BUFFER_SIZE)

def sayhello(stop):
    def _run(x):
        if x < stop:
            print("Hello my friends")
            sched.wait(lambda: _run(x + 1))
    _run(0)


def saymeow(stop):
    def _run(x):
        if x < stop:
            print("Printing from another thread kind offf!!!")
            #sched.wait_until(lambda: _run(x + 1),3)
            sched.wait(lambda: _run(x + 1))
    _run(0)

#using threads
def producer():
    global buffer

    for i in range(10):
        buffer.put(i)
        print(f"produced {i}")
        time.sleep(1)
    
    buffer.put(None)

def consumer():
    global buffer
    
    while True:
        item = buffer.get()
        if item is None:
            break

        print(f"Consumed item is {item}")
        time.sleep(1)


#using async and coroutine model

class AsyncQueue:
    def __init__(self) -> None:
        self.items = deque()
        self.waiting_getters = deque()

    def put(self,val):
        self.items.append(val)
        if self.waiting_getters:
            fn = self.waiting_getters.popleft()
            sched.wait(fn)

    def get(self,cb):
        if self.items:
            cb(self.items.popleft())
        else:
            self.waiting_getters.append(lambda: self.get(cb))

qbuffer = AsyncQueue()

def producer_async(stop):
    def _run(x):
        if x < stop:
            qbuffer.put(x)     
            print("Produced ",x)
            sched.wait_until(lambda: _run(x + 1),1)
        else:
            print("Producer Done")
            qbuffer.put(None)
    _run(0)

def consumer_async():
    
    def _run(x):
        if x is None:
            print("Consumer is Finished")
        else:
            print("Consumed ",x)
            sched.wait_until(lambda: consumer_async(),3)
    
    qbuffer.get(_run)

if __name__ == "__main__":
    #  t1 = threading.Thread(target=producer)
    #  t2 = threading.Thread(target=consumer)

    #  t1.start()
    #  t2.start()

    #  t1.join()
    #  t2.join()

    #  print("Donde")
    
    sched.wait(lambda: producer_async(10))
    sched.wait(lambda: consumer_async())

    sched.run()
