import re
from .tokens import TokenType, Token

KEYWORDS = {
    "Accio": TokenType.ACCIO,
    "Lumos": TokenType.LUMOS,
    "Riddikulus": TokenType.RIDDIKULUS,
    "Finite": TokenType.FINITE,
    "TimeTurner": TokenType.TIMETURNER,
    "AvadaKedavra": TokenType.AVADAKEDAVRA,
    "Incantation": TokenType.INCANTATION,
    "ExpectoPatronum": TokenType.EXPECTOPATRONUM,
    "Legilimens": TokenType.LEGILIMENS,
    "Protego": TokenType.PROTEGO,
    "Crucio": TokenType.CRUCIO,
    "true": TokenType.BOOLEAN,
    "false": TokenType.BOOLEAN,
}

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.tokens = []
        self.line = 1

    def tokenize(self):
        token_specs = [
            ("COMMENT",    r"//[^\n]*"),
            ("STRING",     r'"([^"\\]|\\.)*"'),
            ("NUMBER",     r"\b\d+(\.\d+)?\b"),
            ("GTE",        r">="),
            ("LTE",        r"<="),
            ("EQ",         r"=="),
            ("NEQ",        r"!="),
            ("IDENT",      r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
            ("ASSIGN",     r"="),
            ("PLUS",       r"\+"),
            ("MINUS",      r"-"),
            ("STAR",       r"\*"),
            ("SLASH",      r"/"),
            ("GT",         r">"),
            ("LT",         r"<"),
            ("LPAREN",     r"\("),
            ("RPAREN",     r"\)"),
            ("LBRACE",     r"\{"),
            ("RBRACE",     r"\}"),
            ("LBRACKET",   r"\["),
            ("RBRACKET",   r"\]"),
            ("COMMA",      r","),
            ("NEWLINE",    r"\n"),
            ("SKIP",       r"[ \t\r]+"),
            ("MISMATCH",   r"."),
        ]
        tok_regex = "|".join(f"(?P<{pair[0]}>{pair[1]})" for pair in token_specs)

        for mo in re.finditer(tok_regex, self.source):
            kind = mo.lastgroup
            val = mo.group()

            if kind == "NEWLINE":
                self.line += 1
            elif kind in ("SKIP", "COMMENT"):
                continue
            elif kind == "NUMBER":
                self.tokens.append(Token(TokenType.NUMBER, float(val) if '.' in val else int(val), self.line))
            elif kind == "STRING":
                self.tokens.append(Token(TokenType.STRING, val[1:-1], self.line))
            elif kind == "IDENT":
                tok_type = KEYWORDS.get(val, TokenType.IDENTIFIER)
                actual_val = True if val == "true" else False if val == "false" else val
                self.tokens.append(Token(tok_type, actual_val, self.line))
            elif kind == "MISMATCH":
                raise SyntaxError(f"HowlerError: Unknown magical rune '{val}' at line {self.line}")
            else:
                self.tokens.append(Token(TokenType[kind], val, self.line))

        self.tokens.append(Token(TokenType.EOF, None, self.line))
        return self.tokens