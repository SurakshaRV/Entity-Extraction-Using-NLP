def ans_query(q, data):
    import csv
    import nltk
    import re
    import testing_for_generic
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    tech_words, versions=[],[] 
    file=data[:-4]
    file=file+"1.csv"
    q=q.lower()
    #q=testing_for_generic.main(q)
    with open(file) as f:
        reader = csv.reader((line.replace('\0','') for line in f), delimiter=",",skipinitialspace=True)
        for row in  reader:
            tech_words.append(row[0].lower())
            versions.append(row[1])
    if re.match( r'(is|are|does).*(support|supports|use|uses|implement|implements)?.*(technology|technologies|tech).*(supported|used|implemented)?.*',q):
        if tech_words:
            return 'Yes'
        else:
            return 'No technology is used'
    elif re.match( r'(has|is|does).*(used|use|implement|implemented|support|supports|uses|supported|implements).*', q):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(q)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(filtered_sentence)
        for w in filtered_sentence:
            if w in tech_words:
                return "Yes, "+ str(w)+" is supported."
        return "No, it is not supported."
    elif 'version' in q.split(' '):
        stop_words = set(stopwords.words('english'))
        word_tokens = word_tokenize(q)
        filtered_sentence = [w for w in word_tokens if not w in stop_words]
        print(filtered_sentence)
        for w in filtered_sentence:
            if w!='version' and w in tech_words:
                return versions[tech_words.index(w)]
        return False
    elif re.match( r'.*(technologies|tech|technology).*(use|uses|implement|implements|used|implemented|support|supports|supported).*',q):
        s=set(tech_words)
        stop_words = set(stopwords.words('english'))
        ans=""
        for i in s:
            if i not in stop_words or not i.isdigit():
                  ans+=i+", "
        ans=ans[:-2]+"."
        return "The technologies used are:"+ans
    else:
        return False
    
    


            
