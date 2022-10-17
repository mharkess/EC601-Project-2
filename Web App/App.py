from flask import Flask, render_template, jsonify, request
import TwitterCalls

app = Flask("TwitterBot")

@app.route("/")
def Home():
    return render_template("home.html")

@app.route("/about/")
def About():
    return render_template("about.html")

@app.route("/userSentiment", methods = ['GET'])
def userAnalysis():
    user = request.args.get('fname')
    if user == None:
        returnval = 'ERROR'
    else:
        returnval = TwitterCalls.getAvgSentiment(user)
        tweetdisp = TwitterCalls.getSentimentText(user)
    return render_template("home.html", sentiment = returnval, disp = tweetdisp)
