from flask import Flask,render_template,request
from predict_pipeline import CustomData,PredictPipeline
application=Flask(__name__)
app=application

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
            children=request.form.get("children"),
            smoker=request.form.get("smoker"),
            region=request.form.get("region")
  
        )
    pref_data=data.get_values_as_dataframe()
    # print(pref_data)

    predict_pipeline=PredictPipeline()
    result=predict_pipeline.predict(pref_data)
    # print(result)
    return render_template("home.html",result=result[0])


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)