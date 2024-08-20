from flask import Flask, render_template, request, redirect, url_for, jsonify
from models.storage import Storage
from models.device import Device
from datetime import datetime


app = Flask(__name__)

storage = Storage()
storage.load_session()


@app.route("/", strict_slashes=False)
def index():
    return render_template("index.html", items=storage.all())

@app.route("/add", methods=["POST", "GET"], strict_slashes=False)
def create():
    if request.method == "POST":
        fields = [
            "name",
            "price",
            "mac_address",
            "serial_number",
            "manufacturer",
            "description",
        ]
        new_item = {
            field:
            request.form[field.replace('_', '-')]
             for field in fields
        }
        new_obj = Device(**new_item)
        storage.new(new_obj)
        storage.save()
        return redirect(url_for("index"))
    return render_template("add.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"], strict_slashes=False)
def edit(id):
    el = storage.get(id)
    if request.form.get("_method") == "PUT":
        not_in_form = ["_sa_instance_state", "id", "created_at", "updated_at"]
        edited = False
        for key, value in el.__dict__.items():
            if key not in not_in_form:
                form_value = request.form[key.replace('_', '-')]
                if form_value != value:
                    setattr(el, key, form_value)
                    edited = True
        if edited:
            el.updated_at = datetime.now()
            storage.save()
        return redirect(url_for("index"))
    return render_template("edit.html", el=el)

@app.route("/delete/<int:id>", methods=["DELETE"], strict_slashes=False)
def delete(id):
    el = storage.get(id)
    if el is not None:
        storage.delete(el)
        storage.save()
    return jsonify({"success": True}), 200
