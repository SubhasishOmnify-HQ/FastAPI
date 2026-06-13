from fastapi import FastAPI
app = FastAPI()

# load data set using Json
import json
def load_data():
    with open('data.json','r') as f:
        data = json.load(f)
    return data

@app.get("/")
def root():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {'message': 'A fully functional API to Manage your Patient record'}

@app.get('/view')
def view():
    data = load_data()
    return data