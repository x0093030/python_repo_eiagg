'''
Created on Sep 16, 2024

@author: admin
'''
def is_leap_year(year):
    # Write your code here. 
    # Don't change the function name.
    leap_year_flag = True
    if year % 4 == 0:
        leap_year_flag = True
        if year % 100 == 0:
            #leap_year_flag = False
            if year % 400 == 0:
                leap_year_flag = True
                return leap_year_flag
            else:
                leap_year_flag = False
                return leap_year_flag
        else:
            leap_year_flag = True
            return leap_year_flag
    else:
        leap_year_flag = False
        return leap_year_flag
        
print(is_leap_year(2000))
print(is_leap_year(2400))
print(is_leap_year(1989))