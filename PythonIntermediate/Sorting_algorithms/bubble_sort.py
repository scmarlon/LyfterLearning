
def bubble_sort(numbers_list):
    #Loop through the list as many times as there are elements in the list
    for number_of_iterations in range(0,len(numbers_list) - 1):
        #auxiliary variable to check if any numbers were switched in the current iteration
        counter_auxiliary = False
        for index in range(0, len(numbers_list) - 1 - number_of_iterations):
            print(f'current list: {numbers_list} \n')
            #set the current index and the next index to compare
            current_value = numbers_list[index]
            next_value = numbers_list[index + 1]

            print(f'current number: {current_value}, next number: {next_value}')
            #check if the current index is greater than the next index, if so switch them
            if current_value > next_value:
                numbers_list[index] = next_value
                numbers_list[index + 1] = current_value
                print(f'switching numbers....')
                counter_auxiliary = True

        if not counter_auxiliary:
            return numbers_list
    return numbers_list
numbers_list = [2,1,3]
bubble_sort(numbers_list)

print(f'\nThe list has been sorted...\nFinal list: {numbers_list}')