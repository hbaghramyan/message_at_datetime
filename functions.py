# importing necessary libraries
from datetime import datetime
from time import sleep

def nentry():
    """number of entries function"""
    n = input("How much data do you want to enter?: ")
    if (not(n.isdigit()) or n <= '0'): # checking if an input is a natural number
        print("Please enter a natural number.")
    else:
        return int(n)
    
def validate(dt, dtformat):
    """a function to validate date formate"""
    try:  
        if dt != datetime.strptime(dt, dtformat).strftime(dtformat):
            raise ValueError
        return True
    except ValueError:
        return False

def dtime(n, strd, strt):
    """a function for the user to enter time and date"""
    dt = []
    for i in range(n):
        date = input("Please enter a date in DD.MM.YYYY format:")
        if not(validate(date, strd)):
            print("Please enter a date in the correct format.")
            continue
        time = input("Please enter a time in HH:MM:SS format:")
        if not(validate(time, strt)):
            print("Please enter a time in the correct format.")
            continue
        else:
            item = datetime.strptime(str(time+" "+date), strt+" "+strd)
            if item < datetime.strptime(datetime.now().strftime(strt+" "+strd), strt+" "+strd):
                print("Please enter a time and date not in the past.")
            else:
                dt.append(item)
    comb_dt = []
    if dt:
        print("Thank you very much. I will notify them!")
        print(f"You've entered {len(dt)} correct datetimes:")
        for i in dt:
            print(i.strftime(strt+" "+strd))
            comb_dt.append(i)
    else:
        print(f"You've entered {len(dt)} correct datetimes.")
    comb_dt = sorted(comb_dt)
    return comb_dt

def print_dt(dt, strd, strt):
    """simple message to be displayed at the inserted time"""
    if dt:    
        for i in range(len(dt)):
            while datetime.strptime(datetime.now().strftime(strt+" "+strd), strt+" "+strd) < dt[i]:
                sleep(2)
            print("The datetime ", dt[i].strftime(strt+" "+strd), "has been reached.")
    else:
        print("No message to display.")