def print_numbers_times_2(numbers_list):#O(1)
	for number in numbers_list:#O(n)
		print(number * 2)#O(1)

print_numbers_times_2#This function has O(n) in the forloop.

def check_if_lists_have_an_equal(list_a, list_b):#O(1)
	for element_a in list_a:#O(n) => O(n_a) where n_a is the size of list_a
		for element_b in list_b:#O(n^2) => O(n_a * n_b) where n_b is the size of list_b
			if element_a == element_b:#O(1)
				return True#O(1)
	return False#O(1)
check_if_lists_have_an_equal#If we don't know the size of the lists, n_a = size de list_a. n_b = size de list_b... soo the worst-case O(n_a * n_b). If both lists have the same size n, then O(n^2).
                            #The best case is when the first element of list_a is equal to the first element of list_b, then O(1).

def print_10_or_less_elements(list_to_print):#O(1)
	list_len = len(list_to_print)#O(1)
	for index in range(min(list_len, 10)):#O(1)
		print(list_to_print[index])#O(1)

print_10_or_less_elements#This is a O(1) function, only print a maximum of 10 elements, regardless of the size of the list.

def generate_list_trios(list_a, list_b, list_c):#O(1)
	result_list = []#O(1)
	for element_a in list_a:#O(n) => O(n_a)
		for element_b in list_b:#O(n^2) => O(n_a * n_b)
			for element_c in list_c:#O(n^3) => O(n_a * n_b * n_c)
				result_list.append(f'{element_a} {element_b} {element_c}')#O(1)
	return result_list#0(1)

generate_list_trios #This function Worst-case time complexity: O(n_a * n_b * n_c). It happens If all three lists have the same size n, then O(n^3).
					#Example: list_a = [1,2,3], list_b = [4,5,6], list_c = [7,8,9]. Result, the last for loop will run 27 times, which is O(n^3)...