# Intermediate Python; Selected Topics

Python has become one of the most popular general purpose programming languages over the last decade. Regardless of your interests in programming, Python is a great choice. The language is used at scale to power everything from from web applications to bioinformatics.

This course is designed for people who already know the basics, specifically:

* Basic Python syntax rules
* Data types
* Control flow and looping
* Functions
* Using, installing, and managing libraries

And give those programmers a more powerful toolkit for building useful Python applications that are larger, more maintainable, more efficient, and more interesting. We will cover...

* The use of `argparse` for better CLI tools and scripts.
* Many details about classes and Object Oriented Programming, for larger applications.
* Useful tools and features like iterators, generators, and decorators.
* Testing with `unittest` and `pytest`
* Making web requests synchronously and asynchronously. 
* Proper use of logging.
* Building a simple web server.

## Setup & Installation

* Install python if needed (likely not, but sometimes)
    * [www.python.org/download](www.python.org/download)
    * The latest stable version is suggested.
    * Anything before Python 3.7 is too old.
* Install an IDE or good text editor.
    * Visual Studio Code is a good starting point if you don't already have a preference.
    * [https://code.visualstudio.com/](https://code.visualstudio.com/)
    * Install the Python extension if you go this route [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
    * Because we are asked frequently: NO! Jupyter Notebook is not an acceptable IDE for this class. 
* Some lessons will require the use of 3rd party libraries...
    * See [00_venv_and_setup](00_venv_and_setup) for advice on creating a virtual environment and installing some such packages.
    * For the brave, foolish, and lazy: `pip install requests aiohttp fastapi pytest`
    * If you take the class from Teb's Lab there will be a setup day where you can get help installing these.

## Advice For Instructors

* The suggested order of the material is clearly denoted in the filenames.
* Each folder is designed to be done in a single two-hour session.
* Demonstrations work best while using the debugger to step through the code line by line.
* Exercises are designed such that some students will need additional time after class to complete them, but they should be expected to start in class.
* The general flow is for these materials is:
    * Review the solution from the previous session
    * Demonstration of new concepts (with micro-exercises)
    * Longer Exercise
    * Repeat

## Advice For Self Study Students

* The demonstration sections are written with knowledgeable instructors in mind, and might not contain all the information you'd need to complete an exercise.
    * Consider doing additional research, there are many Python tutorials out there!
        * I especially love the ones by [Real Python](https://realpython.com/)
        * [Free Code Camp](https://www.freecodecamp.org/news/tag/python/) also has a lot of great Python tutorials.
    * Get help from a friend, social network, or elsewhere (Teb's Lab contact information is on our website... I do typically answer emails from students).
    * Try to look at the solutions only as a last resort.

## License

All of the material in this repository is dedicated to the public domain. See the `LICENSE` file for more details.

## Support Free Curricula and Teb's Lab

These materials were created by [Teb's Lab](https://tebs-lab.com). We maintain several open source curriculum repositories, all with public domain dedications. Browse our repos on [Github](https://github.com/Tebs-Lab/), or [our website](https://www.tebs-lab.com/education) or click here to [arrange a training from Teb's Lab](https://www.tebs-lab.com/contracting).
