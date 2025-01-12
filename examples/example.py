# SPDX-License-Identifier: Apache-2.0

import dokkey

# Define a Python callback
def on_key(vk_code):
    print(f"Key pressed: {vk_code}")
    if vk_code == 27: # (esc)
        print("Stop")
        dokkey.uninstall_hook()
        print("Stopped")

dokkey.install_hook(on_key)

dokkey.run_message_loop()