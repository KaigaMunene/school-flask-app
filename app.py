from flask import Flask ,jsonify ,request

app = Flask(__name__)

list_of_students = []

@app.route("/student", methods=["post"])
def add_student():
    data = request.get_json()
    student = data.get("student")
    list_of_students.append(student)
    return jsonify({"message": "student successfully added"})

@app.route("/students", methods = ["get"])
def get_all_student():
    return jsonify({"data": {"student" : list_of_students}})

@app.route("/students/<id>", methods = ["get"])
def get_one_student(id):
    return jsonify ({"data": {"student" : list_of_students[int(id)]}})

@app.route("/student/<id>", methods=["delete"])
def delete_a_student(id):
    list_of_students.pop(int(id))
    return jsonify ({"message" : "student successfully deleted"})



if __name__ == ("__main__"):
    app.run(debug=True)
