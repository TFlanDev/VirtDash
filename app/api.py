from fastapi import FastAPI
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
    hypervisor.disconnect(hypervisor_conn)
    return vm
