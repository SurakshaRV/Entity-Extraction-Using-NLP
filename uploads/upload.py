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
from tech_check2 import *

app = Flask(__name__)
app.secret_key = "super secret key"
f=''
ff=''
@app.route('/')  
def upload():  
    return render_template("test.html")  
 
@app.route('/home', methods = ["GET",'POST'])  
def success():
    global f,ff
    if request.method == 'POST':
        f = request.files['file']
        #flash("UPLOADING FILE...")
        #print(f)
        #print(type(f))
        fn=str(f)
        fn=fn[15:]
        ff=fn[:-22]
        print(ff)
        f.save(f.filename)
        #flash("FILE UPLOADED")
        #flash("EXTACTING TEXT IN THE PDF FILE.")
        pdfparser(ff)
        #flash("TAGGING THE EXTRACTED TEXT.")
        tagging(ff)
        #flash("DONE TAGGINGING.")
        return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg').lower()
    userText=userText.strip('?')
    print(userText)
    query_type=mainQuery(userText)
    if query_type!="tech":
        userText=spell_correct(userText)
    if re.match( r'.* (support|supports|supported|use|implement|implements|uses|used|implemented).*',userText):
        if ans_query(userText,ff):
            print("Basic")
            return ans_query(userText,ff)
        else:
            if query_type=="tech":
                return str(chatty(userText))
            elif query_type=="generic":
                if str(genericResponse(userText)) !="None":
                     return str(genericResponse(userText))
                else:
                     return "I can't uderstand you :("
            else:
                return "Sorry. I did not understand..."            
    elif "version" in userText:
       if ans_query(userText,ff):
           print("Basic")
           return ans_query(userText,ff)
       else:
            if query_type=="tech":
                return str(chatty(userText))
            else:
                return "Sorry. I did not understand..."
    elif query_type=="generic":
        print("Gen")
        print(userText)
        if str(genericResponse(userText)) !="None":
            return str(genericResponse(userText))
        else:
            return "Sorry. I did not understand..."
    elif query_type=="tech":
        print("Tech")
        return str(chatty(userText))
    else:
        return "Sorry.No idea..."
  
if __name__ == '__main__':
    app.debug = True
    app.run() 

