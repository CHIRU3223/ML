import xlwt
from xlwt import Workbook 


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
        x=x+'\n'
        f.writelines(x)
        

f.close() 
  
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
f=open('demo.txt','r+')
read=f.readlines()
data=[]
j=0
k=0
for i in read:
    sheet1.write(0, k,k)
    sheet1.write(1, j, i)
    j+=1
    k+=1

wb.save('selex4.xls') 
f.close()