import csv

words=[]
tech_words=[]
versions=[]
file='kb - Sheet1.csv'.encode("utf-8")

with open(file, 'r') as csvfile:
    reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter=",",skipinitialspace=True)
    for row in reader:
        words.extend(row)
#print(words)
txtfile=input("Enter file name: ")
with open(txtfile,'r') as f:
    content=f.read().split()
for i in range(len(content)):
    if content[i] in words:
        tech_words.append(content[i])
        for n in content[i+1].split('.'):
            if n in ['0','1','2','3','4','5','6','7','8','9']:
                versions.append(content[i+1])
                break
            elif content[i+1]=='ver' or content[i+1]=='version':
                versions.append(content[i+2])
                break
            else:
                versions.append('NA')
                break
        #print(tech_words)

def ans_query(q):
    if q.lower()=="are there any technologies used":
        if tech_words:
            print('Yes')
        else:
            print('No technology is used')
    elif q.lower()=="what are the technologies used":
        print(tech_words)
    else:
        for i in range(len(versions)):
            print(tech_words[i]," - ", versions[i])

choice=1
while choice:
    query=input("Ask me anything: ")
    ans_query(query)
    choice=int(input("have more questions? [yes=1|no=0]"))
