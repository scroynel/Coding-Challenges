'''

Write a Friday 13th detector

Create a function in Python that accepts two parameters. They’ll both be numbers. 
The first will be the month as a number, and the second will be the four-digit year. 
The function should parse the parameters and return True if the month contains a 
Friday the 13th and False if it doesn’t.

'''
import datetime as dt

def friday13_detector(year):
    day = 13
    friday13 = []
    
    for month in range(1, 13):
        data = dt.date(year, month, day)
        if data.weekday()== 4:
            friday13.append(f"{data.strftime('%d %B')}")
    
    return '\n'.join(friday13)
            
  
print(friday13_detector(2024))