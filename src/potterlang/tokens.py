from enum import Enum, auto

class TokenType(Enum):
    # Keywords
    ACCIO = auto()          # Variable declaration
    LUMOS = auto()          # Output
    RIDDIKULUS = auto()     # If
    FINITE = auto()         # Else
    TIMETURNER = auto()     # While
    AVADAKEDAVRA = auto()   # Exit / Halt
    INCANTATION = auto()    # Function def
    EXPECTOPATRONUM = auto()# Return
    LEGILIMENS = auto()     # Input
    PROTEGO = auto()        # Try
    CRUCIO = auto()         # Catch

    # Literals
    IDENTIFIER = auto()
    NUMBER = auto()
    STRING = auto()
    BOOLEAN = auto()

    # Operators
    ASSIGN = auto()         # =
    PLUS = auto()           # +
    MINUS = auto()          # -
    STAR = auto()           # *
    SLASH = auto()          # /
    EQ = auto()             # ==
    NEQ = auto()            # !=
    GT = auto()             # >
    LT = auto()             # <
    GTE = auto()            # >=
    LTE = auto()            # <=

    # Delimiters
    LPAREN = auto()         # (
    RPAREN = auto()         # )
    LBRACE = auto()         # {
    RBRACE = auto()         # }
    LBRACKET = auto()       # [
    RBRACKET = auto()       # ]
    COMMA = auto()          # ,

    EOF = auto()

class Token:
    def __init__(self, type_: TokenType, value, line: int):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"Token({self.type.name}, {repr(self.value)}, line={self.line})"