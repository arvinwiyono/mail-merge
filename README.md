# FIT4004 Assignment 3 - Automated Unit Testing #

![python-snake.png](https://bitbucket.org/repo/LBGnXb/images/2060809057-python-snake.png)

## Simple mailmerge functionality with Python ##
* Arvin Wiyono (awiy1@student.monash.edu)
* Wanyu Yin (wyyin1@student.monash.edu)

### In this assignment, we use: ###

* Python 3.3.X
* Python unittest
* Python unittest.mock and patch
* Nosetests (http://nose.readthedocs.io/en/latest/)
* Coverage.py (https://coverage.readthedocs.io/en/coverage-4.0.3/)
* Drone.io for CI (https://drone.io/)

### Build status ###
![status.PNG](https://bitbucket.org/repo/LBGnXb/images/2460734211-status.PNG)

### Coverage ###
![coverage.PNG](https://bitbucket.org/repo/LBGnXb/images/908951404-coverage.PNG)

### Run the unit test ###
```shell
cd project_dir
nosetests
```

### Generate a coverage report ###
```shell
coverage run mailmerge_test.py
coverage report
coverage html
```