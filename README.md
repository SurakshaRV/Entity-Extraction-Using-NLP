# Technical Chatbot

Objective of the project:
1. To develop a Named Entity Recognizer model to tag  technical words in the given pdf file using NLP.
2. To build a Technical Chatbot that answers technical questions related to the  uploaded PDF as well as answer generic queries asked by the user. 

Datasets used:
1. Aruba Clearpass Guides available at <a href=https://support.arubanetworks.com/Documentation/tabid/77/DMXModule/512/Default.aspx?EntryId=28161>Aruba Support Portal (ASP)</a> to train Spacy model to recognize technical words.


An NLP Model trained to do the following tasks.
1. Take the pdf file uploaded by the user
2. Scrape the text 
3. Tag the technical words as well as detect their versions
4. Create a knowledge base to store all the tagged words and their versions 
5. Answer user's queries.
