# SPDX-License-Identifier: Apache-2.0
# Author: Peter Bohus

import signal
import dokkey

def cleanup_and_exit(signum, frame):
    try:
        dokkey.uninstall_hook()
    except Exception as e:
        print(f">>> Error during cleanup: {e}")
    finally:
        print(">>> Exiting gracefully.")
        exit(0)

signal.signal(signal.SIGINT, cleanup_and_exit)

# Install the hook and run the message loop
def on_key_press(key_code):
    print(f">>> Key pressed: {key_code}")

print("Listening for key presses. Press Ctrl+C to stop.")
try:
    dokkey.install_hook(on_key_press)
    dokkey.run_message_loop()
except Exception as e:
    print(f">>> Error: {e}")
finally:
    dokkey.uninstall_hook()
