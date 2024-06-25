import json
import os
import sys
import subprocess
import dotenv

## I guess there's lusers on Wintendo still? Do we need to accomodate for the mentally retarded?
def checkForTask():
	try:
		subprocess.run(['taska', '>', '/dev/null', '2>&1'], stderr=subprocess.DEVNULL).returncode
	except Exception as e:
		sys.stderr.write('Cannot find TaskWarrior! Is it in your path?')




checkForTask()