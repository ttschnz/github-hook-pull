from flask import Flask, request
import json, os

app=Flask(__name__)

@app.route("/", methods=["POST"])
def handleHook():
    response = {}
    try:
        if request.form["secret"] == os.environ["SECRET"]:
            response["success"] = True
            os.system(os.environ["COMMAND"])
        else:
            response["success"] = False
    except:
        response["success"] = False
    return json.dumps(response)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=os.environ["PORT"])