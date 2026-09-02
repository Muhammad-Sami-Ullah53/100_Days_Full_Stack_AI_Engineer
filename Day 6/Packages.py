# packages are just python files containing code
# 2 types of packages built-in and external
# some packages are used to extract data from websites, some for ai ml, some for data analytics and some for connect with APIs etc
# requests -> Make web requests
# openai -> use AI models
# pandas -> Work with data tables

import math  # import whole module
from math import sqrt, pi  # import specific items from a module

import os
current_dir=os.getcwd()  # Get current directory
print(f"Your current directory is {current_dir}")

import pandas as pd 

# Agr hm kisi project me koi external modules ko use kr rhy hein to us ki requirement he k pahly usy install kia jaye lkn hamy kisi ka project mila he orr hm dekhna chahy  to sb sy pahly us project ki requirements.txt bnaye gy ab ye kesy bnaye gy is k lye hm terminal me pip freeze > requirements.txt ko run karein gy
 