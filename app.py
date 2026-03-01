from fastapi import FastAPI, HTTPException
from calculator import square_root, factorial, natural_log, power

app = FastAPI(title="Scientific Calculator API")


@app.get("/")
def home():
    return {"message": "Scientific Calculator API is running"}


@app.get("/sqrt")
def sqrt(number: float):
    try:
        return {"result": square_root(number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/factorial")
def fact(number: int):
    try:
        return {"result": factorial(number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/ln")
def ln(number: float):
    try:
        return {"result": natural_log(number)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/power")
def pow(x: float, b: float):
    return {"result": power(x, b)}

#changes to check webhook
#again test after crum issue
#changes in webhook url https://unobtainable-werner-unpensioned.ngrok-free.dev to https://unobtainable-werner-unpensioned.ngrok-free.dev/github-webhook/ because of github plugin