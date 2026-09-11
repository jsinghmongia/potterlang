import sys
from .lexer import Lexer
from .parser import Parser
from .interpreter import Interpreter
from .environment import Environment

def run(code: str, env: Environment):
    try:
        tokens = Lexer(code).tokenize()
        ast = Parser(tokens).parse()
        Interpreter().evaluate(ast, env)
    except Exception as e:
        print(f"\033[91m{e}\033[0m")

def repl():
    print("\033[93m--- The Sorting Hat REPL (PotterLang v1.0) ---")
    print("Type your incantations. Use 'AvadaKedavra' or Ctrl+C to exit.\033[0m")
    env = Environment()
    while True:
        try:
            line = input("🪄 > ")
            if not line.strip():
                continue
            run(line, env)
        except (KeyboardInterrupt, EOFError):
            print("\nMischief Managed.")
            break

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        with open(filepath, "r") as f:
            code = f.read()
        run(code, Environment())
    else:
        repl()

if __name__ == "__main__":
    main()