
def find_missing_number_in_array(input_array:list)-> int:
    """Function to find the missing number in a given array within lower and upper limits
    params: input_array, lower_limit, upper_limit
    return: missing_number: int"""
    
    for item in range(10, 21):
        if item not in sorted(input_array):
            return item
   


dummy_array = [10, 11, 12, 13, 14, 16, 17, 18, 19, 20]
dummy_array2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

print(find_missing_number_in_array(dummy_array2))