#!/bin/bash

python3 -m venv venv

source venv/bin/activate

# Install the required packages
# pip install simpy
# pip install pandas
# pip install matplotlib
# pip install seaborn

python3 EmergencySimulation.py

deactivate