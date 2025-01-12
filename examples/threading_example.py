import dokkey
import threading
import time

key_count = 0
lock = threading.Lock()


# Define a Python callback
def on_key(vk_code):
    global key_count
    with lock:  # Ensure thread-safe increment
        key_count += 1
    print(f"Key pressed: {vk_code}")
    if vk_code == 27:  # Escape key
        dokkey.uninstall_hook()


# Function to print the key count every 5 seconds
def print_key_count():
    global key_count
    while True:
        time.sleep(5)
        with lock:
            print(f"Key count: {key_count}")


thread = threading.Thread(target=print_key_count, daemon=True)
thread.start()

dokkey.install_hook(on_key)
dokkey.run_message_loop()
