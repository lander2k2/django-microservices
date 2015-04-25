#!/bin/bash

#VIRTUALENV="/Users/lander2k2/.virtualenvs/user_service"
#MANAGE="/Users/lander2k2/Projects/betfit/user_service"

VIRTUALENV="/Users/lander2k2/.virtualenvs/betfit_website"
MANAGE="/Users/lander2k2/Projects/betfit/website"

/bin/bash -c ". $VIRTUALENV/bin/activate; eval python $MANAGE/manage.py runserver"

