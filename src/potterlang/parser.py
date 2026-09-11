from .tokens import TokenType
from .ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def match(self, *types):
        if self.current().type in types:
            tok = self.current()
            self.pos += 1
            return tok
        return None

    def expect(self, token_type):
        tok = self.match(token_type)
        if not tok:
            curr = self.current()
            raise SyntaxError(f"Expected token {token_type.name}, found {curr.type.name} at line {curr.line}")
        return tok

    def parse(self):
        statements = []
        while self.current().type != TokenType.EOF:
            statements.append(self.parse_statement())
        return ProgramNode(statements)

    def parse_statement(self):
        if self.match(TokenType.ACCIO):
            ident = self.expect(TokenType.IDENTIFIER)
            self.expect(TokenType.ASSIGN)
            return VarDeclNode(ident.value, self.parse_expression())

        if self.match(TokenType.LUMOS):
            return PrintNode(self.parse_expression())

        if self.match(TokenType.EXPECTOPATRONUM):
            return ReturnNode(self.parse_expression())

        if self.match(TokenType.AVADAKEDAVRA):
            return HaltNode()

        if self.match(TokenType.INCANTATION):
            name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.LPAREN)
            params = []
            if self.current().type != TokenType.RPAREN:
                params.append(self.expect(TokenType.IDENTIFIER).value)
                while self.match(TokenType.COMMA):
                    params.append(self.expect(TokenType.IDENTIFIER).value)
            self.expect(TokenType.RPAREN)
            body = self.parse_block()
            return FunctionDefNode(name, params, body)

        if self.match(TokenType.RIDDIKULUS):
            self.expect(TokenType.LPAREN)
            cond = self.parse_expression()
            self.expect(TokenType.RPAREN)
            then_b = self.parse_block()
            else_b = self.parse_block() if self.match(TokenType.FINITE) else None
            return IfNode(cond, then_b, else_b)

        if self.match(TokenType.TIMETURNER):
            self.expect(TokenType.LPAREN)
            cond = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return WhileNode(cond, self.parse_block())

        if self.match(TokenType.PROTEGO):
            try_b = self.parse_block()
            self.expect(TokenType.CRUCIO)
            self.expect(TokenType.LPAREN)
            err_var = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.RPAREN)
            catch_b = self.parse_block()
            return TryCatchNode(try_b, err_var, catch_b)

        expr = self.parse_expression()
        if isinstance(expr, VariableNode) and self.match(TokenType.ASSIGN):
            val = self.parse_expression()
            return VarAssignNode(expr.name, val)
        return expr

    def parse_block(self):
        self.expect(TokenType.LBRACE)
        statements = []
        while self.current().type not in (TokenType.RBRACE, TokenType.EOF):
            statements.append(self.parse_statement())
        self.expect(TokenType.RBRACE)
        return BlockNode(statements)

    def parse_expression(self):
        return self.parse_comparison()

    def parse_comparison(self):
        node = self.parse_term()
        while True:
            op = self.match(TokenType.EQ, TokenType.NEQ, TokenType.GT, TokenType.LT, TokenType.GTE, TokenType.LTE)
            if not op:
                break
            node = BinaryOpNode(node, op.type, self.parse_term())
        return node

    def parse_term(self):
        node = self.parse_factor()
        while True:
            op = self.match(TokenType.PLUS, TokenType.MINUS)
            if not op:
                break
            node = BinaryOpNode(node, op.type, self.parse_factor())
        return node

    def parse_factor(self):
        node = self.parse_postfix()
        while True:
            op = self.match(TokenType.STAR, TokenType.SLASH)
            if not op:
                break
            node = BinaryOpNode(node, op.type, self.parse_postfix())
        return node

    def parse_postfix(self):
        node = self.parse_primary()
        while True:
            if self.match(TokenType.LBRACKET):
                index = self.parse_expression()
                self.expect(TokenType.RBRACKET)
                node = IndexAccessNode(node, index)
            elif isinstance(node, VariableNode) and self.match(TokenType.LPAREN):
                args = []
                if self.current().type != TokenType.RPAREN:
                    args.append(self.parse_expression())
                    while self.match(TokenType.COMMA):
                        args.append(self.parse_expression())
                self.expect(TokenType.RPAREN)
                node = FunctionCallNode(node.name, args)
            else:
                break
        return node

    def parse_primary(self):
        if tok := self.match(TokenType.NUMBER, TokenType.STRING, TokenType.BOOLEAN):
            return LiteralNode(tok.value)

        if self.match(TokenType.LEGILIMENS):
            self.expect(TokenType.LPAREN)
            prompt = self.parse_expression() if self.current().type != TokenType.RPAREN else LiteralNode("")
            self.expect(TokenType.RPAREN)
            return InputNode(prompt)

        if self.match(TokenType.LBRACKET):
            elements = []
            if self.current().type != TokenType.RBRACKET:
                elements.append(self.parse_expression())
                while self.match(TokenType.COMMA):
                    elements.append(self.parse_expression())
            self.expect(TokenType.RBRACKET)
            return ArrayLiteralNode(elements)

        if tok := self.match(TokenType.IDENTIFIER):
            return VariableNode(tok.value)

        if self.match(TokenType.LPAREN):
            node = self.parse_expression()
            self.expect(TokenType.RPAREN)
            return node

        raise SyntaxError(f"Unexpected token '{self.current().value}' at line {self.current().line}")