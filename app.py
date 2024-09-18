from flask import Flask, request
from db import items, stores

app = Flask(__name__)


@app.get("/store") # http://127.0.0.1:5000/store
def get_stores():
    return{"stores" : stores}

@app.post("/store") # http://127.0.0.1:5000/store
def create_store():
    request_data= request.get_json()
    new_store = {"name": request_data["name"], "items" : []}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item") # http://127.0.0.1:5000/store/<name>/item
def create_item(name):
    request_data= request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404  

@app.get("/store/<string:store_id>")    # http://127.0.0.1:5000/store/<store_id>
def get_store(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message": "Store not found"}, 404

@app.get("/store/<string:name>/item")    # http://127.0.0.1:5000/store/<name>/item
def get_item_in_store(name):
    for store in stores:
        if store["name"]==name:
            return {"items": store["items"]}, 201
    return {"message": "Store not found"}, 404