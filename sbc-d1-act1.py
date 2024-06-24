'''from random import choice 
import time

choices = ["ZEVEL", 
           "AIRON", 
           "JED", 
           "SHMN", 
           "ACE",
           "ALDRAIN", 
           "JHOREN", 
           "ALVIN"]

for i in range (1,6):
    print(i)
    time.sleep(1)
   
print(choice(choices))
'''
'''
t = (1,2,3,4,5,0)#tuple
l = [1,2,3,4,5,0] #list
#    0 1 2 3 4

l[5] = 6
t[5] = 6
l.append(7)
t.append()
print(l)
print(t)
'''
'''
l = [5,4,7,1,2]
 
#l.append(3)
#print(l)
l.insert(1,6)
print(l)
'''
'''
l = [5,4,7,1,2]
l.remove(1) # 5472
l.pop(-3)#572

print(l)
'''
l = [5,4,7,1,2]
l.reverse()
print(l)
