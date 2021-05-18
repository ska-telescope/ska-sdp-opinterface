from flask import Flask, render_template, url_for, request, redirect
from ska_sdp_config import config

app = Flask("__name__")


@app.route("/test")
def hello_world():
    return "Hello, World!"


@app.route("/")
@app.route("/db_list")
def db_list():
    cfg = config.Config()
    d = {}
    for txn in cfg.txn():
        keys = txn.raw.list_keys("/", recurse=8)
        for key in keys:
            d[key] = txn.raw.get(key)
    print(d)
    return render_template("db_list.html", entries=d)


@app.route("/db_create", methods=["POST", "GET"])
def db_create():
    if request.method == "POST":
        key = request.form["key"]
        value = request.form["value"]
        cfg = config.Config()
        for txn in cfg.txn():
            txn.raw.create(key, value)
        print(key + ",  " + value)
        return redirect(url_for("db_list"))

    return render_template("db_create.html")


if __name__ == "__main__":
    app.run(debug=True)
