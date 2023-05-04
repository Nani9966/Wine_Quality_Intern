from flask import Flask
from Wine_ML.logger import logging
from Wine_ML.exception import CustomException

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("we are trying exception block")
    except Exception as e:
        Wine = CustomException(e,sys)
        logging.info(Wine.error_message)
        logging.info("We are testing logging module")
        return "hello World"

if __name__=="__main__":
    app.run(debug=True)