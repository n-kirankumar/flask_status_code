from flask import Flask,jsonify,request

app = Flask('__main__')


@app.route('/person-details', methods=['GET'])
def get_infor():
    data = request.args    # immutable dict; reads query parameters
    name = data.get('name')
    occupation = data.get('occupation')

    # Validate if both name and occupation are provided
    if not name or not occupation:
        return jsonify({"error": "name and occupation query parameters are required"}), 400

    return jsonify(name=name, occupation=occupation),200


'''To capture the request payload, you can use the request.json 
attribute in Flask to handle JSON data sent in the body of a POST request. 
'''
@app.route('/person-details', methods=['POST'])
def get_info():
    if request.is_json:
        data = request.get_json()
        name = data.get('name')
        occupation = data.get('occupation')

        # Validate if both name and occupation are provided
        if not name or not occupation:
            return jsonify({"error": "name and occupation fields are required"}), 400

        return jsonify(name=name, occupation=occupation)
    else:
        return jsonify({"error": "Request must be JSON"}), 400


@app.route('/check')
def get_info():
    parametr



app.run(debug = True)

