class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VarDeclNode(ASTNode):
    def __init__(self, name: str, expr):
        self.name = name
        self.expr = expr

class VarAssignNode(ASTNode):
    def __init__(self, name: str, expr):
        self.name = name
        self.expr = expr

class PrintNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class IfNode(ASTNode):
    def __init__(self, condition, then_branch, else_branch=None):
        self.condition = condition
        self.then_branch = then_branch
        self.else_branch = else_branch

class WhileNode(ASTNode):
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class FunctionDefNode(ASTNode):
    def __init__(self, name: str, params: list, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode(ASTNode):
    def __init__(self, name: str, args: list):
        self.name = name
        self.args = args

class ReturnNode(ASTNode):
    def __init__(self, expr):
        self.expr = expr

class InputNode(ASTNode):
    def __init__(self, prompt_expr):
        self.prompt_expr = prompt_expr

class ArrayLiteralNode(ASTNode):
    def __init__(self, elements: list):
        self.elements = elements

class IndexAccessNode(ASTNode):
    def __init__(self, target, index):
        self.target = target
        self.index = index

class TryCatchNode(ASTNode):
    def __init__(self, try_block, error_var: str, catch_block):
        self.try_block = try_block
        self.error_var = error_var
        self.catch_block = catch_block

class BinaryOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class LiteralNode(ASTNode):
    def __init__(self, value):
        self.value = value

class VariableNode(ASTNode):
    def __init__(self, name: str):
        self.name = name

class HaltNode(ASTNode):
    pass