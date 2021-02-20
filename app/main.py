from fastapi import FastAPI
from faker import Faker

faker = Faker()

app = FastAPI(title="Async FastAPI")


@app.get('/', tags=["home"])
def home():
    return {"note": "Surya Kosana testing ci cd"}


@app.get('/about', tags=["about"])
def get_profile_info():
    profile_dict = {
        "first_name": faker.unique.first_name(),
        "last_name": faker.unique.last_name(),
        "address": faker.address()
    }
    return profile_dict


@app.get('/{id}')
def get_id_name(id: str) -> str:
    names_dict = {
        "1": "Surya",
        "2": "Prakash",
        "3": "Reddy",
        "4": "Kosana",
        "5": "Surya Prakash Reddy Kosana"
    }
    return names_dict[id]
