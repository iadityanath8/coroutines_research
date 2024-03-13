# Asynchronous Programming with Generators and Yield

This project demonstrates asynchronous programming in Python using generators and the `yield` statement. It includes a simple scheduler, `YScheduler`, which manages the execution of coroutines based on cooperative multitasking.

## Basic Example of Generators

The `c1` function is an example of a coroutine defined using a generator. It calculates the running sum of provided values asynchronously using `yield`.

## Scheduler for Yield Async Methods

The `YScheduler` class serves as a scheduler for managing asynchronous coroutines. It utilizes a priority queue for sleeping coroutines and a task queue for pending coroutines.

### Methods:

- `wait(coro)`: Adds a coroutine to the task queue.
- `ev_sleep(duration)`: Puts the current coroutine to sleep for a specified duration.
- `event_loop_begin()`: Initiates the event loop, executing coroutines as per their scheduling.

## Asynchronous Examples

The provided examples, `s1` and `s2`, demonstrate synchronous code execution with delays using `sleep`.

### Replaced with Yield:

These examples are replaced with asynchronous versions using generators and `yield`:

- `s1_Y`: Asynchronously prints messages from somewhere with a delay between iterations.
- `s2_Y`: Asynchronously prints some other values with a different delay between iterations.

## Usage

1. Create an instance of `YScheduler`.
2. Add asynchronous coroutines to the scheduler using `wait`.
3. Begin the event loop using `event_loop_begin`.

```python
if __name__ == "__main__":
    sched = YScheduler()
    sched.wait(s1_Y()) 
    sched.wait(s2_Y())
    sched.event_loop_begin()

