from flask import Flask, request
import json, os

app=Flask(__name__)

@app.route("/", methods=["POST"])
def handleHook():
    response = {}
    try:
        # only return if 1 user has been found (since username is UNIQUE, it should only be 1 or 0)
        if(users.count()==1):
            request.form["secret"] == os.environ["SECRET"]
            response["success"] = True
        else:
            response["success"] = False
    except:
        response["success"] = False
    return json.dumps(response)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=os.environ["PORT"])