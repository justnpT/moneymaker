strategos
=========

Python 2.7xy <- scientific python distribution 

### Installing dependencies

1. Make sure you have Python 2.7xy and pip installed
2. Clone strategos repo
Windows:
3. Open the repo main folder
4. hold ctrl+shift and run console Windows git bash. This gives the required admin rights to the process
5. type pip install -r requirements.txt

<h2> Below content is not related to strategos. It is information for later use </h2>

4. Type
   * `setup.py install` <- Windows
   * `sudo python setup.py install` <- Linux
   * `sudo python setup.py install` <- Mac
5. Wait for information: "Finished processing dependencies for api-tests==[version]"
6. Lets check if it works. Type `python main_runner.py --group="sony_business_value"`. We are adding sony_business_value group so that you don't have to wait for all hundreds tests to finish.
7. You should now start seeing small dots appearing. Each dot is a test, and when they all finish, you should see information: `Ran [int] tests in [float]s` it means you have installed everything properly.

### Envirionment variables requirements

1. workspace path must be added to sys.path so that you can import modules by specyfing the exact strategos path.

### Setting up api-tests on Jenkins

Your Jenkins instance should:
    * Python installed
    * virtual env installed

1. Create new Job in Jenkins
2. Add proper source code management, choosing git. 
    * define repository url. eg. git@github.com:Wikia/api-tests.git
    * define creadentials
    * define branches to build. eg. origin/master
3. Provide build commands in rows:
    * `#!/bin/sh`  <- first row
    * `virtualenv --no-site-packages --no-pip --python=python2.7 ve` <- 2nd row. Creates virtual environment
    * `ve/bin/python setup.py install` <- 3rd row. Installs all necessary libraries
    * `ve/bin/python main_runner.py --with-xunit --xunit-file=results.xml` <- 4th row. Runs tests on production with nice log report.
4. Save the job.
5. Now you can run the tests using created Job. To do that open the mainpage of Job and click `build now`


### Running tests by groups


To	run groups use `main_runner.py`file and `--group` parameter: eg: `--group=Activity`. In order to add more than one group, use whitespace for separation and type: `--group=Activity --group=mobile_business_value (...)`. In order to run all groups, leave the empty value

`$ python main_runner.py <nose options> --group=group1 --group=group2 ...`
` if no groups specified, all tests will be run`

Singular tests which execute for longer than 5 seconds, should be marked with 'long' group, so that can be easily excluded from very frequent runs in continous integration services (Jenkins). Example of such test is content_programmed_api test which takes 70 seconds to execute.

### Other

To clean up the working directory:

`$ ./clean`


To run all tests, including those marked TODO (which makes sense for test environments, not production),
install Twisted and run above commands with env variable TEST_WITH_TWISTED_TRIAL set (or run trial apitests directly).
Running with Twisted does not executed tests in parallel or create an xUnit style XML result file.

<h2>Interactive Maps Tests</h2>
To run tests for the maps, run:

`python main_runner.py --token=<token> --group=interactive_maps --env=dev-testinteractivemaps`

The token can be found in InteractiveMapsConfig.json configuration file, which is stored in the config repository.

<h2>Trouble shooting</h2>
<h3>Missing Python modules</h3>

If it happened to me that I had Python 2.7+, virtualenv and `./setup` worked well, `./devbox <name>` worked well but when I wanted to run `export API_ENV="dev-<name>"; trial apitests/test_lyrics_api.py` I got error:
```bash
[ERROR]
Traceback (most recent call last):
  File "/usr/lib/python2.7/dist-packages/twisted/trial/runner.py", line 660, in loadByNames
    things.append(self.findByName(name))
  File "/usr/lib/python2.7/dist-packages/twisted/trial/runner.py", line 469, in findByName
    return filenameToModule(name)
  File "/usr/lib/python2.7/dist-packages/twisted/trial/runner.py", line 85, in filenameToModule
    ret = reflect.namedAny(reflect.filenameToModuleName(fn))
  File "/usr/lib/python2.7/dist-packages/twisted/python/reflect.py", line 464, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/nandy/Phpstormprojects/api-tests/apitests/test_lyrics_api.py", line 1, in <module>
    from wikia import *
  File "/home/nandy/Phpstormprojects/api-tests/apitests/wikia.py", line 7, in <module>
    import os, sys, requests, unittest, unittest.case, itertools, contextlib
exceptions.ImportError: No module named requests

apitests/test_lyrics_api.pyc
```

The solution here was rather simple: install request module. To do so run this command in your terminal:
`sudo pip install <module_name>`
in example:
`sudo pip install requests`
after it's installed `export API_ENV="dev-<name>"; trial apitests/test_lyrics_api.py` should work just fine.

