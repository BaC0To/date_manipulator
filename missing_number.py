
def find_missing_number_in_array(input_array, lower_limit:int, upper_limit:int):
    """Function to find the missing number in a given array within lower and upper limits
    params: input_array, lower_limit, upper_limit
    return: missing_number: int"""
    missing_numbers = []

    for item in range(lower_limit, upper_limit+1, 1):
        if item in sorted(input_array):
            pass
        else:
            missing_numbers.append(item)

    #string.strip(characters)
    missing_numbers_str = str(missing_numbers).strip("[]")
    print(f"Missing number in the said array ({lower_limit}-{upper_limit}): {missing_numbers_str}")
    return int(missing_numbers_str)




array = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
u_limit = 20
l_limit = 10
array2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

find_missing_number_in_array(array,l_limit, u_limit)