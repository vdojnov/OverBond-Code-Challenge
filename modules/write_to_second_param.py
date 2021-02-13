import csv
import sys

def write_to_second_param(output_obj, file_name): 
    # Turns the list in to a CSV file with the file name that was passed as the second parameter 
    with open(file_name, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(output_obj)