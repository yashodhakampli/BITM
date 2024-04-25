# 1 Python Program to Map Two Lists into a Dictionary

# 2 Python Program to Check if a Key Exists in a Dictionary or Not

# 3 print first letter of key basis using dictionary

# 4 Python Program to Count the Frequency of Each Word in a String using Dictionary

'''
Case 1:
Enter string:hello world program world test
{'test': 1, 'world': 2, 'program': 1, 'hello': 1}
 
Case 2:
Enter string:orange banana apple apple orange pineapple
{'orange': 2, 'pineapple': 1, 'banana': 1, 'apple': 2}

'''

#-----------------------
'''
keys=[]
values=[]
n=int(input("Enter number of elements for dictionary:"))
print("For keys:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    keys.append(element)
print("For values:")
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    values.append(element)
d=dict(zip(keys,values))
print("The dictionary is:")
print(d)
'''
#-------------------------------

d={'A':1,'B':2,'C':3}
key=input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")
      
      #------------------
'''      
my_dict = {'apple': 10, 'banana': 20, 'angel': 30, 'BALAJI': 40,'chennai':100,'zebra':120}

for key, value in my_dict.items():
    if key[2].lower() == 'l':
        print(f"The value of '{key}' is {value}")
'''        
        
#----------------------------





'''      
test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(zip(l,wordfreq))
print(dict(zip(l,wordfreq)))
'''

'''
a=[1,2,3]
b=['a','b','c']
res=dict(zip(a,b))
print(res)
'''
