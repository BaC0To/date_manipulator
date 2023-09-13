"""The Fibonacci sequence is the series of numbers where each number is the sum of the two preceding numbers. For example,

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, …

Mathematically we can describe this as:

xn= xn-1 + xn-2

"""

def fibonacci(first_n_numbers):
    """Function that prints as list the first N-selected FIbonacci numbers
    param: First-N-numbers: int
    return: List of First-N-numbers :list
    """
    fibonacci_list = []
    first_num = 0
    second_num = 1
    
    i = 0
    
    while i < first_n_numbers:
        
        if i == 0:
            fibonacci_list.append(first_num)
        else:
            next_num = first_num + second_num
            fibonacci_list.append(next_num)
            first_num = second_num
            second_num = next_num

        i += 1

    return fibonacci_list

#just try:
first_n_numbers = 10
print(fibonacci(first_n_numbers))