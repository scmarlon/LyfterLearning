def print_numbers_times_2(numbers_list):#O(1)
	for number in numbers_list:#O(n)
		print(number * 2)#O(1)

print_numbers_times_2#This function has O(n) in the forloop.

def check_if_lists_have_an_equal(list_a, list_b):#O(1)
	for element_a in list_a:#O(n)
		for element_b in list_b:#O(n^2)
			if element_a == element_b:#O(1)
				return True#O(1)
	return False#O(1)

check_if_lists_have_an_equal#This function has O(n) and O(n²) in the second forloop.

def print_10_or_less_elements(list_to_print):#O(1)
	list_len = len(list_to_print)#O(1)
	for index in range(min(list_len, 10)):#O(n)
		print(list_to_print[index])#O(1)

print_10_or_less_elements#This is a O(1) and O(n) function in the forloop.

def generate_list_trios(list_a, list_b, list_c):#O(1)
	result_list = []#O(1)
	for element_a in list_a:#O(n)
		for element_b in list_b:#O(n^2)
			for element_c in list_c:#O(n^3)
				result_list.append(f'{element_a} {element_b} {element_c}')#O(1)
				
	return result_list#0(1)

generate_list_trios#This function has O(n), O(n^2), and O(n^3) in the nested for loops.