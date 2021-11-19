# tikal-build

As asked on the task, I chose Github Actions as my ci service , and the python project - https://github.com/lvthillo/python-flask-docker.

In order to accomplish this task, I created a path ./github/workflows/github_action_demo.yml

On this yml, with github action templates - I ran the commands for the build and test of our project. 
In order to test our prcess, I have created a python file (called test.py - you can find it under app folder on this repo) using unittest for our app.py (after searching and reading about unittest on pages like https://medium.com/@neeti.jain/how-to-do-unit-testing-in-flask-and-find-code-coverage-fa5201399bc4 and https://www.tutorialspoint.com/unittest_framework/unittest_framework_assertion.htm
in order to understand more about the unittest. 
(Had a conflict about using pytest/unittest - and decided to go with unittest)

On this yml, you can see the steps starts with the pull part,

After that - we run the image,

The next step we test it,

And assuiming the test goes well - the next step is the output of the image. 


That's it for this task - of course there are many other ways to get this task done, for exapmle with jenkins build jobs (with a different tepmlate but with the same steps).
