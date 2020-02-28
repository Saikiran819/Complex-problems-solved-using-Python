# importing the multiprocessing module 
import multiprocessing 
import os 

def worker1(): 
	# printing process id
    print("ID of process running worker1: {}".format(os.getpid()))

def worker2(): 
    # printing process id
    print("ID of process running worker2: {}".format(os.getpid()))
    
if __name__ == "__main__":
	# printing main program process id 
	print("ID of main process: {}".format(os.getpid())) 

	# creating processes 
	p1 = multiprocessing.Process(target=worker1)
	p2 = multiprocessing.Process(target=worker2)

	# starting processes 
	p1.start()
	p2.start()

	# process IDs 
	print("ID of process p1: {}".format(p1.pid))
	print("ID of process p2: {}".format(p2.pid))

	# wait until processes are finished 
	p1.join() 
	p2.join() 

	# both processes finished 
	print("Both processes finished execution!") 

	# check if processes are alive 
	print("Process p1 is alive: {}".format(p1.is_alive())) 
	print("Process p2 is alive: {}".format(p2.is_alive())) 

"""
To prove that each process has independent memory space

"""

# empty list with global scope 
result = [] 

def square_list(mylist): 
	""" 
	function to square a given list 
	"""
	global result 
	# append squares of mylist to global list result 
	for num in mylist: 
		result.append(num * num) 
	# print global list result 
	print("Result(in process p1): {}".format(result)) 

if __name__ == "__main__":
	# input list 
	mylist = [1,2,3,4] 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list, args=(mylist,)) 
	# starting process 
	p1.start() 
	# wait until process is finished 
	p1.join() 

	# print global result list 
	print("Result(in main program): {}".format(result)) 

"""
Two different processes using shared memory, Here asn array and a value
"""

def square_list2(mylist2, result2, square_sum): 
	""" 
	function to square a given list 
	"""
	# append squares of mylist to result array 
	for idx, num in enumerate(mylist2): 
		result2[idx] = num * num 

	# square_sum value 
	square_sum.value = sum(result2) 

	# print result Array 
	print("Result(in process p1): {}".format(result2[:])) 

	# print square_sum Value 
	print("Sum of squares(in process p1): {}".format(square_sum.value)) 

	# input list 
	mylist2 = [1,2,3,4] 

	# creating Array of int data type with space for 4 integers 
	result2 = multiprocessing.Array('i', 4) 

	# creating Value of int data type 
	square_sum = multiprocessing.Value('i') 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list2, args=(mylist2, result2, square_sum)) 

	# starting process 
	p1.start() 

	# wait until process is finished 
	p1.join() 

	# print result array 
	print("Result(in main program): {}".format(result2[:])) 

	# print square_sum Value 
	print("Sum of squares(in main program): {}".format(square_sum.value)) 


