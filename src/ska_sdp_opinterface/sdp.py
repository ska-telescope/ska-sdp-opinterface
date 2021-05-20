from flask import Flask, render_template, url_for, request, redirect
from ska_sdp_opinterface import model


app = Flask(__name__)


@app.route("/test")
def hello_world():
    return "Hello, World!"


@app.route("/")
@app.route("/db_list")
def db_list():
    return render_template("db_list.html", title="Database Contents List",
                           entries=model.get_raw_dict())


@app.route("/db_tree")
def db_tree():
    return render_template("db_tree.html", title="Database Contents Tree",
                           data=model.get_tree_data())


@app.route("/workflows")
def workflows():
    return render_template("workflows.html", title="Workflows",
                           data=model.get_workflows())


@app.route("/db_create", methods=["POST", "GET"])
def db_create():
    if request.method == "POST":
        key = request.form["key"]
        value = request.form["value"]
        model.create_entry(key, value)
        return redirect(url_for("db_list"))

    return render_template("db_create.html")


if __name__ == "__main__":
    app.run(debug=True)
