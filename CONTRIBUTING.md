# CONTRIBUTING

You can get this software using git by running the following:

> git clone https://github.com/david-a-wheeler/hello.git

We use GitHub and git to manage the project.
If you don't know how to use GitHub or git, see
[GitHub help](https://help.github.com/).

If you have feedback (including bug reports and enhancement requests),
[please create a GitHub issue](https://github.com/david-a-wheeler/hello/issues).

If you want to propose a contribution, please create a pull request on
GitHub for our project
[david-a-wheeler/hello](https://github.com/david-a-wheeler/hello).

Contributions must conform to our license (MIT) and must agree 
to the
[Developer Certificate of Origin (DCO) Version 1.1](https://developercertificate.org/) (which states that you have the legal right to make the contribution).
To clearly indicate that you agree with the DCO,
each commit in your pull request should have a line with
"Signed-off-by: YOURNAME <YOUREMAIL>"; you can create that
with the "-s" option of "git commit".

This program is written in Python3.
Code contributions should follow
[PEP 8 (Style Guide for Python Code)](https://www.python.org/dev/peps/pep-0008/),
and pass the "pylint" style checker.
Please make sure your changes pass pylint before creating a pull request.

Here's one way you can install the pylint style checker:

> pip3 install pylint

Here's one way you can run the pylint style checker:

> python3 -m pylint hello.py
