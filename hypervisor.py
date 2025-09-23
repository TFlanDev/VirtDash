import libvirt
import sys
import argparse



def connect():
    """Establishes a connection to the system's libvirt daemon"""
    try:
        conn = libvirt.open("qemu:///system")
        print("Connection to qemu:///system successful")
        return conn
    except libvirt.libvirtError as e:
        print(f"Failed to open connection to qemu:///system: {e}", file = sys.stderr)
        sys.exit(1)

def disconnect(conn):
    """Closes the connection to the libvirt daemon"""
    try:
        conn.close()
        print("Connection closed")
    except libvirt.libvirtError as e:
        print(f"Failed to close connection: {e}", file = sys.stderr)
    return

def get_domain_by_name(conn, name):
    """Finds and returns a VM domain by its name."""
    try:
        domain = conn.lookupByName(name)
        print(f"Domain {name} found")
        return domain
    except libvirt.libvirtError as e:
        print(f"Failed to find the domain {name} : {e}", file = sys.stderr)
        sys.exit(1)

def start_domain(conn, name):
    """Finds a VM by name and starts it."""
    try:
        domain = conn.lookupByName(name)
        if not domain.isActive():
            domain.create() 
            print(f"Domain '{name}' started successfully.")
        else:
            print(f"Domain '{name}' is already running.")
    except libvirt.libvirtError as e:
        print(f"Error starting domain '{name}': {e}", file=sys.stderr)

def shut_down_domain(conn, name):
    """Finds a VM by name and shuts it down."""
    try:
        domain = conn.lookupByName(name)
        if domain.isActive():
            domain.destroy() 
            print(f"Domain '{name}' has been shut down.")
        else:
            print(f"Domain '{name}' is not running.")
    except libvirt.libvirtError as e:
        print(f"Error shutting down domain '{name}': {e}", file=sys.stderr)

def list_vms(conn):
    """Lists all VMs, returning their name, state, and memory."""
    vms = []
    try:
        domains = conn.listAllDomains(0)
        if not domains:
            return [] 

        state_map = {
            libvirt.VIR_DOMAIN_NOSTATE: 'no state',
            libvirt.VIR_DOMAIN_RUNNING: 'running',
            libvirt.VIR_DOMAIN_BLOCKED: 'blocked',
            libvirt.VIR_DOMAIN_PAUSED: 'paused',
            libvirt.VIR_DOMAIN_SHUTDOWN: 'shutdown',
            libvirt.VIR_DOMAIN_SHUTOFF: 'shut off',
            libvirt.VIR_DOMAIN_CRASHED: 'crashed',
            libvirt.VIR_DOMAIN_PMSUSPENDED: 'pm-suspended',
        }

        for domain in domains:
            # domain.info() returns -> [state, maxMemory, memory, numVcpus, cpuTime]
            info = domain.info()
            state_code = info[0]
            memory_kb = info[2] # Memory is in KB

            vm_data = {
                'name': domain.name(),
                'state': state_map.get(state_code, 'unknown'), 
                'memory_mb': memory_kb / 1024 # Convert KB to MB
            }
            vms.append(vm_data)
        
        return vms
    except libvirt.libvirtError as e:
        print(f"Error listing VMs: {e}", file=sys.stderr)
        return None 



#conn = connect()
#domain = get_domain_by_name(conn, "ubuntu24.04")
#start_domain(domain)
#state, reason = domain.state()
#print(f"The state of '{domain.name()}' is: {state}")
#shut_down_domain(domain)
#disconnect(conn)

        