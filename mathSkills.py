import sys
from statistics import mean, median, pvariance, pstdev
from math import floor
if len(sys.argv) != 2: # validate input
    print("Wrong input - refer to README.md")
    exit()
input = sys.argv[1]
error_to_catch = getattr(__builtins__,'FileNotFoundError', IOError)
try:
    file = open(input, "r")
except error_to_catch:  # validate file availability
    print("File Not Found - refer to README.md")
    exit()
fileData = []
for num in file:
    if num.strip().isnumeric(): # ensure removal of white spaces or carriage return then validate data type
        fileData.append(int(num)) 
    else:
        print("Invalid data - refer to README.md")
        exit()
file.close()
if len(fileData) == 0: # validate data availability
    print("Empty File - refer to README.md")
    exit()
def roundUp(x) -> int: # to avoid statisitical rounding (when at .5, rounds to the next even integer)
    return floor(x + 0.5)
print("Average: ", roundUp(mean(fileData)))
print("Median: ", roundUp(median(fileData)))
print("Median: ", roundUp(pvariance(fileData)))
print("Median: ", roundUp(pstdev(fileData)))