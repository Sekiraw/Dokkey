from typing import Callable

def install_hook(callback: Callable[[int], None]) -> None:
    """Install a keyboard hook.

    Args:
        callback: A Python function to call on key press, receiving the virtual key code as an argument.
    """
    ...

def uninstall_hook() -> None:
    """Uninstall the keyboard hook."""
    ...

def run_message_loop() -> None:
    """Run the Windows message loop."""
    ...
