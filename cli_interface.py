class CLIInterface:
    def get_user_input(self) -> str:
        """ prompt the user to input a str"""
        return input("you: ")
       
    def show_response(self,response:str):
        """print the response of ai to the user"""
        print(f"Ai: {response}")
   