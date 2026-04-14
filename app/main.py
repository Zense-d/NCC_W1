from fastapi import FastAPI
import os

app = FastAPI()

anm = os.getenv("anm", "")
NMSG = os.getenv("wmsg")
auth = os.getenv("nme")
aunr = os.getenv("nrp")

@app.get("/")
def read_root():
    return {"message": f"{NMSG}","anda berada di" : f"{anm}"}

@app.get("/me")
def read_root():
    return {"service": f"{NMSG}", "author" : f"{anm}", "NRP" : f"{aunr}"}

@app.get("/showcapybara")
def read_root():
    cp = os.getenv("easteregg")
    return {f"{cp}"}


@app.get("/health")
def health_check():
    return {"status": "running gwenchana", "code": "200 OK" }