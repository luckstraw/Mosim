#!/bin/bash

python3 -m venv myenv

source myenv/bin/activate

# Install the required packages
# pip install numpy
# pip install scikit-learn+
# pip install matplotlib

python3 part_1.py
python3 part_2.py
python3 part_3.py
python3 part_4.py

deactivate