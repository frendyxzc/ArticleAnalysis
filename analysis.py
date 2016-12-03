#!/usr/bin/python
import sys
import os

os.system("python extract_tags.py ./data/2869885.txt");
os.system("python extract_tags.py ./data/4634116.txt");

os.system("python chart/run.py ./result/2869885_tags ./result/4634116_tags");