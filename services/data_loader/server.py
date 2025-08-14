from fastapi import FastAPI
from dal import DataLoader

app = FastAPI()
dal = DataLoader()

@app.get("/data")
def get_data():
    return dal.select_all()
