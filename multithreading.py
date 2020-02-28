import threading as thd
import time
import requests
import os

def func():
    print("Started the thread {}\n".format(thd.current_thread().name))
    time.sleep(2)
    print("Ended the thread {}\n".format(thd.current_thread().name))

threads = []

for i in range(10):
    threads.append(thd.Thread(target = func, name = "t"+str(i+1)))
    threads[i].start()
    
for j in range(10):
    threads[i].join()

# global variable x 
x = 0

def increment(): 
	""" 
	function to increment global variable x 
	"""
	global x 
	x += 1

def thread_task(): 
	""" 
	task for thread 
	calls increment function 100000 times. 
	"""
	for _ in range(100000): 
		increment() 

def main_task(): 
	global x 
	# setting global variable x as 0 
	x = 0

	# creating threads 
	t1 = thd.Thread(target=thread_task) 
	t2 = thd.Thread(target=thread_task) 

	# start threads 
	t1.start() 
	t2.start() 

	# wait until threads finish their job 
	t1.join() 
	t2.join() 

for i in range(10): 
	main_task() 
	print("Iteration {0}: x = {1}".format(i,x))

# global variable x 
y = 0

def increment2(): 
	""" 
	function to increment global variable x 
	"""
	global y 
	y += 1

def thread_task2(lock): 
	""" 
	task for thread 
	calls increment function 100000 times. 
	"""
	for _ in range(100000): 
		lock.acquire() 
		increment2() 
		lock.release() 

def main_task2(): 
	global y
	# setting global variable x as 0 
	y = 0

	# creating a lock 
	lock = thd.Lock() 

	# creating threads 
	t1 = thd.Thread(target=thread_task2, args=(lock,)) 
	t2 = thd.Thread(target=thread_task2, args=(lock,)) 

	# start threads 
	t1.start() 
	t2.start()

	# wait until threads finish their job
	t1.join()
	t2.join()

for i in range(10): 
	main_task2() 
	print("Iteration {0}: y = {1}".format(i,y)) 

"""
Downloading images parallelly using multithreading

"""


img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]


def download_images(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]+'.jpg'
    dirPath = os.path.dirname(os.path.realpath('__file__'))
    img_name = os.path.join(dirPath, 'Images\\'+img_name)
    with open(img_name, 'wb') as f:
        f.write(img_bytes)
        print('{} is downloaded\n'.format(img_name))
        
        
t1 = time.perf_counter()

t = []
for img in img_urls:
    tn = thd.Thread(target = download_images, args = (img,))
    t.append(tn)
    tn.start()
for tn in t:
    tn.join()

t2 = time.perf_counter()

print('Finished in {} second(s)'.format(t2-t1))
        
