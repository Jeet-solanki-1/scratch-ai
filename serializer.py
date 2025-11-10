 #TODO (optional) serialization interface
 """
 # serializer.py
from typing import Dict, Any

class Serializer:
    def serialize(self, data: Dict[str, Any]) -> str:
        Return a serialized string from data (e.g., JSON).
        pass

    def deserialize(self, payload: str) -> Dict[str, Any]:
       Parse payload and return a dict
        pass
"""
from typing import Dict, Any
class Serializer:
    def serialize(self,data:Dict[str,Any]) -> str:
        pass
    def deserialize(self,payload:str) -> Dict[str,Any]:
        pass
