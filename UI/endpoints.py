
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__, static_folder = 'public')

@app.route('/')
def root():
	return app.send_static_file('index.html')

@app.route('/<path:path>')
def default(path):
  return app.send_static_file(path)

# user sends persona
# sends back an array of relevant articles
@app.route('/add_persona', methods=['POST'])
def add_persona():
	json = request.json or {'phrase': '', 'weight': 0}
	phrase, weight = json['phrase'], json['weight'] # use phrase and weight

	# TODO: get actual feed

	# TODO: return jsonniy(feed = <actual feed>)

	return jsonify(feed = [{
		'text': 10 * 'My insane text from ' + weight,
		'title': 'Big Title'
		} for i in xrange(0, 10)])


if __name__ == "__main__":
    app.run()