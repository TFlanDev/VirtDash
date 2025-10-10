from fastapi import FastAPI
import hypervisor
app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/vms")
def list_vms():
    pass