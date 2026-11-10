# Bubble sort algorithm starts from the last right index of the list and compares it with the previous index, to sort the list...
def bubble_sort_invert(numbers_list):
    print(f'Initial list: {numbers_list}\n')
    #Loop through the list as many times as there are elements in the list
    for number_of_iterations in range(0,len(numbers_list) - 1):
        counter_auxiliary = False
        #Loop through the list from the last index to the first index, comparing each index with the previous index
        for index in range(len(numbers_list) -1, number_of_iterations, - 1 ):

            current_value = numbers_list[index]
            previous_value = numbers_list[index - 1]
            print(f'current index: {current_value}, previous index: {previous_value}')
            #check if the current index is less than the previous index, if so switch them
            if current_value < previous_value:
                numbers_list[index] = previous_value
                numbers_list[index - 1] = current_value
                counter_auxiliary = True
                print(f'switching numbers....')
            print(f'current list..... modified: {numbers_list} \n')
        #check if any numbers were switched in the current iteration, if not, the list is sorted and we can return it
        if not counter_auxiliary:
            return numbers_list
        
    return numbers_list 

numbers_list = [5, 2, 1, 3, 4]
bubble_sort_invert(numbers_list)

print(f'\nThe list has been sorted...\nFinal list: {numbers_list}')