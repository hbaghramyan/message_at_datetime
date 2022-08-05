#### TESTS FOR NENTRY FUNCTION 

n = nentry()  
How much data do you want to enter?:  -5  
Please enter a natural number.  

n = nentry()  
How much data do you want to enter?:  a  
Please enter a natural number.  

n = nentry() 
How much data do you want to enter?:  6 

n = nentry() 
How much data do you want to enter?:  0 
Please enter a natural number. 

#### TESTS FOR VALIDATE FUNCTION 

validate("23:10:55", strt) 
True 
validate("23:10:5", strt) 
False 
validate("23:10:55", strd) 
False 
validate("04.08.2022", strd) 
True 
validate("04.08.202", strd) 
False 
validate("04.08.202", strt) 
False 


#### TESTS FOR DTIME FUNCTION 

dtime(n, strd, strt) 
Please enter a date in DD.MM.YYYY format: 04.08.2022 
Please enter a time in HH:MM:SS format: 12:12:12 
Please enter a time and date not in the past. 
Please enter a date in DD.MM.YYYY format: 04.08.2022 
Please enter a time in HH:MM:SS format: 23:1:12 
Please enter a time in the correct format. 
You've entered 0 correct datetimes. 
[] 


dtime(n, strd, strt) 
Please enter a date in DD.MM.YYYY format: 03.08.2022 
Please enter a time in HH:MM:SS format: 12:12:12 
Please enter a time and date not in the past. 
Please enter a date in DD.MM.YYYY format: 04.08.2022 
Please enter a time in HH:MM:SS format: 23:50:12 
Thank you very much. I will notify them! 
You've entered 1 correct datetimes: 
23:50:12 04.08.2022 
[datetime.datetime(2022, 8, 4, 23, 50, 12)] 

#### TESTS FOR THE OVERALL PERFORMANCE OF THE PROGRAM 

How much data do you want to enter?: 3 
Please enter a date in DD.MM.YYYY format:05.08.2022 
Please enter a time in HH:MM:SS format:15:31:35 
Please enter a date in DD.MM.YYYY format:05.08.2022 
Please enter a time in HH:MM:SS format:15:31:48 
Please enter a date in DD.MM.YYYY format:05.08.2022 
Please enter a time in HH:MM:SS format:15:32:00 
Thank you very much. I will notify them! 
You've entered 3 correct datetimes: 
15:31:35 05.08.2022 
15:31:48 05.08.2022 
15:32:00 05.08.2022 
The datetime  15:31:35 05.08.2022 has been reached. 
The datetime  15:31:48 05.08.2022 has been reached. 
The datetime  15:32:00 05.08.2022 has been reached. 

How much data do you want to enter?: 4 

Please enter a date in DD.MM.YYYY format:05.08.2022 

Please enter a time in HH:MM:SS format:3:36;15 

Please enter a time in the correct format. 

Please enter a date in DD.MM.YYYY format:05.08.2022 

Please enter a time in HH:MM:SS format:15:36:15 

Please enter a date in DD.MM.YYYY format:05.08.2022 

Please enter a time in HH:MM:SS format:15:35:45 

Please enter a date in DD.MM.YYYY format:05.08.2022 

Please enter a time in HH:MM:SS format:15:35:20 

Thank you very much. I will notify them! 

You've entered 3 correct datetimes: 

15:36:15 05.08.2022 

15:35:45 05.08.2022 

15:35:20 05.08.2022 

The datetime  15:35:20 05.08.2022 has been reached. 

The datetime  15:35:45 05.08.2022 has been reached. 

The datetime  15:36:15 05.08.2022 has been reached. 

