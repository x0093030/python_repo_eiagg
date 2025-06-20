def is_leap(year):
    leap = False
    
    # Write your logic here
    if year in range(1900,100001):
        #if year%4==0 and (year%100==0 and year%400==0):
        if (year%4==0 and (year%100!=0)) or year%400==0:
            #print("leap year")
            leap = True
            return leap
        else:
            #print("NOT leap year")
            return leap

year = int(input())