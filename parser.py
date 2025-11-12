 #TODO Intent / fact extraction
# parser.py
from typing import Optional, Tuple

class Intent:
    """
    Simple enumeration-ish container for intents.
    For now: 'query', 'teach', 'command', 'unknown'
    """
    QUERY = "query"
    TEACH = "teach"
    COMMAND = "command"
    UNKNOWN = "unknown"

class IntentExtractor:
    """
    Small, replaceable strategy for extracting intent and facts from text.
    Exposes:
      - extract_intent(text) -> (intent, payload)
      - For TEACH intent, payload could be (key, value)
    """

    def __init__(self):
        pass

    def extract_intent(self, text: str) -> Tuple[str, Optional[dict]]:
        """
        Inspect text and return (intent, payload)
        payload examples:
          - query: {"key": "name"}
          - teach: {"key": "name", "value": "Jeet"}
          - command: {"cmd": "show_memory"}
          - unknown: None
        """
        pass

    # helper methods you might implement later
    def _detect_teach(self, text: str) -> Optional[Tuple[str, str]]:
        """Return (key, value) if text matches teach pattern, else None."""
        pass

    def _detect_query(self, text: str) -> Optional[str]:
        """Return key if text matches a query pattern, else None."""
        pass
