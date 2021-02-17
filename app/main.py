from fastapi import FastAPI


app = FastAPI(title="Async FastAPI")


@app.get('/')
def home():
    return {"note": "Surya Prakash Kosana deployed application on raspberrypi kubenetes cluster"}