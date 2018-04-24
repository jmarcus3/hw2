HW 2

NOTE: THE FINAL GREEN COMMIT WAS SIMPLY A CHANGE TO THE README FILE
AND WAS NOT INTENDED TO BE PART OF THE TDD PROCESS.

Some notes regarding this assignment:

First, I recently read the canvas post about testing the refactoring improvements
of the code (like making better variable names and such) but because I 
started on this before I read the post, I didn't use TDD just for changing
the variable names. I understand that this was not the way to go, but rather than
changing my code back and starting from scratch, I'll just write here what
I think I could have done:

To test the breaking up of the code into separate files, I could have
written a test that literally just tested to see if the new file with
the non-UI classes existed and had the expected class methods. Once
I did that, I would be free to import the classes into my UI file
as a refactor in order to satisfy the requirement that information
should only exist in one place.  

To test the variable names and method names, I could have written
a test that tried to call the methods of classes with the better names,
and then change them when they throw errors.    

Next, my UI file uses pythons input function in order to get user input.
I don't know how to fake user input from another function, but seemed like
clean code to have the methods that call for user input call other internal
methods that actually do the work. My test code tests the internal methods,
but I couldn't figure out how to test that the UI methods were printing
the right thing, so it was in the refactoring stage that I spot checked to 
ensure that the UI methods printed what was returned to them by the methods
they called.

Further, you'll see that the above decision was made part of the way through, and
my first several commits are going down a different development path that I realized
was incorrect and started over.

Finally, note that at some point during the processes I wound up needing to refactor 
some of the tests to take into account the fact that the date was changing during the
testing process which was causing tests to fail, so at some point in my commit history
you will see the tests change from hard-coded dates to calling date generating methods. 
