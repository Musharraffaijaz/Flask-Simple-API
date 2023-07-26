from flask import Flask, request, jsonify #This will import Flask from flask, and will request to create a json response

#to create a flask application we use app function
app = Flask(__name__)


@app.route("/get-user/<user_id>")
def get_user(user_id):
    #creating a dictionary named as user_data
    user_data = {
        "user_id": user_id,
        "name": "Musharaf Aijaz",
        "email": "eyemusharraffaijaz@gmail.com"
    }

    extra = request.args.get('extra')
    if extra: 
        user_data["extra"] = extra

    return jsonify(user_data), 200 #heae we are jsonify the dictionary user_data so that flask can esily read it

@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()

    return jsonify(data), 201

if (__name__ == "__main__"):
    app.run(debug=True) 

    
#there are a lot of route methods in python such as, GET, POST, PUT, DELETE. 
# GET: Requests data from a specified path.
# POST: Create a Resource.
# PUT: Updates a resource.
# DELETE: Deletes a resource