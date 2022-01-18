#!/bin/bash

python detect.py --weights .\\runs\\train\\exp\\weights\\best.pt --source $* --save-txt
