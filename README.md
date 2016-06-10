![Travis CI Build](https://travis-ci.org/arvinwiyono/mail-merge.svg?branch=master)
# FIT4004 Assignment 3 - Automated Unit Testing #
![Python](http://s33.postimg.org/wcj9d0t0v/python_snake.png)

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
coverage run --branch mailmerge_test.py
coverage report
```
Coverage **statement-cov.zip** and **branch-cov.zip** are downloadable from the archived artifacts in the Drone.io CI
