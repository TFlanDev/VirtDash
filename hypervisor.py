import libvirt
import sys

def connect():
    try:
        conn = libvirt.open("qemu:///system")
        print("Connection to qemu:///system successful")
        return conn
    except libvirt.libvirtError as e:
        print(f"Failed to open connection to qemu:///system: {e}", file = sys.stderr)
        sys.exit(1)

def disconnect(conn):
    try:
        conn.close()
        print("Connection closed")
    except libvirt.libvirtError as e:
        print(f"Failed to close connection: {e}", file = sys.stderr)
    return

def get_domain_by_name(conn, name):
    try:
        domain = conn.lookupByName(name)
        print(f"Domain {name} found")
        return domain
    except libvirt.libvirtError as e:
        print(f"Failed to find the domain {name} : {e}", file = sys.stderr)
        sys.exit(1)
def shut_down_domain(domain):
    try:
        domain.destroy()
        print(f"Kill signal sent to domain {domain.name()}")
    except libvirt.libvirtError as e:
        print(f"Failed to shutdown the domain {domain.name()} : {e}", file = sys.stderr)
        sys.exit(1)
def start_domain(domain):
    try:
        domain.create()
        print(f"Domain {domain.name()} started")
    except libvirt.libvirtError as e:
        print(f"Failed to start the domain {domain.name()} : {e}", file = sys.stderr)
        sys.exit(1)



conn = connect()
domain = get_domain_by_name(conn, "ubuntu24.04")
start_domain(domain)
state, reason = domain.state()
print(f"The state of '{domain.name()}' is: {state}")
shut_down_domain(domain)
disconnect(conn)

        