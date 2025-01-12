import dokkey

# Define a Python callback
def on_key(vk_code):
    print(f"Key pressed: {vk_code}")

# Install the hook
dokkey.install_hook(on_key)

try:
    print("Listening for key presses. Press Ctrl+C to stop.")
    dokkey.run_message_loop()
except KeyboardInterrupt:
    dokkey.uninstall_hook()
    print("Stopped.")
