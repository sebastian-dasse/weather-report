# weather-report

Still work in progress.

## Open tasks
- [x] query weather api
- [x] extract data from json/xml
- [x] print data
- [ ] complete documentation

## Prerequisites

### mandatory
- Python 2
- Requests

### recommended
- virtualenv

## Installation

It is recommended to install Requests inside a virtualenv, to keep your system setup nice and tidy. However, if you don't care to mess up your system -- feel free to skip all steps related to virtualenv.

To install on Windows do the following:

1. Install the latest [Python 2](https://www.python.org/download/).
2. Open the git bash.
3. Install [virtualenv](https://virtualenv.pypa.io/en/stable/installation/). The preferred way to do this is through *pip*, which comes with your Python installation: `[sudo] pip install virtualenv`.
4. Create a virtualenv: `virtualenv ~/my_env`.
5. Activate *my_env*: `source ~/my_env/Scripts/activate`.
6. To ensure that *my_env* was indeed activated you can check, that the Python version from within your virtualenv is chosen: `which python`.
7. Install Requests inside your virtualenv: `pip install requests`.
8. To ensure that Requests was sucessfully installed check the output of: `pip list`.
9. To run the weather-report do the following: ... TODO
10. To deactivate *my_env* when you are done: `deactivate`.
