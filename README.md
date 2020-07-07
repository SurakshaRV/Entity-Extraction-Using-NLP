# Technical Chatbot

Objectives of the project :rocket:
--------------------------------------
1. To develop a Named Entity Recognizer model to **tag  technical words** in the given pdf file using **NLP**.
2. To build a Technical Chatbot that **answers technical questions** related to the  uploaded PDF as well as answer generic queries asked by the user. 

Architecture/Design:
------------------------------------------------------------------------------------------------------------------------------------------
![architecture](https://github.com/SurakshaRV/Entity-Extraction-Using-NLP/blob/master/arch.PNG)

Installation and Usage:
-------------------------
The requirements.txt in the repository defines the packages that are installed when building this project. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install them.

```bash
# Clone this repository
$ git clone https://github.com/SurakshaRV/Entity-Extraction-Using-NLP

# Go into the repository
$ cd Entity-Extraction-Using-NLP

# Install dependencies
$ pip install -r requirements.txt 

# Run the app
$ python upload.py
```

Summary :
----------------------
This is an NLP Model trained to do the following tasks.
1. Take the pdf file uploaded by the user
2. Scrape the text 
3. Tag the technical words as well as detect their versions
4. Create a knowledge base to store all the tagged words and their versions 
5. Answer user's queries.

# For more information read the <a href='https://github.com/SurakshaRV/Entity-Extraction-Using-NLP/tree/master/Documentation'>documentation</a>
