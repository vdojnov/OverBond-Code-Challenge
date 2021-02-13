import csv
from csv import reader
import sys

def read_file():
    # read csv passes as a parameter in the cli as a list of lists
    with open(sys.argv[1], 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj)
        # Pass reader object to list() to get a list of lists
        input_data = list(csv_reader)   

    return input_data
