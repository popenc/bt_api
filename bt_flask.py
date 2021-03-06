from flask import Flask, request, jsonify
import os
import logging
from bt_cli import BTCLI

app = Flask(__name__)
app.config.update(
	DEBUG=True
)

# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# os.environ.update({
# 	'PROJECT_ROOT': PROJECT_ROOT
# })
logging.basicConfig(level=logging.DEBUG)

###################
# FLASK ENDPOINTS #
###################

@app.route("/bt")
def test_page():
	pass

@app.route("/bt/test")
def test_bt():
	return jsonify({"status": "bt_flask up and running."})

@app.route("/bt/rest")
def rest_endpoints():
	pass

@app.route("/bt/rest/run", methods=["POST"])
def run_bt():
	"""
	Runs bt_cli.py module for biotransformation predictions.
	"""
	post_dict = request.get_json()
	requested_smiles = post_dict['smiles']
	bt_results = BTCLI().run_bt_routine(requested_smiles)  # bt_cli expecting list of smiles
	return jsonify({"status": True, "data": bt_results})

if __name__ == '__main__':
	app.run(debug=True)