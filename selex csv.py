import csv


f = open('monitor data.rtf','r+')  
lines = f.readlines()  # return a list of lines in file
list_of_elements = []
l=[]
count=0
bad_chars = ['%','/','-','\par']
for line in lines:
    list_of_elements += line.split(" ")
    # l +=line.split("\")
f.close()
f=open('demo.txt','w')
for x in list_of_elements:
    x=x.strip()
    if not(x.isalnum()) and x!="" and x not in bad_chars and "\par" not in x:
        print(x)
        count=count+1
        x=x+'\n'
        f.writelines(x)
        

f.close() 
values=[]
keys=[]
f=open('demo.txt','r+')
read=f.readlines()
for i in range(count):
 	keys.append(i)
for i in read:
    i=i[:-1]
    values.append(i)
filename ="results111.csv"
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(keys)  
        
    # writing the data rows  
    csvwriter.writerow(values) 
print(values)
f.close()