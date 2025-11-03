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

    """
    ********Note- we will use try catch bloaks to make robustness in our ai runtime, like errors unexpected ones later, but as of now it is as simple as it understandable.***********
    def main():
    cli = CLIInterface()
    logic = LogicEngine()
    kb = Knowledge()
    detector = KeywordDetector()

    while True:
        try:
            user_input = cli.get_user_input()
            if not user_input:
                continue  # skip empty input

            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye!")
                break

            keywords = detector.detect_keywords(user_input)
            response = logic.decide_response(keywords, kb)
            cli.show_response(response)

        except KeyboardInterrupt:
            # Handles Ctrl+C gracefully
            print("\n[System]: Program interrupted by user. Exiting safely.")
            break

        except Exception as e:
            # Catches unexpected errors, so the program does not crash
            print(f"[Error]: {e}")

"""