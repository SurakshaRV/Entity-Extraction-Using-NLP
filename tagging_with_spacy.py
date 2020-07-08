import spacy
import csv
import nltk
from nltk.corpus import stopwords

#################### version parser ########################################
def version_parser(txtfile,referenceKB,newKb):
    import re
    import csv

    words=[]
    tech_words=[]
    versions=[]

    with open(txtfile,'r') as f: #Give the txt file which contains text extracted from pdf file here for finding versions
        content1=f.read() # read the file
        content=content1.split(' ') # make a list of words from the read text
        for i in range(len(content)):
            # split the words joined by '\n'
            if '\n' in content[i]:
                l=content[i].split('\n')
                for w in l:
                    # insert the word to the words list only if it's not digit
                    if not w.isdigit():
                        content.insert(i,w)

    file=referenceKB.encode("utf-8") # referenceKB is the csv file that contains tagged words
    with open(file, 'r') as csvfile: # read and store the tagged technologies in 'words' list to find their versions later.
        reader = csv.reader((line.replace('\0','') for line in csvfile), delimiter=",",skipinitialspace=True)
        for row in reader:
            words.extend(row)

    content_words=[]
    content_words1=content1.split(' ')
    for i in content_words1:
        content_words.extend(i.split('\n'))

    with open(newKb,'w', newline='') as csv_file: # open the csv file(knowledge base) to store technologies and their versions.
        writer = csv.writer(csv_file, delimiter=',')
        for i in range(len(content_words)): # iterate thru the words in the words list 
            if content_words[i] in words: #check if the word is in the list of tagged words. if present, find it's version
                tech_words.append(content_words[i])
                for n in content_words[i+1].split('.'): 
                    #split the word right next to tagged word (since generally version is in the format 'x.x.x')
                    # make sure it's not of the form 'x.x.x.x' (ex: IP address) 
                    if re.match('v\d((\.\d)*|(\.[a-zA-Z]))',content_words[i+1].lower()): # check if it's in the format v1 or v2.3 or v3.4.5 etc
                        versions.append(content_words[i+1])
                        writer.writerow((content_words[i],content_words[i+1]))
                        break
                    # check for the format: 'python ver 3.7.4' and 'python version 2.7.5'
                    elif (content_words[i+1].lower()=='ver' or content_words[i+1].lower()=='version') and any(content_words[i+2].split('.')) in ['0','1','2','3','4','5','6','7','8','9']:
                        versions.append(content_words[i+2])
                        writer.writerow((content_words[i],content_words[i+2]))
                        break
                    # check if any of the char of the word is digit, and make sure it doesn't end with '.' 
                    elif n in ['0','1','2','3','4','5','6','7','8','9'] and content_words[i+1][-1]!='.' :
                        versions.append(content_words[i+1])
                        writer.writerow((content_words[i],content_words[i+1]))
                        break
                    else: # if none of the above formats is found, then add the version as 'NA'
                        versions.append('NA')
                        writer.writerow((content_words[i],"NA"))
                        break
    return tech_words, versions

def tagging(data):
    prdnlp = spacy.load("FINAL") #  the trained spacy model was named as 'FINAL'
    txtfile='{}'.format(data.replace('pdf','txt'))
    with open(txtfile,'r') as f: #Give the text extracted file here for tagging
        content1=f.read()
        content1=content1.replace("\n"," ").replace("/"," ").replace(","," ").replace(":"," ")
        content=content1.split()
        for i in range(len(content)): 
            if '\n' in content[i]: ## split the words joined by '\n'
                l=content[i].split('\n')
                for w in l:
                    if not w.isdigit():
                        content.insert(i,w)
                        
    # pass the read text to spacy model for tagging
    doc = prdnlp(content1[:1000000]) # spacy has a limitation : only string with no more than 1 million characters should be passed
    
    # grab only the text of the entities tagged
    items = [x.text for x in doc.ents]

    # Update KB with new words
    new_words=set(items)#[w for w in items if not w in words] # words tagged by spacy which are not there in the KB
    referenceKB='{}'.format(data.replace('pdf','csv'))
    with open(referenceKB,'w', newline='') as file:
        writer=csv.writer(file)
        for w in new_words:
            if len(w)>1:
                if not w[0].isdigit():
                    writer.writerow([w])

    newKB=data[:-4]
    newKB=newKB+"1.csv"

    version_parser(txtfile,referenceKB,newKB)
