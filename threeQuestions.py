def ans_query(q, data):
    import csv
    import nltk
    import re
    import testing_for_generic
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    tech_words, versions=[],[] 
    #getting the name of .csv file of the uploaded .pdf file
    file=data[:-4] 
    file=file+"1.csv"
    q=q.lower()
    #q=testing_for_generic.main(q)
    with open(file) as f:
        reader = csv.reader((line.replace('\0','') for line in f), delimiter=",",skipinitialspace=True)
        #creating a list of technical words and versions of those technologies
        for row in  reader:
            tech_words.append(row[0].lower())
            versions.append(row[1])
            
        #checking whether any technologies used in uploaded .pdf file  
    if re.match( r'(is|are|does).*(support|supports|use|uses|implement|implements)?.*(technology|technologies|tech).*(supported|used|implemented)?.*',q):
        if tech_words:
            return 'Yes'
        else:
            return 'No technology is used'
    #checking wheher the queried tech is used in uploaded .pdf file
    elif re.match( r'(has|is|does).*(used|use|implement|implemented|support|supports|uses|supported|implements).*', q):
        stop_words = set(stopwords.words('english')) #getting all the english stopwords
        word_tokens = word_tokenize(q) #tokenizing the user query
        filtered_sentence = [w for w in word_tokens if not w in stop_words] #filtering the tokenized query from stop words
        #checking if filtered sentence has any technical word
        for w in filtered_sentence:
            if w in tech_words:
                return "Yes, "+ str(w)+" is supported."
        return "No, it is not supported."
    #checking for the version of the queried technology
    elif 'version' in q.split(' '):
        stop_words = set(stopwords.words('english')) #getting all the english stopwords
        word_tokens = word_tokenize(q)#tokenizing the user query
        filtered_sentence = [w for w in word_tokens if not w in stop_words] #filtering the tokenized query from stop words
        #print(filtered_sentence)
        for w in filtered_sentence:
            if w!='version' and w in tech_words:
                return versions[tech_words.index(w)] #returning the version of the technical word
        return False
    #checking for all technologies used in the uploaded .pdf file
    elif re.match( r'.*(technologies|tech|technology).*(use|uses|implement|implements|used|implemented|support|supports|supported).*',q):
        s=set(tech_words) #removing the duplicates from tech_words list
        stop_words = set(stopwords.words('english')) #getting all the english stopwords
        ans=""
        #getting all the tech words
        for i in s:
            if i not in stop_words or not i.isdigit():
                  ans+=i+", "
        ans=ans[:-2]+"."
        return "The technologies used are:"+ans
    else:
        return False
    
    


            
