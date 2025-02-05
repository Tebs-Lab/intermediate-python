There are many forms of parallel programming. Historically, Python was strictly single-threaded -- which means it couldn't perform any form of parallel programming. 

Today though, Python has legitimate support for multiple kinds of parallel code. 

* Multiprocessing -- multiple separate processes running simultaneously on different CPU cores.
     * Operating systems do a lot of this automatically. 
     * Another example is dividing a large list into smaller lists and processing each list on a separate CPU core.
     * Easy to introduce race conditions and other special bugs.
     * Great for CPU bound tasks that can be divided across multiple cores (e.g. 2 cores sum half a list each)
     * Use the `multiprocessing` package in Python

* Concurrency -- a broad term for multiple programs/processes sharing time on a single CPU core.
    * Operating systems also do a lot of this (especially prior to true multi-core processors were invented), and many programming languages also support it.
    * I/O bound tasks are a common use case: do some computation while waiting for the hard drive, or a network request.
    * Python supports two modules for "concurrent" programming:
        * Multithreading
        * Asyncio

* Multithreading
    * More flexible support for various kinds of concurrent workloads.
    * Easier to create errors.
    * "Preemptive" concurrency -- which means any task could be swapped in/out of the processor at any time.
        * Which makes things hard to think about.
        * Requires the use of "locks" to manage any shared resources.

* Asyncio 
    * More limited support for concurrent workloads.
    * Simpler and easier to understand. 
    * "cooperative" concurrency -- which means the code has specific moments when an individual thread "releases" control so another thread can be swapped in/out. 
        * via the async/await keywords in Python.







Concurrent programming, what Python supports, is when  

A common modern example of this is making web requests -- we have to wait for the response from the server, so why don't we do something else while we're waiting?

This paradigm allows us to do certain kinds of "I/O bound" tasks much faster, but it also introduces opportunities for errors and more confusing code. 