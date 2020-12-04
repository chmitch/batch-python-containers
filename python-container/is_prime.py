#!/usr/bin/env python
import argparse
from math import sqrt
from itertools import count, islice
import numpy as np
import pandas as pd


# Python program to check if the input number is prime or not
def is_prime(n):

	return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

def read_val_from_file(file):

	df = pd.read_csv(file)
	#We're expecting a file with one row and one column with a header row calling the cell "Number"
	return df['Number'].values[0]	

if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument("file", help="url to the source data file",
		type=str)
	
	##We're expecting a valid url as an input pointing to a file to process
	args = parser.parse_args()
	num = read_val_from_file(args.file)
	
	if is_prime(num):
		print('The number: {} is prime'.format(num))
	else:
		print('The number: {} is not prime'.format(num))