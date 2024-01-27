from multiprocessing import Queue

fruits=['apple','apricot','banana','mango','papaya']

queue=Queue()

count=0
print('insert item in queue using put()')
for f in fruits:
    print('item ',count,f)
    queue.put(f)
    count+=1
print()
count=0
print('get item in queue using get()')
while not queue.empty():
    got_fruit_by_queue=queue.get()
    print('item ',count,'',got_fruit_by_queue)
    count+=1

