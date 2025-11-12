from typing import List, Optional
from memory_manager import MemoryManager
from parser import IntentExtractor

class LogicEngine:
    # TODO extended logic engine (uses memory manager)

    def __init__(self, memory: MemoryManager, extractor: IntentExtractor):
        self.memory = memory
        self.extractor = extractor
        pass

    def decide_response(self, keywords:list[str],kb) -> str:
            """ 
            return a response string based on rules
            take the keywords detected from detecor and 
            you also gine a kb instance so use it make logics rules perform them on keywords and 
            then return a value from kb , kb = knowledge base of ai or small emdeing as of now.
            
            """

            if "name" in keywords:
                return f"My name is {kb.get_fact('name')}."
            elif "version" in keywords:
                return f"My current version is {kb.get_fact('version')}."
            elif "creator" in keywords or "who" in keywords:
                return f"I am created by Mr.{kb.get_fact('creator')}."
            elif "what" in keywords:
                return f"{kb.get_fact('scratch_ai')}."
            else:
                return f"{kb.get_fact('default_response')}."

    
        """
        Full-text entry point for Phase 2. It will:
          - ask the extractor for intent
          - for TEACH intent: call memory.set_fact and return confirmation
          - for QUERY intent: call memory.get_fact and format reply
          - for COMMAND intent: optionally delegate to CommandHandler
          - for UNKNOWN: fallback to default response
        """
     # minimal helper signatures
    def _handle_teach(self, key: str, value: str) -> str:
        pass

    def _handle_query(self, key: str) -> str:
        pass

    """ 
    ******we will try the below apprch later but for readablity adn giving idea of what we are gonna do i am continue with if else!*****
    """
    """
    rules = {
         "name": lambda kb: f"My name is {kb.get_fact('name')}.",
        "version": lambda kb: f"My current version is {kb.get_fact('version')}.",
        "who": lambda kb: f"I am created by Mr.{kb.get_fact('creator')}."
        }

    for kw in keywords:
        if kw in rules:
        return rules[kw](kb)
    return kb.get_fact("default_response")
    """

