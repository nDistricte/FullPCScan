# FullPCScan

## Overview
The project is a Python-based utility designed to retrieve indicators that could tell the observer if the user could be cheating or not. We check files for certain names if the malicious user does not care about hiding the cheats. In most cases, people use USB drives to initialize their cheats and then unplug the USB drive while starting the game. Therefore, we are currently retrieving data on when the USB drive was inserted and unplugged from the PC. Additionally, we return most of the processes that were running before executing the CoD.exe.

## Requirments
Python 3.6 or higher
pip install psutil pywin32 --> pywin32 should usually be installed by running the scan file

## Usage
There are 2 options:
1. python scan.py
2. executing the scan.exe file from the dist directory
