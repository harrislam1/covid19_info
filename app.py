from flask import Flask, render_template, request 
from deeppavlov import configs, train_model
from deeppavlov.core.common.file import read_json

app = Flask(__name__)


model_config = read_json(configs.faq.tfidf_logreg_en_faq)
model_config["dataset_reader"]["data_url"] = "https://raw.githubusercontent.com/harrislam1/covid19_info/main/cdc_covid19_2021faq.csv"
bot = train_model(model_config)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot([userText])[0][0])


if __name__ == "__main__":
    app.run()