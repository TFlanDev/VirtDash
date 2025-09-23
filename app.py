import argparse
import hypervisor

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A CLI tool to manage KVM virtual machines.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Sub-command for 'list'
    parser_list = subparsers.add_parser("list", help="List all virtual machines.")
    
    # Sub-command for 'start'
    parser_start = subparsers.add_parser("start", help="Start a virtual machine.")
    parser_start.add_argument("vm_name", type=str, help="Name of the VM to start.")

    # Sub-command for 'stop'
    parser_stop = subparsers.add_parser("stop", help="Stop a virtual machine.")
    parser_stop.add_argument("vm_name", type=str, help="Name of the VM to stop.")
    
    args = parser.parse_args()
    
    conn = hypervisor.connect()
    if not conn:
        exit(1) # Exit if connection failed

    if args.command == "list":
        all_vms = hypervisor.list_vms(conn)
        if all_vms:
            print(f"{'Name':<20} {'State':<15} {'Memory (MB)':<15}")
            print("-" * 50)
            for vm in all_vms:
                print(f"{vm['name']:<20} {vm['state']:<15} {vm['memory_mb']:.0f}")
        else:
            print("No virtual machines found.")

    elif args.command == "start":
        hypervisor.start_domain(conn, args.vm_name)

    elif args.command == "stop":
        hypervisor.shut_down_domain(conn, args.vm_name)
    
    hypervisor.disconnect(conn)