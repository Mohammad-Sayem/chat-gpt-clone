# from flask import Flask,render_template,request,jsonify
# from flask_pymongo import PyMongo
# import openai

# openai.api_key ='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'




# app = Flask(__name__)
# app.config["MONGO_URI"] = "mongodb+srv://mirza_danish_baig:00000000@cluster0.kum30lc.mongodb.net/chatgpt"
# mongo = PyMongo(app)

# @app.route('/')
# def hello_world():
#         chats=mongo.db.chats.find({})
#         mychats=[chat for chat in chats]
#         print(mychats)
  
#         return render_template('index.html',mychats=mychats)
 
# @app.route('/api',methods=['GET','POST'])
# def api():
#     if request.method=='POST':
    
#         # print(request.json)

#         question=request.json.get('question')
#         chat=mongo.db.chats.find_one({"question":question})
#         if chat:
#             data={'question':question,'answer':f"{chat['answer']}"}
#         # data={'result':f" answer of {question}"}
#             return jsonify(data)
#         else:
#             response = openai.Completion.create(
#             model="text-davinci-003",
#             prompt=question,
#             temperature=1,
#             max_tokens=256,
#             top_p=1,
#             frequency_penalty=0,
#             presence_penalty=0
#             )

#             # data={"question":question,"answer":response['choices'][0]['text']}
#             data = {"question":question, "answer":response["choices"][0]["text"]}
#             print(response)
#             mongo.db.chats.insert_one({"question":question,"answer":f"answer from mongodb{response['choices'][0]['text']}"})
#             return jsonify(data)

#     data={'result':'i am sorry babu i am a machine'}
#     return jsonify(data)
   



# app.run(debug=True)  

from flask import Flask,render_template,request,jsonify
from flask_pymongo import PyMongo
import openai

openai.api_key = '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'

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://mirza_danish_baig:00000000@cluster0.kum30lc.mongodb.net/chatgpt"
mongo = PyMongo(app)






@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api",methods=["GET","POST"])
def api():
    if request.method=="POST":
       print(request.json)
       question=request.json.get("question")
       chat=mongo.db.chats.find_one({"question":question})
       if chat:
        #  data={"question":question,"answer":question}
         data={'question':question,'answer':f"{chat['answer']}"}
         print(data)
         return jsonify(data)
       else:
        


            response = openai.Completion.create(
            model="text-davinci-003",
            prompt=question,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )
            data={"question":question,"answer":response["choices"][0]["text"]}
            print(response)
            mongo.db.chats.insert_one({"question":question,"answer":
            f"this answer from mongo db{response['choices'][0]['text']}"
            })
            return jsonify(data)


       

          
    data={"result":'fafah a fafha  ahfiafa'}
    return jsonify(data)
        


app.run ( debug=True ,port=8001)








	
