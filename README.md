# MeowAsync Library Documentation

## Overview

This async library provides functionality for scheduling and executing asynchronous tasks using the round-robin scheduling algorithm. It includes a `Scheduler` class for managing tasks and an `AsyncQueue` class for implementing asynchronous queues.

## Classes

### Scheduler

The `Scheduler` class manages the scheduling and execution of asynchronous tasks.

#### Methods

- `__init__()`: Initializes the scheduler with empty task queues.
- `add_task(task_coro)`: Adds an asynchronous task coroutine to the ready task queue.
- `ev_sleep(t_val)`: Suspends the current task and schedules it to be resumed after a specified time interval.
- `event_loop_begin()`: Starts the event loop to execute tasks according to the round-robin scheduling algorithm.

### AsyncQueue

The `AsyncQueue` class implements an asynchronous queue.

#### Methods

- `__init__()`: Initializes the queue with an empty item deque and an empty getter deque.
- `put(val)`: Adds an item to the queue and resumes a waiting getter coroutine if available.
- `get()`: Retrieves an item from the queue asynchronously. If the queue is empty, suspends the current task until an item becomes available.

## Example Usage

```python
from async_library import Scheduler, AsyncQueue

# Create a scheduler
sched = Scheduler()

# Create an async queue
q = AsyncQueue()

# Define producer and consumer coroutines
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
        print("Consuming", item)
    print("Done")

# Add tasks to the scheduler
sched.add_task(producer(10))
sched.add_task(consumer())

# Start the event loop
sched.event_loop_begin()
