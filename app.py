from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from classifier.utils.common_functions import decodeImage
from classifier.pipeline.predict import PredictionPipeline

 #initialising flask
os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")

app= Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename= "inputImage.jpg"
        self.classifier= PredictionPipeline(self.filename)




@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template("index.html")



@app.route("/train", methods=["GET","POST"])
@cross_origin()
def trainRoute():
    os.system("python3 main.py")
    return "Training done successful"



@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image= request.json["image"]
    decodeImage(image, clApp.filename)
    results= clApp.classifer.predict()
    return jsonify


if __name__== "__main__":
    clApp=ClientApp()
    app.run(host="0.0.0.0", port= 8080)


