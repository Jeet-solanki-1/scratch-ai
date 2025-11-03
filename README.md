Scratch-ai is an ai made from scrath means not depended on any framework of pythone all work is doen from scrath, means starting from zero.

## Current Phase — Phase 1: Foundation of Logic

### Objective

Establish a minimal but complete working core using **pure Python** and **logical reasoning** only.

### Completed

* Defined modular project structure
* Built CLI-based interaction loop
* Implemented keyword detection via regex
* Designed logic engine to produce responses
* Created internal knowledge base
* Handled runtime errors safely (graceful exit and exception catching)

---

## Project Structure

```
scratch-ai/
│
├── main.py                # Entry point — connects all core modules
├── cli_interface.py       # Handles user input and output
├── keyword_detector.py    # Detects keywords or phrases from text
├── logic_engine.py        # Core reasoning layer that decides responses
├── knowledge.py           # Internal knowledge store (facts and memory)
└── README.md              # Project documentation
```

---

## How It Works

**Flow of interaction:**

```
User → CLIInterface → KeywordDetector → LogicEngine → KnowledgeBase → Response
```

### Step-by-step:

1. The user types a query.
2. The detector scans it for known words or patterns.
3. The logic engine interprets the detected intent.
4. The knowledge base returns relevant information.
5. The response is displayed to the user.

---

## Example Dialogue

```
you: what is your name?
Scratch_AI: My name is junior_ai.

you: who created you?
Scratch_AI: I am created by Mr.JLSS.

you: what is scratch_ai?
Scratch_AI:
I am Scratch_AI — as the name suggests, I am built independently.
I am a logic-based AI, not trained on massive data.
Like a human child, I learn day by day and build my own memory through experience.
No external frameworks (like PyTorch or TensorFlow) were used by the developers at JLSS Corporation to build me — only pure logic and code.
```

---

## Design Core

| Layer               | Role                              | Analogy                |
| ------------------- | --------------------------------- | ---------------------- |
| **KnowledgeBase**   | Stores facts and static responses | Long-term memory       |
| **LogicEngine**     | Processes reasoning rules         | Thought process        |
| **KeywordDetector** | Identifies cues from text         | Ears and comprehension |
| **CLIInterface**    | Handles human interaction         | Mouth and ears         |

---

## Principles of Growth

> Scratch-AI should not be taught *what* to think.
> It should be taught *how* to think.

Each new phase adds an evolutionary layer — like how a human brain develops:

* Memory and recall
* Context understanding
* Intent inference
* Reasoning across unknowns
* Self-learning

---

## Running the Program

To start Scratch-AI:

```bash
python main.py
```

Example queries:

```
what is your name?
who created you?
```

To exit:

```
quit
```

or press `Ctrl + C`.

---
