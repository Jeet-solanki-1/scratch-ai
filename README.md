Scratch-ai is an ai made from scrath means not depended on any framework of pythone all work is doen from scrath, means starting from zero.
Nice — calm, low-level, practical design. I’ll lay out a tidy Phase-2 architecture (classes, responsibilities, method signatures only) and give you interface-only Python files you can drop into the repo and implement later. I’ll keep it KISS, DRY, and follow simple design patterns (Repository for persistence, Strategy for parsing, Command-like handlers for memory ops) — but in the smallest, most practical form.

I’ll first explain the pieces in plain language, then provide the file / class interfaces (with `pass`) you asked for.

# Phase 2 — Memory: architecture (LLD, interfaces only)

## Goals (short)

* Allow the AI to **learn** facts from user input.
* Persist facts between runs.
* Provide safe, discoverable operations: `get`, `set`, `delete`, `list`.
* Keep responsibilities separated so implementation can evolve.

## High-level components

1. **CLIInterface** — unchanged: input / output
2. **KeywordDetector** — unchanged, for quick detection
3. **Parser / IntentExtractor** — new: detect “teach” patterns (e.g. “my name is X”, “remember that X is Y”) and extract (key, value)
4. **MemoryRepository** (persistence) — new: simple repository that loads/saves JSON file (Repository pattern)
5. **MemoryManager** — new: business logic API around repository (get, set, delete, list). This is what LogicEngine calls.
6. **LogicEngine** — extended: handles learning intents, queries, and uses MemoryManager for facts.
7. **CommandHandler** — new (optional simple): high-level commands like `show memory`, `forget <k>`, `clear memory`.
8. **Models** — small dataclass for `Fact` if helpful.
9. **Serializer** — tiny interface if you want to swap JSON for other formats later.

## Design principles applied

* **KISS**: keep methods small and explicit.
* **SRP (Single Responsibility)**: repository only handles I/O; manager only handles business rules.
* **DRY**: memory operations centralized in `MemoryManager`.
* **Testability**: by depending on interfaces (repo, parser) you can mock easily.
* **Small design patterns**:

  * Repository for persistence (`MemoryRepository`).
  * Strategy for parsing (`IntentExtractor` can be swapped).
  * Command pattern spirit for memory commands (a `CommandHandler` that dispatches operations).

---

# Project structure (Phase 2 interfaces)

```
scratch-ai/
│
├── main.py
├── cli_interface.py
├── keyword_detector.py
├── parser.py               # Intent / fact extraction
├── memory_repository.py    # persistence interface
├── memory_manager.py       # business logic over repository
├── logic_engine.py         # extended logic engine (uses memory manager)
├── command_handler.py      # optional: explicit commands (show/forget/clear)
├── models.py               # small dataclasses (Fact)
├── serializer.py           # (optional) serialization interface
└── knowledge.py            # existing defaults (can be replaced by memory repo)
```

---

# Interfaces — code (all methods `pass` — implement later)

Below are ready-to-save files (interfaces only). Copy them into your project and run linter/CI — they won’t break main imports.

---

### `models.py`

```python
# models.py
from dataclasses import dataclass

@dataclass
class Fact:
    key: str
    value: str
```

---

### `serializer.py` (optional abstraction)

```python
# serializer.py
from typing import Dict, Any

class Serializer:
    def serialize(self, data: Dict[str, Any]) -> str:
        """Return a serialized string from data (e.g., JSON)."""
        pass

    def deserialize(self, payload: str) -> Dict[str, Any]:
        """Parse payload and return a dict."""
        pass
```

---

### `memory_repository.py`

```python
# memory_repository.py
from typing import Dict, Optional

class MemoryRepository:
    """
    Repository handling persistence of facts.
    Default implementation may use JSON file.
    """

    def __init__(self, path: str = "memory.json"):
        """
        Initialize repository with a file path (or other backend).
        """
        pass

    def load_all(self) -> Dict[str, str]:
        """Load all facts from persistent store; return dict[key]=value."""
        pass

    def save_all(self, facts: Dict[str, str]) -> None:
        """Persist the entire facts dictionary atomically."""
        pass

    def exists(self, key: str) -> bool:
        """Return True if key exists in persistent store (can be in-memory cache)."""
        pass
```

---

### `memory_manager.py`

