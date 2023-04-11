from flask import Flask,render_template,request
from predict_pipeline import CustomData,PredictPipeline
app=Flask(__name__)

@app.route("/")

def home():
    return  render_template("index.html")

@app.route("/predict",methods=["POST","GET"])
def predict_datapoints():
    if request.method=="GET":
        return render_template("index.html")
    else:
        data=CustomData(
            age=request.form.get("age"),
            sex=request.form.get("sex"),
            bmi=request.form.get("bmi"),
            chidren=request.form.get("children"),
            smoker=request.form.get("smoker"),
            region=request.form.get("region")
  
        )




if __name__=="__main__":
    app.run(debug=True)