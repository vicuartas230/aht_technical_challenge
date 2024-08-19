from flask import Flask, render_template, request
from models.storage import Storage
from models.device import Device


app = Flask(__name__)

storage = Storage()
storage.load_session()


@app.route("/", strict_slashes=False)
def index():
    return render_template('index.html', items=storage.all())

@app.route("/add", methods=['POST', 'GET'], strict_slashes=False)
def create():
    if request.method == 'POST':
        fields = [
            "name"
            "price"
            "mac_address"
            "serial_number"
            "manufacturer"
            "description"
        ]
        new_item = {
            field.replace('_', '-'): (float(request.form[field])
                                      if field == "price"
                                      else request.form[field])
                                      for field in fields
        }
        new_obj = Device(**new_item)
        storage.new(new_obj)
        storage.save()
    return render_template('add.html')

@app.route("/edit/<int:id>", methods=['GET', 'PUT'], strict_slashes=False)
def edit(id):
    el = storage.get(id)
    if el is not None:
        for k, v in el.items():
            print("key: ", k, "Value: ", v)
    return render_template('edit.html')

@app.route("/delete/<int:id>", strict_slashes=False)
def delete(id):
    el = storage.get(id)
    if el is None:
        return {
            "result": "No object found."
        }
    else:
        storage.delete(el)
        storage.save()
        return {
            "result": "done"
        }
