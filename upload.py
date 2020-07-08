from flask import *
from chat import *
import nltk
import csv
import re
import random
from extracting_pdf import *
from queryClassifier import *
from tagging_with_spacy import *
from techBot import *
from threeQuestions import *
import testing_for_generic
from fuzzywuzzy import fuzz
from tech_check import *

#creating an instance of Flask class and takes current module name as arguement
app = Flask(__name__)
#initializing secret key for the session
app.secret_key = "super secret key"
f=''
ff=''
#bounding '/' url with upload function
@app.route('/')
def upload():
    return render_template("test.html")

@app.route('/home', methods = ["GET",'POST'])
def success():
    global f,ff
    #checking if a file is selected to upload
    if request.method == 'POST':
        #getting the selected file
        f = request.files['file']
        #uploading the selected .pdf file.
        f.save(f.filename)
        #obtaining the name of the .pdf file uploaded
        fn=str(f)
        fn=fn[15:]
        filename=fn[:-22]
        #extracting the text in the .pdf file.
        pdfparser(filename)
        #tagging the extracted text.
        tagging(filename)
        #returning rendered home.html template
        return render_template("home.html")

@app.route("/get")
def get_bot_response():
    #getting the user query and converting it to lowercase
    userText = request.args.get('msg').lower()
    #removing the question mark at the end of query
    userText=userText.strip('?')
    #getting the query type using NaiveBaeyes classifier
    query_type=mainQuery(userText)
    if query_type!="tech":
        userText=spell_correct(userText) #correcting the spelling of user query
    if re.match( r'.* (support|supports|supported|use|implement|implements|uses|used|implemented).*',userText):
        #getting the chatbot response if query is a basic question
        if ans_query(userText,ff):
            print("Basic")
            return ans_query(userText,ff)
        else:
            #getting the chatbot response if query is a technical question
            if query_type=="tech":
                return str(chatty(userText))
            #getting the chatbot response if query is a generic question
            elif query_type=="generic":
                if str(genericResponse(userText)) !="None":
                     return str(genericResponse(userText))
                else:
                     return "I can't uderstand you :("
            else:
                return "Sorry. I did not understand..."

    #getting the chatbot response if query is related to version of a tech
    elif "version" in userText:
       if ans_query(userText,ff):
           print("Basic")
           return ans_query(userText,ff)
       else:
            if query_type=="tech":
                return str(chatty(userText))
            else:
                return "Sorry. I did not understand..."
    #getting the chatbot response if query is a generic question
    elif query_type=="generic":
        print("Gen")
        print(userText)
        if str(genericResponse(userText)) !="None":
            return str(genericResponse(userText))
        else:
            return "Sorry. I did not understand..."
    #getting the chatbot response if query is a technical question
    elif query_type=="tech":
        print("Tech")
        return str(chatty(userText))
    else:
        return "Sorry.No idea..."

if __name__ == '__main__':
    app.debug = True
    app.run()
