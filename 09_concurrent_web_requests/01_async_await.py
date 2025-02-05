# In Python, core support for asynchronous / concurrent programming comes from
# the async and await keywords, as well as the asyncio module.

# Asyncio is the easiest method to write asynchronous Python code.
import asyncio

# The async keyword is used to define a function that will run asynchronously.
async def sleepy_function():
    print("I'm going to sleep for 1 second.")

    # Await prevents the next line of code from running until the awaited task is complete.
    # It also releases control back to the event loop, allowing other code to run.
    await asyncio.sleep(1) 
    print("I woke up!")

# the .run function will run an async function and wait for it to complete.
asyncio.run(sleepy_function())
print('finished first task')
asyncio.run(sleepy_function())
print("finished second task")
print('\n\n\n')

# By comparison .create_task will create tasks in the background and 
# add them to the event loop. This allows for multiple tasks to run concurrently.
# However, we're not allowed to do this at the top level of a script.
async def two_sleepy():
    coroutine_1 = asyncio.create_task(sleepy_function())
    coroutine_2 = asyncio.create_task(sleepy_function())

    await coroutine_1
    await coroutine_2

    print("Both tasks are done!")

asyncio.run(two_sleepy())
print('\n\n\n')

# INSTRUCTOR NOTE: Draw a diagram of the event loop and how the tasks are added to the queue.

# You can also use asyncio.gather to run multiple tasks concurrently and wait for them all to complete.
async def multi_sleepy(n=5):
    tasks = [sleepy_function() for i in range(n)]
    await asyncio.gather(*tasks)

asyncio.run(multi_sleepy())

# Mini-exercise: Write a new version of sleepy_function such that:
#   * It accepts a parameter that is printed before and after the sleep (think of this as an ID)
#   * It sleeps for a random amount of time between 1 and 3 seconds
# Then, write a new version of multi_sleepy that calls this new sleepy function with 5 different IDs.

# hint, here's how you can generate a random number between 1 and 3:
import random
x = random.randint(1, 3)
