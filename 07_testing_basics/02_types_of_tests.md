# Test Types

There's a lot of jargon in the world of testing. This section is not meant to be exhaustive, rather it should set a foundation. The main types of tests you need to know about today are:

1. Unit Tests
    * These test the smallest "units" of code, typically individual functions and methods.
    * Often times these are a kind of "sanity" check that prove things like 1+1=2
    * These are incredibly useful whenever code is "refactored" because you are able to change the code a ton and still prove nothing critical "changed" about how the function maps inputs to outputs.
    * Typically these tests are fast.
    * These tests do NOT require the entire app to run, and in fact should explicitly be testing only individual components at a time.

2. Integration Tests
    * These test how components work together.
    * They do require multiple components of the app to be instantiated simultaneously.
    * They should not duplicate the unit tests, rather they should test the emergent behaviors that only occur when 2 or more components are used together.
    * They may involve explicitly testing intermediate results and internal states of the relevant components

3. Functional Tests
    * These are like even bigger integration tests.
    * These generally should not test the intermediate results and only test the big picture end goal of a system. 
    * These generally involve several different components of the app working together -- and often require the entire app to be running. 

4. End-to-End Tests
    * These involve simulating an actual user using the app.
    * They are pretty expensive to build, maintain, and run, compared to other tests.
    * They often require additional 3rd party software to perform the simulation
    * They definitely require the entire app to be running.

5. Performance Tests
    * Instead of testing for 'correctness' these test for speed, memory use, or other key performance metrics
    * They are usually related to making sure some critical component of the code runs fast enough under certain expected conditions (such as many simultaneous users, or certain inputs that are known to cause issues).
    * Harder to write because they require judgement calls about what is "fast enough"
    * Harder to make reliable because for them to be relevant you must deploy the code to something like "staging" that emulates the target hardware. 

# Test Methodologies and Metrics

* Test Driven Development
    * A style of software development that prioritizes tests.
    * Tests are often written first, or using "Red Green Refactor" 
    * RGR says...
        1. Write a test case. (Red, because the new test will fail)
        2. Change the code so the test passes. (Green)
        3. Make the code nicer, easier to read, etc. (Refactor)
        4. Repeat.

* Test Coverage: a measure of what share of the lines of code are subject to tests.
    * Some people really shoot for 100% 
    * Some people only test "critical paths" 
    * It's a judgement call.

* There are whole books written about this stuff.
* My advice is:
    * Don't be too dogmatic, use judgement instead of hard rules.
    * Tests are almost always worth it for software that will still be in use one year from now. 
    * Writing tests can help you design a good, maintainable, usable API.
    * Writing tests almost always exposes edge cases, which is valuable. 
    * Great unit tests reduces (but does not eliminate) the need for other kinds of tests.

