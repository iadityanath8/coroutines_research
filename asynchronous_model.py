from collections import deque
import heapq
import time

class Scheduler:
    def __init__(self) -> None:
        self.ready_task = deque()
        self.sleeping_task = []
        self.id = 0
        self.current = None

    def add_task(self,task_coro) -> None:
        self.ready_task.append(task_coro)
    
    def ev_sleep(self,t_val) -> None:
        self.id += 1
        tt = t_val + time.time()
        heapq.heappush(self.sleeping_task,(tt,self.id,self.current))
        self.current = None  # Stop every task in here 

    def event_loop_begin(self) -> None:
        while self.ready_task or self.sleeping_task:
            if not self.ready_task:
                deadline,_ ,coro = heapq.heappop(self.sleeping_task)
                delta = deadline - time.time()

                if delta > 0:        
                    time.sleep(delta)  
             
                sched.add_task(coro)
            
            self.current = self.ready_task.popleft()
            try:
                next(self.current)
                if self.current:
                    self.add_task(self.current)
            except StopIteration:
                pass

sched = Scheduler()

class AsyncQueue():
    def __init__(self) -> None:
        self.items = deque()
        self.getters = deque()
    
    def put(self,val) -> None:
        self.items.append(val)
        
        if self.getters:
            sched.add_task(self.getters.popleft())

    def get(self):
        if not self.items:
            self.getters.append(sched.current)
            sched.current = None
            yield 
        return self.items.popleft()

q = AsyncQueue()

def producer(n):
    for i in range(n):
        print("Producing", i)
        q.put(i)
        yield sched.ev_sleep(1) 

def consumer():
    while True:
        item = yield from q.get()
        yield sched.ev_sleep(2)
        if item is None:
            break
        print("Consuming",item) 
    
    print("Done")

if __name__ == "__main__":
    sched.add_task(producer(10))
    sched.add_task(consumer())
    sched.event_loop_begin()

