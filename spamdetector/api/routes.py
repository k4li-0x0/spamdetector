from fastapi import FastAPI

from ..model import util

app = FastAPI()


@app.get("/predict")
def predict_request(message: str):
    result = util.predict(message)
    return {"result": str(result)}
