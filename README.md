# Asynchronous Model and Event Loop

This project demonstrates an asynchronous model and event loop implemented in Python. The asynchronous model allows executing asynchronous tasks using coroutines and generators, while the event loop manages the execution of these tasks.

## Overview

The asynchronous model consists of the following components:

- **Coroutines**: Coroutines are implemented using Python generators. Coroutines can pause their execution using the `yield` keyword and resume later.
- **Event Loop**: The event loop manages the execution of coroutines. It maintains a task queue and handles sleeping coroutines.

## YScheduler Class

The `YScheduler` class is responsible for managing coroutines and the event loop:

- `wait(coro)`: Adds a coroutine to the task queue for execution.
- `ev_sleep(duration)`: Schedules the current coroutine to sleep for a specified duration.
- `event_loop_begin()`: Starts the event loop, which executes coroutines and manages sleeping coroutines.

## Example Usage

The provided example demonstrates the usage of the asynchronous model:

1. Two example coroutines (`s1_Y` and `s2_Y`) are defined using generators. These coroutines print messages asynchronously and schedule themselves to sleep using `sched.ev_sleep`.
2. An instance of `YScheduler` (`sched`) is created.
3. The example coroutines are scheduled for execution using `sched.wait`.
4. The event loop is started using `sched.event_loop_begin`.

## Example Output

The output of the provided example will show messages printed asynchronously by the coroutines, with delays introduced by the sleep durations specified in the coroutines.

## Running the Example

To run the example, execute the Python script containing the provided code. Ensure you have Python installed on your system.

## Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.


```bash
python asynchronous_model.py
