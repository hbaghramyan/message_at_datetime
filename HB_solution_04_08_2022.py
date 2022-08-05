# importing necessary libraries
from functions import *

strd = "%d.%m.%Y" # string variable for date formate
strt = "%H:%M:%S" # string variable for time formate

# Run this cell to input number of entries
n = nentry()

# Run this cell to input time and date
dt = dtime(n, strd, strt)

# Run this cell to print time and date
print_dt(dt, strd, strt)
