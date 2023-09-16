# Problem 3:  Biggest and smallest number in an array
#  Write a program to print the biggest and smallest number in the array. 

def find_max_min(array):

    max_number = array[0]  
    min_number = array[0]  
    
    for n in array:
        if n > max_number:
            max_number = n
        elif n < min_number:
            min_number = n
    
    return max_number, min_number

# Example usage:
my_array = [12, 43, 28, 94, 76, 61]
max_number, min_number = find_max_min(my_array)

print(f"Maximum is: {max_number}")
print(f"Minimum is: {min_number}")
