from fastapi import FastAPI


app = FastAPI(title="Async FastAPI")


@app.get('/')
def home():
    return {"note": "Surya Kosana testing python fastapi ci cd"}
