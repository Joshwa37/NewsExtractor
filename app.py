from dotenv import load_dotenv
import os
from flask import Flask
from flask import Flask,redirect,url_for,render_template,request,session,flash,jsonify
import requests


load_dotenv()


app=Flask(__name__)

def elaborate_news(raw_data):
    articles = raw_data.get('results', [])
    processed_list = []
    for item in articles:
        
        clean_item = {
            'title': item.get('title'),
            'desc': item.get('description'),
            'source': item.get('source_name'),
            'img': item.get('image_url', 'https://via.placeholder.com/300'),
            'url': item.get('link')
        }
        processed_list.append(clean_item)
    
    return processed_list
@app.route("/")
def commom():
    return render_template("home.html")
@app.route("/home")
def home():
    payload={
        'apikey':os.getenv("API_KEY"),
        'q':request.args.get('topicInput'),
        'language':request.args.get('lang','en'),
        
    }
    print("ckjbajscb")
    responce=requests.get("https://newsdata.io/api/1/news?",params=payload)
    responce=responce.json()
    responce=elaborate_news(responce)
    return jsonify(responce)




if __name__ == "__main__":
    app.run(debug=True)

