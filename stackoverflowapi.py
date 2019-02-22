from flask import Flask
from flask_restful import Resource, Api
from nltk.tokenize import word_tokenize
import pickle
from sklearn.externals import joblib

app = Flask(__name__)
api = Api(app)

class StackoverflowTagging(Resource):
    def __init__(self):

        self.additional_string = "Hello"
        self.loadedClassifier = joblib.load('classifier.pkl')
        self.mbl_loaded = pickle.load(open("MultiLabelBinarizer.pickle", "rb"))

    def get(self, x):
        prediction = self.loadedClassifier.predict([x])
        classes = self.mbl_loaded.inverse_transform(prediction)
        return classes

    def tokenize(self, text):
        tokenize_text = word_tokenize(text)
        return tokenize_text

    def toLowerCase(self, text):
        return text.lower()



api.add_resource(StackoverflowTagging, '/get-tags/<x>')  # Route_1


if __name__ == '__main__':
    app.run(port=5003)