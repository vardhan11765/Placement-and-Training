'''f=open("vardhan.txt")
#print(f.readline())
#print(f.read())
#print(f.readline())
for i in f:
    print(i)

f.close()

'''
f = open("vardhan", "a")
f.write("Now the file has more content!")
f.close()



#open and read the file after the appending:
f = open("vardhan.txt", "r")
print(f.read())
