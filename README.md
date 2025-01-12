# Dokkey

**Dokkey** is a Python package designed to detect keypresses on Windows. It captures keyboard input and returns the ASCII code of the key pressed. This package has been tested on **Windows 11**.

---

## Features

- Detects keypresses on Windows.
- Returns the ASCII code of the key pressed.
- Lightweight and easy to integrate into your projects.

---

## Requirements

- Python 3.7 or higher
- Windows OS (Tested on Windows 11)

---

## Installation

Install the package using pip:

```bash
pip install dokkey
```

## Usage
Here is an example of how to use Dokkey:

```python
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
```
## Output Example
```plaintext
Listening for key presses. Press Ctrl+C to stop.
Key pressed: 65  # (A key)
Key pressed: 98  # (b key)
```

## How It Works
Dokkey leverages Windows APIs to capture global keyboard events and converts the input to ASCII codes. It ensures minimal interference with other running applications.

## Limitations
This package works only on Windows.
It may require administrator privileges for certain use cases.
## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Developed by Sekiraw

## Acknowledgements
Thanks to the Python and Windows development communities for providing tools and resources to make this project possible.

```vbnet
This styling ensures clarity, proper sectioning, and good readability. Let me know if you`d like any further adjustments!
```
