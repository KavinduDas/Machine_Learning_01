from flask import Flask ,render_template ,request , redirect
from helper import preprocessing ,vectorizer ,get_prediction
from loggers import logging

app = Flask(__name__)

logging.info('Flask server started')

data = dict()
reviews = []
positive = 0
negative = 0

@app.route("/")



def index():
    data["reviews"] = reviews
    data["positive"] = positive
    data["negative"] = negative

    logging.info("==Opens Web Page==")
    return render_template("index.html" ,data=data)

@app.route("/", methods = ["POST"])

def my_post():
    text = request.form['text']
    logging.info(f"Text : {text}")

    prepocessed_text = preprocessing(text)
    logging.info(f"Prepoccessed Text : {prepocessed_text}")

    vectorized_text = vectorizer(prepocessed_text)
    prediction = get_prediction(vectorized_text)

    if prediction == "negative":
        global negative
        negative += 1
    else:
        global positive
        positive += 1
    
    reviews.insert(0,text)
    return redirect(request.url)



if __name__  == "__main__":
    app.run()