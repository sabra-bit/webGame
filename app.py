from flask import Flask, redirect, url_for, render_template, request ,jsonify
 

app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
   return render_template("index1.html")


if __name__ == "__main__":
   app.run(debug= True)
    #  app.run( host="0.0.0.0" ,port=8080 , debug= True ) 
