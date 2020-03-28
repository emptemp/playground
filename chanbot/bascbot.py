import basc_py4chan

#do=0
#print ("1 - scan; 2 - sort")
#do = raw_input()
catalog=[]

#if do:
b = basc_py4chan.Board('b')
all_thread_ids = b.get_all_thread_ids()
count = 0
file = open("4chan.txt", "w")
str_all_thread_ids = [str(id) for id in all_thread_ids]
for str_all_thread_ids in str_all_thread_ids:	
	count += 1
	if b.thread_exists(str_all_thread_ids):
		thread = b.get_thread(str_all_thread_ids)
		thread_id = str(str_all_thread_ids)
		replies = str(len(thread.replies))
		topic = thread.topic
		print count	
		int_rpy = int(replies)
		catalog.append([thread_id,int_rpy])
		file.write(thread_id)
		file.write("\t") 
		file.write(replies)
		file.write("\t")
		file.write((topic.comment).encode('utf-8'))
		file.write("\n")
			
file.close()

hot=sorted(catalog, key=lambda thread: thread[1], reverse=True)

for n in range(0,len(catalog)):
	print catalog[n]

f = open("hot.txt","w")
for n in range(0,len(hot)):
	thread = hot[n]
	print (hot[n])
	print (" ")
	f.write(thread[0])
	f.write("\n")
f.close()
