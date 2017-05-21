
from flask import Flask
from flask import jsonify
from flask import request
from getData import getReportsForPersona

personaTitles = [
	"ICE Director",
	"Assistant Secretary of Defense for Nuclear, Chemical, and Biological Defense Programs (ASD(NCB))",
	"North Korea policy group",
	"Director; maritime security operations",
	"Director; wildfire division",
	"mission director; syria",
	"centCOM j2"
]

personas = [{'phrases': [], 'reports': []} for _ in personaTitles]

app = Flask(__name__, static_folder = 'public')

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/<path:path>')
def default(path):
  return app.send_static_file(path)

# user sends persona
# sends back an array of relevant articles
'''
@app.route('/edit_persona/<int:target>', methods=['POST'])
def edit_persona(target):
	json = request.json

	# for each target use phrase and weight
	phrase, weight = json['phrase'], json['weight']

	print 'hello!'

	persona = getReportsForPersona(personaTitles[target])

	# TODO: get actual feed

	# TODO: return jsonify(feed = <actual feed>)

	# TODO: remove everything after this
	return jsonify(feed = [{
		'text': 10 * 'My insane text from ' + weight,
		'title': 'Big Title'
		} for i in xrange(0, 10)])
'''

# user sends persona
# sends back an array of relevant articles
@app.route('/fetch_persona/<int:target>', methods=['GET'])
def add_persona(target):
	print 'hello!'
	persona = getReportsForPersona(personaTitles[target])

	# TODO: get actual feed

	# TODO: return jsonify(feed = <actual feed>)

	# TODO: remove everything after this
	return jsonify(persona = persona)


if __name__ == "__main__":
    app.run()