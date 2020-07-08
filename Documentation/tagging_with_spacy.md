### Documentation for tagging of technical words with Spacy and finding the tagged technologies' versions

**Method** : tagging()  
**Parameters** : Name of the pdf file uploaded by the user.  
**Returns** : None. This method opens the .txt file to which text extracted from the pdf file was written   
              and parses it to tag the technical words present in it. Then the tagged words are stored in the knowledge base (.csv file).   
              
**Method** : version_parser()  
**Parameters** : 1. txtfile: Name of the .txt file to which text extracted from the pdf file was written.  
                 2. referenceKB: Name of the the .csv file in which tagged entities were stored.
                 3. newKB: Name of the .csv file (Knowledge Base) in which tagged entities along with their versions are to be stored.   
**Returns** : This method parse the .txt file to find the versions of the tagged words present in referenceKB and stores both the   
              tagged words and their corresponding versions in newKB.
       
