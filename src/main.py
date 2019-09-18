#!/usr/bin/python

import getpass
from os import path

# Main program
def main():
	print("[MAIN] Calling Data_Wrangling_CAP1...")
	import Data_Wrangling_CAP1
	print("[MAIN] Calling Exogenous_Variables...")
	import Exogenous_Variables

print("[MAIN] Running Rainfall Predictor as "+getpass.getuser()+" ...")
print("[MAIN] HOME (~)="+path.expanduser("~"))
print("[MAIN] ")
main()