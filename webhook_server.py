# from flask import Flask, request, jsonify

# app = Flask(__name__)

# # Root endpoint
# @app.route('/', methods=['GET', 'POST'])
# def root():
#     return "Welcome to the webhook server!", 200

# # Webhook endpoint
# @app.route('/webhook', methods=['POST'])
# def webhook():
#     data = request.json  # Get the JSON data sent by the webhook
#     print("Received data:", data)

#     violation_type = data.get("violationType", "Unknown")
#     artifact = data.get("artifact", "N/A")

#     # Email content
#     subject = f"Policy Violation Alert: {violation_type}"
#     body = f"Violation detected in artifact: {artifact}\n\nFull Data:\n{data}"

#     # Process the data (e.g., save to a file or database)
#     return jsonify({"status": "success"}), 200

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)



import json
from flask import Flask, request, jsonify
from send_email import send_email 

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    return "Welcome to the webhook server!", 200


@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    
    with open("scan_results.json", "w") as file:
        json.dump(data, file, indent=4)


    subject = "Policy Violation Alert:"

    send_email(subject, str(data)) 

    return jsonify({"status": "Email Sent"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
