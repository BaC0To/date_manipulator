from datetime import datetime, timedelta
import re

def offset_date_with_days(offset_days:int) -> str:
    """Function that recalculates date with desired +- days offset
    params: offset_days:int
    return: date:str
    """

    return str((datetime.now() + timedelta(offset_days)).date())

def is_date_iso_format(input_date) -> bool:
    """ISO Format date validator
    params: input_date : datetime.date
    return: bool
    """

    if (re.fullmatch("\d{4}-\d{2}-\d{2}", input_date)):
        print(f"Date is : {input_date} and is correctly IS0 formatted like: YYYY-MM-DD")
        return True

    else:

        print(f"Date is : {input_date} and is incorrectly formatted.")
        return False

def is_date_correct(input_date) -> bool:
    """Correct Date Check
     params: input_date : any
    return: bool"""

    date_correct_status = False
    yy, mm , dd = str(input_date).split('-')
    dd = int(dd)
    mm = int(mm)
    yy = int(yy)
    if(mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
        max1 = 31
    elif(mm == 4 or mm == 6 or mm == 9 or mm == 11):
        max1 = 30
    elif(yy % 4 == 0 and yy % 100 != 0 or yy % 400 == 0):
        max1 = 29
    else:
        max1 = 28
    if(mm < 1 or mm > 12):
        print(f"Date {input_date} is invalid.")
        date_correct_status = False
    elif(dd < 1 or dd > max1):
        print(f"Date {input_date} is invalid.")
        date_correct_status = False
    else:
        print(f"Date {input_date} is valid.")
        date_correct_status = True
        
    
    return date_correct_status