```python
# memory_manager.py
from typing import Dict, Optional
from memory_repository import MemoryRepository

class MemoryManager:
    """
    Business logic around memory operations:
    - get_fact
    - set_fact
    - delete_fact
    - list_facts
    Keeps an in-memory cache and delegates persistence to MemoryRepository.
    """

    def __init__(self, repository: MemoryRepository):
        self.repository = repository
        pass

    def load(self) -> None:
        """Load facts from repository into local cache."""
        pass

    def get_fact(self, key: str) -> Optional[str]:
        """Return value for key or None."""
        pass

    def set_fact(self, key: str, value: str) -> None:
        """Set and persist a fact."""
        pass

    def delete_fact(self, key: str) -> bool:
        """Delete a fact; return True if deleted, False if not found."""
        pass

    def list_facts(self) -> Dict[str, str]:
        """Return a shallow copy of all facts."""
        pass

    def clear(self) -> None:
        """Clear all memory and persist reset state."""
        pass
```

---

### `parser.py` (Intent / Fact extraction)

```python
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
```

---

### `command_handler.py`

```python
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
```

---

### `logic_engine.py` (Phase 2 interface update)

```python
# logic_engine.py
from typing import List, Optional
from memory_manager import MemoryManager
from parser import IntentExtractor

class LogicEngine:
    """
    Decide responses. Uses IntentExtractor to parse user input and MemoryManager for facts.
    """

    def __init__(self, memory: MemoryManager, extractor: IntentExtractor):
        self.memory = memory
        self.extractor = extractor
        pass

    def decide_response(self, text: str) -> str:
        """
        Full-text entry point for Phase 2. It will:
          - ask the extractor for intent
          - for TEACH intent: call memory.set_fact and return confirmation
          - for QUERY intent: call memory.get_fact and format reply
          - for COMMAND intent: optionally delegate to CommandHandler
          - for UNKNOWN: fallback to default response
        """
        pass

    # minimal helper signatures
    def _handle_teach(self, key: str, value: str) -> str:
        pass

    def _handle_query(self, key: str) -> str:
        pass
```

---

### `memory_repository_json.py` (concrete repo example; interface file is above)

```python
# memory_repository_json.py
import json
import os
from typing import Dict
from memory_repository import MemoryRepository

class MemoryRepositoryJSON(MemoryRepository):
    """
    Simple JSON file-backed repository implementing MemoryRepository.
    """

    def __init__(self, path: str = "memory.json"):
        self.path = path
        pass

    def load_all(self) -> Dict[str, str]:
        pass

    def save_all(self, facts: Dict[str, str]) -> None:
        pass

    def exists(self, key: str) -> bool:
        pass
```

---

### `cli_interface.py` (ensure get_user_input returns str)

```python
# cli_interface.py
class CLIInterface:
    def get_user_input(self) -> str:
        """Prompt user and return text. Should never return None (return '' for empty)."""
        pass

    def show_response(self, response: str) -> None:
        """Print or display the AI response."""
        pass
```

---

### `keyword_detector.py` (keep as is — interface)

```python
# keyword_detector.py
class KeywordDetector:
    def __init__(self):
        pass

    def detect_keywords(self, text: str) -> list[str]:
        pass
```

---

## How these pieces interact (flow)

1. `main.py` reads raw input string from `CLIInterface`.
2. `LogicEngine.decide_response(text)` is called (no more passing keywords around).
3. `LogicEngine` asks `IntentExtractor.extract_intent(text)`:

   * If intent is TEACH: payload `{"key":..., "value":...}` → `MemoryManager.set_fact(...)` → return confirmation.
   * If intent is QUERY: payload `{"key":...}` → `MemoryManager.get_fact(...)` → format reply.
   * If intent is COMMAND: delegate to `CommandHandler`.
   * Else fallback to default or ask user to clarify.
4. `MemoryManager` maintains cache and delegates persistence to `MemoryRepository`.
5. `main.py` prints the response with `CLIInterface.show_response`.

## Extra small notes (implementation guidance for later)

* Keep the teach patterns simple initially (e.g., regex for `my NAME is VALUE`, `remember that KEY is VALUE`, `X is Y` with short keys).
* Persist immediately on `set_fact` to avoid losing memory on crash.
* Use atomic write (write to temp file then rename) when saving JSON for safety.
* Add `MemoryManager.load()` at program start to ensure memory initialized.
* Provide command `show memory` and `forget <key>` parsing in `CommandHandler` (or IntentExtractor can produce COMMAND intent).

---

If you want, I can:

* produce a single commit-ready patch (all these interface files created) you can drop in; **or**
* generate minimal example implementations for `MemoryRepositoryJSON` and `IntentExtractor` heuristics so you have a working Phase-2 skeleton immediately.

Which would you like next? (I’ll proceed calmly and implement just the parts you request.)
