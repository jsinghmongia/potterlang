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
        print(f"Error: {e}", file=sys.stderr)

def repl():
    print("PotterLang 1.0.0 Interactive REPL")
    print("Enter 'AvadaKedavra' or press Ctrl+C to exit.")
    env = Environment()
    while True:
        try:
            line = input(">>> ")
            if not line.strip():
                continue
            run(line, env)
        except (KeyboardInterrupt, EOFError):
            print("\nExiting.")
            break

def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                code = f.read()
            run(code, Environment())
        except FileNotFoundError:
            print(f"Error: File '{filepath}' not found.", file=sys.stderr)
            sys.exit(1)
    else:
        repl()

if __name__ == "__main__":
    main()