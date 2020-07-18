f = open('monitor data.rtf','r+')  
lines = f.readlines()  # return a list of lines in file
list_of_elements = []
l=[]
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
        f.writelines(x)
f.close()
        



