from flask import Flask
from flask import request, render_template, jsonify
#from flask_sqlalchemy import SQLAlchemy

info= {"header":"Social golf app by Axel and Boris" ,"body": "An app developed for further enhancing the experience of the wonderful game of golf"}
henrik={"id":1, "firstName": "Henrik", "lastName": "Boris-Möller", "hcp": 8.8, "club": "Wasa GK"}
axel = {"id":2, "firstName": "Axel", "lastName": "Sundberg", "hcp": 4.8, "club": "Båstad GK"}
card= {"id":1, "course":"LAGK", "timestamp": "14.30 2016-06-12", "score": {1:None, 2:None, 3:None}, "ForImprovementInfo":"Instead of score:(...) we will in the future have (player1:((playerId:1... (score: () etc"}

app = Flask(__name__)
#db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({"info":info})

@app.route("/user/<int:userId>")
def user(userId):
	if userId==1:
		return jsonify({"userInfo":henrik})
	if userId==2:
		return jsonify({"userInfo":axel})
	else: 
		return jsonify({"error": [{"message":"There exist no user with that id"}, {"type":"not found"}]})

@app.route("/scorecard/<int:scoreCardId>", methods=['GET'])
def scoreCard(scoreCardId):
	if scoreCardId==1:
		return jsonify({"scoreCard":card})
	else: 
		return jsonify({"error": [{"message":"There exist no round with that id"}, {"type":"not found"}]})


@app.route("/scorecard/<int:scoreCardId>", methods=['POST'])
def addScore(scoreCardId):
	if scoreCardId==1:
		hole=request.json["hole"]
		score=request.json["score"]
		if hole>3 or hole<1:
			return jsonify({"error": [{"message":"There exist no hole with that id"}, {"type":"not found"}]})
		card["score"][hole]=score
		return jsonify({"hole":hole, "score":score})
	else: 
		return jsonify({"error": [{"message":"There exist no round with that id"}, {"type":"not found"}]})


if __name__ == '__main__':
    app.run()