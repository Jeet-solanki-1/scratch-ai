from cli_interface import CLIInterface
from logic_engine import LogicEngine
from knowledge import Knowledge
from keyword_detector import KeywordDetector

def main():
    cli = CLIInterface()
    logic = LogicEngine()
    kb = Knowledge()
    detector = KeywordDetector()
    while True:
        user_input = cli.get_user_input()
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye!")
            break


        keywords = detector.detect_keywords(user_input)
        response = logic.decide_response(keywords,kb)
        """now print the response"""
        cli.show_response(response)

if __name__ == "__main__":
    main()