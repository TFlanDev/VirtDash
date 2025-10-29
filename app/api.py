from fastapi import FastAPI, HTTPException
import hypervisor,schemas
from typing import List
app = FastAPI()


@app.get("/vms", response_model=List[schemas.VM])
def list_vms():
    hypervisor_conn = hypervisor.connect()
    vms = hypervisor.list_vms(hypervisor_conn)
    hypervisor.disconnect(hypervisor_conn)
    return vms


@app.get("/vm/{vmname}/", response_model=schemas.VM)
def get_vm_by_name(vmname : str):
    hypervisor_conn = hypervisor.connect()
    vm = hypervisor.get_vm_info(hypervisor_conn, vmname)
    if not vm:
        raise HTTPException(status_code=404, detail="VM Does not exist")
    hypervisor.disconnect(hypervisor_conn)
    return vm

@app.put("/vm/{vmname}/start")
def start_vm(vmname: str):
    hypervisor_conn = hypervisor.connect()
    result = hypervisor.start_domain(hypervisor_conn, vmname)
    if not result:
        raise HTTPException(status_code=404, detail="VM Does not exist")
    hypervisor.disconnect(hypervisor_conn)
    return {"result": result} 

@app.put("/vm/{vmname}/stop")
def stop__vm(vmname : str):
    hypervisor_conn = hypervisor.connect()
    result = hypervisor.shut_down_domain(hypervisor_conn, vmname)
    if not result:
        raise HTTPException(status_code=404, detail="VM Does not exist")
    hypervisor.disconnect(hypervisor_conn)
    return {"result": result}   

