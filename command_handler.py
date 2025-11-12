#TODO optional: explicit commands (show/forget/clear)
# command_handler.py
from typing import Optional, Dict
from memory_manager import MemoryManager

class CommandHandler:
    """
    Handle explicit commands (show memory, forget X, clear memory).
    Keeps command parsing separate from general language parsing.
    """

    def __init__(self, memory: MemoryManager):
        self.memory = memory
        pass

    def handle(self, text: str) -> Optional[str]:
        """
        If text is a command, perform it and return a user-facing reply string.
        Return None if text is not a command.
        """
        pass

    def _cmd_show_memory(self) -> str:
        """Return nicely formatted memory listing."""
        pass

    def _cmd_forget(self, key: str) -> str:
        """Forget a fact and return confirmation message."""
        pass

    def _cmd_clear(self) -> str:
        """Clear memory and return confirmation."""
        pass
