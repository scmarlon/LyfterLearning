#Bubble sort algorithm implementation
def bubble_sort(numbers_list):#O(1)

    print(f'\nList: {numbers_list} ')#O(1)

    #Loop through the list as many times as there are elements in the list
    for number_of_iterations in range(0,len(numbers_list) - 1):#O(n)

        #auxiliary variable to check if any numbers were switched in the current iteration
        counter_auxiliary = False#O(1)
        for index in range(0, len(numbers_list) - 1 - number_of_iterations):# O(n^2)

            #set the current index and the next index to compare
            current_value = numbers_list[index]#O(1)
            next_value = numbers_list[index + 1]#O(1)

            #check if the current index is greater than the next index, if so switch them
            if current_value > next_value:#O(1)
                numbers_list[index] = next_value#O(1)
                numbers_list[index + 1] = current_value#O(1)
                counter_auxiliary = True#O(1)
        if not counter_auxiliary:#O(1)
            return numbers_list#O(1)
    return numbers_list#O(1)

numbers_list = [2,1,3] #O(1)
bubble_sort(numbers_list) #This function has O(n) in the best case and O(n²) in the average and worst cases.

print(f'\nThe list has been sorted...\nFinal list: {numbers_list}') #O(1)