"""
A prototype web-interafce to the SDP Configuration database built
using FLASK
"""

from flask import Flask, render_template

from ska_sdp_opinterface import model

app = Flask(__name__)


@app.route("/test")
def hello_world():
    """A test 'Hello World' target"""
    return "Hello, World!"


@app.route("/")
@app.route("/db-list")
def db_list():
    """List entries target"""
    return render_template(
        "db_list.html",
        title="Database Contents List",
        entries=model.get_raw_dict(),
    )


@app.route("/db-tree")
def db_tree():
    """Entries tree-view target"""
    return render_template(
        "db_tree.html",
        title="Database Contents Tree",
        data=model.get_tree_data(),
    )


@app.route("/scripts")
def scripts():
    """List scripts from database"""
    return render_template(
        "scripts.html", title="Scripts", data=model.get_scripts()
    )


# @app.route("/db-create", methods=["POST", "GET"])
# def db_create():
#     """Create database entry prototype"""
#     if request.method == "POST":
#         key = request.form["key"]
#         value = request.form["value"]
#         model.create_entry(key, value)
#         return redirect(url_for("db_list"))
#
#     return render_template("db_create.html")


if __name__ == "__main__":
    app.run()
