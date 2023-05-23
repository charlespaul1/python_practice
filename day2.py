# checking if a year is leap using the gregorian calendar
def is_leap(year):
    # can evenly be divided by 4
    if year % 4 == 0:
        # can evenly be divided by 100
        if year % 100 == 0:
            # can evenly be divided by 400
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False
    
    
print(is_leap(2100))
                                            