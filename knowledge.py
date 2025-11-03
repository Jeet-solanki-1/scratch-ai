class Knowledge:
    def __init__(self):
        """ Dfine some default knowledg base """
        self.fact={
            "name":"Scratch-ai",
            "creator":"JLSS",
            "version":"v1.0",
            "default_response":"I dit't learnt this yet. But if you teach me i will definatly learn it i am dedicated as JEET",
            "scratch_ai": """   I am Scratch_AI — as the name suggests, I am built independently.
                I am a logic-based AI, not trained on massive data. Like a human child, I learn day by day and build my own memory through experience.
                No external AI frameworks (like PyTorch or TensorFlow) were used by the developers at JLSS Corporation to build me — only pure logic and code.
                """,
                
        }
        
    def get_fact(self,key:str) -> str:
        """ retrive a value fact by key!"""
        return self.fact.get(key,None)
        
    def set_fact(self,key:str,value:str):
        """ set a key value pair in knowledge base."""
        """
         i got it now when the user set the fact , at the same time we have to add the logic to logic engine,
         as as of now we are not asuming to make complex english or math heavy work to understad user intent easily , we will do that in future phases
         but as of now i think this approch is quite good as user inputs facts we settle them in logic_engine to retrive teh new logic,
         ok i will also use hashing here. somehow to get intent of user or to pick seen facts easily. 
        """

        