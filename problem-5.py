

def is_leap(year):
    leap = False

    if year%400 == 0 :
        return True
    
    elif year%100 == 0 :
        return leap
    
    elif year%4 == 0 :
        return True
 
    else:   
       return leap

#is_leap (year = int(input()))
year = int(input())
is_leap (year)
print(is_leap(year))