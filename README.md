HW 2

To start, I made a few improvements without testing since I didn't
see how to.  First, I changed all the internal variable names in 
the classes so that they were more descriptive.  Also, I broke the
single file from last week into three files: The first is the classes,
the second is the user interface (the cmd loop), and the third is 
the test file. The test file tests the classes and methods in the class
file, as I don't know how to interact with the input method from another
method.

Next, I started down a testing path that was wrong, so there are several commits
that are down a different path. The new direction I'm going in is I need to make the code more 
testable and exception safe by refactoring the cmd loop code so that the methods that take
input simply take the user input and pass it along without doing anything else. 
This way, I can test the internal methods in the test suite, and leave the methods
that the user is interacting with to spot checking since the code is so simple. In
this way, the test suite is simulating the way the user facing methods act.
