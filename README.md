
# Experiment/Research: Round Robin Basic Scheduler Implementation

## Introduction:
This experiment demonstrates a basic implementation of a Round Robin scheduler using Python. A Round Robin scheduler is a preemptive CPU scheduling algorithm that allocates a fixed time slice to each process or task in a circular queue. Once a task's time slice expires, it is put back at the end of the queue, allowing other tasks to execute in the meantime.

## Code Overview:
- The code consists of a `Scheduler` class responsible for managing the execution of tasks.
- Tasks are added to the scheduler using `wait` and `wait_until` methods.
- `run` method executes tasks in a round-robin manner until the call queue and wait list are empty.
- The experiment includes two sample functions `f1` and `f2` which represent tasks to be executed by the scheduler.

## Usage:
- To use the scheduler, create an instance of `Scheduler`.
- Add tasks using `wait` or `wait_until` methods.
- Start the scheduler by calling the `run` method.

## Example:
```python
sched = Scheduler()

def f1(x, stop):
    if x < stop:
        print("Hello my friends")
        sched.wait(lambda: f1(x + 1, stop))

def f2(x, stop):
    if x < stop:
        print("Printing from another thread kind offf!!!")
        sched.wait_until(lambda: f2(x + 1, stop), 3)

if __name__ == "__main__":
    sched.wait(lambda: f1(0, 4))
    sched.wait(lambda: f2(0, 3))
    sched.run()
