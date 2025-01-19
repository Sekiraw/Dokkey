# SPDX-License-Identifier: Apache-2.0
# Author: Peter Bohus

import dokkey
import threading
import time
import signal
import sys

key_count = 0
lock = threading.Lock()


# Define a Python callback
def on_key(vk_code):
    global key_count
    with lock:  # Ensure thread-safe increment
        key_count += 1
    print(f">>> Key pressed: {vk_code}")
    if vk_code == 27:  # Escape key
        dokkey.uninstall_hook()


# Function to print the key count every 5 seconds
def print_key_count():
    global key_count
    while True:
        time.sleep(5)
        with lock:
            print(f">>> Key count: {key_count}")


# Signal handler for graceful termination
def handle_exit_signal(signum, frame):
    print("\n>>> Terminating...")
    try:
        dokkey.uninstall_hook()
    except Exception as e:
        print(f">>> Error during cleanup: {e}")
    finally:
        sys.exit(0)


# Set up signal handling
signal.signal(signal.SIGINT, handle_exit_signal)
signal.signal(signal.SIGTERM, handle_exit_signal)

# Start the key count thread
thread = threading.Thread(target=print_key_count, daemon=True)
thread.start()

# Install the hook and run the message loop
try:
    dokkey.install_hook(on_key)
    dokkey.run_message_loop()
finally:
    print(">>> Cleaning up...")
    dokkey.uninstall_hook()