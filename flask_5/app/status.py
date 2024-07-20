from flask import Flask, jsonify, request

app = Flask('__main__')


@app.route('/status-demo', methods=['GET'])
def status_demo():
    status_code = request.args.get('status_code')

    if not status_code:
        return jsonify({"error": "status_code query parameter is required"}), 400  # Bad Request

    try:
        status_code = int(status_code)
    except ValueError:
        return jsonify({"error": "status_code must be an integer"}), 400  # Bad Request

    if status_code == 200:
        return jsonify({"message": "OK"}), 200  # OK
    elif status_code == 201:
        return jsonify({"message": "Created"}), 201  # Created
    elif status_code == 204:
        return '', 204  # No Content
    elif status_code == 400:
        return jsonify({"error": "Bad Request"}), 400  # Bad Request
    elif status_code == 401:
        return jsonify({"error": "Unauthorized"}), 401  # Unauthorized
    elif status_code == 403:
        return jsonify({"error": "Forbidden"}), 403  # Forbidden
    elif status_code == 404:
        return jsonify({"error": "Not Found"}), 404  # Not Found
    elif status_code == 500:
        return jsonify({"error": "Internal Server Error"}), 500  # Internal Server Error
    else:
        return jsonify({"error": "Status code not handled"}), 400  # Bad Request for unhandled status codes


app.run(debug=True)
