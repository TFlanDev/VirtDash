# KVM CLI Manager

A Python command-line tool to manage KVM virtual machines using the `libvirt` library.

## Features

* **List**: See all VMs, their state, and memory.
* **Start**: Turn on a VM.
* **Stop**: Shut down a VM.

## Setup

1.  **Make sure KVM and `libvirtd` are installed and running** on your Linux machine.

2.  **Install required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Give your user permission** to talk to libvirt. You'll probably need to log out and back in after running this.
    ```bash
    sudo usermod -aG libvirt $(whoami)
    ```

## Usage

All commands are run through `app.py`.

* **List all VMs:**
    ```bash
    python3 app.py list
    ```

* **Start a VM named `ubuntu24.04`:**
    ```bash
    python3 app.py start ubuntu24.04
    ```

* **Stop a VM named `ubuntu24.04`:**
    ```bash
    python3 app.py stop ubuntu24.04
    ```

## What's Next?

* **Web UI**: Build a simple web interface with fastAPI to manage VMs from a browser.
* **Create VMs**: Add a command to spin up new VMs from a golden image.
* **More Controls**: Add options for gracefully shutting down, pausing, or rebooting VMs.
