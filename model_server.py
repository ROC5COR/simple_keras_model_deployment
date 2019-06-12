from flask import Flask
from flask import render_template
from flask import request, jsonify
from keras.models import load_model
import tensorflow as tf
import numpy as np

app = Flask(__name__)

global model
model = load_model('vector_direction.h5')
model.summary()

global graph
graph = tf.get_default_graph()



@app.route("/", methods=['GET','POST'])
def home():
	if request.method == 'POST':
		if request.is_json:
			print("JSON received !\n")
			try:
				data = request.json['data']
				data = np.array([data])
				print("Data received: ",data)
				with graph.as_default(): # Needed to restore the graph
					y = model.predict(data)
					print("Predicted: ",y)
					return 'ok: '+str(y[0][0])
				return 'ko: Error while creating session'
			except Exception as e:
				print("Exception: ",e)
				return 'ko: wrong format'
			print(request.json)
			return 'ok'
		else:
			print("This is not JSON\n")
			return 'ko: you have to pass JSON'

	elif request.method == 'GET':
		return render_template('index.html')

app.run(host='0.0.0.0', port=5000)
