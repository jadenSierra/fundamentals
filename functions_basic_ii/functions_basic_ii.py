
#CountDown
def count_down(num):
    c_down = []
    for int in range(num,0,-1):
        c_down.append(int)
    return c_down

print(count_down(5))


# Print and Return 

def print_and_return(list):
    print(list[0])
    return list[1]

print(print_and_return([1,2]))

# First plus length 

def first_plus_length(list):
    return list[0] + len(list)

print(first_plus_length([1,2,3,4,5]))

# Values greater than second

def values_greater_than_second(list):
    new_list = []

    if len(list) < 2:
        return False
    
    for int in range(0,len(list)):
        if list[int] > list[1]:
            new_list.append(list[int])
    print(len(new_list))
    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# This length, that value

def this_length_that_value(size,val):
    new_list = []
    for i in range(0,size):
        new_list.append(val)
    return new_list

print(this_length_that_value(4,7))
print(this_length_that_value(6,2))
