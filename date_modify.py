from datetime import datetime, timedelta
import re


def offset_date_with_days(offset_days:int) -> str:
    """Function that recalculates date with desired +- days offset
    params: offset_days:int
    return: date:str
    """

    current_date = datetime.today().strftime("%Y-%m-%d")
   #print(f"Current date: {current_date}")

    new_date = (datetime.now() + timedelta(offset_days)).date()

    """ if offset_days > 0:
        print(f"New date with desired delta days= +{offset_days}: {new_date}")
    elif offset_days <= 0:
        print(f"New date with desired delta days= {offset_days}: {new_date}")
    else:
        pass """

    return str(new_date)

def is_date_iso_format(input_date) -> bool:
    """ISO Format date validator
    params: input_date : datetime.date
    return: bool
    """

    if (re.fullmatch("\d{4}-\d{2}-\d{2}", input_date)):
            print(f"Modified date is : {input_date} and is correctly IS0 formatted like: YYYY-MM-DD")
            return True
    else:
         return False



#is_date_iso_format(offset_date_with_days(+2))
