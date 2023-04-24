#!/usr/bin/env bash

#create virtual environment
python3 -m venv tensorflow_env

source ./tensorflow_env/bin/activate

#then install requirements.txt
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

#deactivate the venv
deactivate