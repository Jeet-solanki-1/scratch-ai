import re

class KeywordDetector:
    def __init__(self):
        self.keywords = ["what","who","name","creator","version"]

    def detect_keywords(self, text:str) -> list[str]:
        found = []
        text = text.lower()
        for kw in self.keywords:
            if re.search(r"\b"+ re.escape(kw) +r"\b",text):
                found.append(kw)

        return found

     
    