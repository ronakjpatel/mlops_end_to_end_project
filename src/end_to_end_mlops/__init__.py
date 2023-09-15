
'''
-------------- Information about this file ------------------------
This file will be run first whenever we build the whole application as a package (setup.py). This is true for all __init__.py 
contained inside the sub directories as well. 

Secondly, we can simple import the function of variable by simply using "import <name>" is other modules.
For example, let's say of we want to import the logger in main.py file then we simple write "from end_to_end_mlops import logger"
"end_to_end_mlops" is a project name here. 
 
Whenever we log information from any module it will save the log inside log/running_log.log file

---------------------------------------------------------------------
'''


import os
import sys
import logging

#This is the the sentence structure of the log it is going to save in loig file. 
#first time then module level and module name and the message 
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

#Giving the directory name in which the logs are going to be saved
log_dir = "logs"

log_filepath = os.path.join(log_dir,"running_log.log")

os.makedirs(log_dir,exist_ok=True)

#This will setup the initial logger that we will use throughout the project. 
logging.basicConfig( level=logging.INFO,
                    format=logging_str,
                    handlers=[logging.FileHandler(log_filepath),
                              logging.StreamHandler(sys.stdout)
                              ]
    
)

#Getting the logger object
logger = logging.getLogger("mlProjectLogger")