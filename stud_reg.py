from flask import Flask, render_template, request, redirect
import utils.json_utils as json_utils

file="data/stud.json"

app=Flask(__name__)

@app.route("/")
def index():
    data=json_utils.read_json(file)
    return render_template("homepage.html", data=data["students"])

@app.route("/register", methods=["GET","POST"])
def reg():
    if request.method=="POST":
        user=request.form["username"]
        course=request.form["course"]
        data=json_utils.read_json(file)
        stud_dict={
            "s_no": len(data["students"])+1,
            "name":user,
            "course":course,
            "status":"Enrolled"
        }
        data["students"].append(stud_dict)
        json_utils.write_json(file,data)
    return redirect("/")


@app.route("/update/<int:id>")
def update(id):
    data=json_utils.read_json(file)
    valid_data=[]
    for stud in data["students"]:
        if id==stud["s_no"]:
            valid_data=stud
    return render_template("update.html",id=id,user=valid_data["name"],course=valid_data["course"],status=valid_data["status"] )

@app.route("/update_data", methods=["GET","POST"])
def update_data():
    if request.method=="POST":
        id=request.form["id"]
        user=request.form["username"]
        course=request.form["course"]
        status=request.form["state"]
        data=json_utils.read_json(file)
        for stud in data["students"]:
            if str(id)==str(stud["s_no"]):
                stud_dict={
                    "s_no": id,
                    "name":user,
                    "course":course,
                    "status":status
                }
                data["students"][int(id)-1]=stud_dict
        json_utils.write_json(file,data)
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)