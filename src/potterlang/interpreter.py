import sys
from .tokens import TokenType
from .ast_nodes import *
from .environment import Environment

class ReturnTrigger(Exception):
    def __init__(self, value):
        self.value = value

class PotterFunction:
    def __init__(self, name: str, params: list, body, closure_env: Environment):
        self.name = name
        self.params = params
        self.body = body
        self.closure_env = closure_env

    def call(self, interpreter, args):
        if len(args) != len(self.params):
            raise TypeError(f"Function '{self.name}' expected {len(self.params)} arguments, got {len(args)}.")
        local_env = Environment(parent=self.closure_env)
        for param, arg in zip(self.params, args):
            local_env.values[param] = arg
        try:
            return interpreter.evaluate(self.body, local_env)
        except ReturnTrigger as ret:
            return ret.value

class Interpreter:
    def evaluate(self, node, env: Environment):
        if isinstance(node, ProgramNode):
            res = None
            for stmt in node.statements:
                res = self.evaluate(stmt, env)
            return res

        if isinstance(node, LiteralNode):
            return node.value

        if isinstance(node, VariableNode):
            return env.get(node.name)

        if isinstance(node, VarDeclNode):
            val = self.evaluate(node.expr, env)
            env.define(node.name, val)
            return val

        if isinstance(node, VarAssignNode):
            val = self.evaluate(node.expr, env)
            env.assign(node.name, val)
            return val

        if isinstance(node, PrintNode):
            val = self.evaluate(node.expr, env)
            print(val)
            return val

        if isinstance(node, InputNode):
            prompt = self.evaluate(node.prompt_expr, env)
            user_val = input(str(prompt))
            try:
                return float(user_val) if '.' in user_val else int(user_val)
            except ValueError:
                return user_val

        if isinstance(node, ArrayLiteralNode):
            return [self.evaluate(elem, env) for elem in node.elements]

        if isinstance(node, IndexAccessNode):
            target = self.evaluate(node.target, env)
            idx = self.evaluate(node.index, env)
            try:
                return target[idx]
            except IndexError:
                raise IndexError(f"Index {idx} out of bounds.")

        if isinstance(node, FunctionDefNode):
            func = PotterFunction(node.name, node.params, node.body, env)
            env.define(node.name, func)
            return func

        if isinstance(node, FunctionCallNode):
            func = env.get(node.name)
            if not isinstance(func, PotterFunction):
                raise TypeError(f"'{node.name}' is not callable.")
            args = [self.evaluate(arg, env) for arg in node.args]
            return func.call(self, args)

        if isinstance(node, ReturnNode):
            val = self.evaluate(node.expr, env)
            raise ReturnTrigger(val)

        if isinstance(node, HaltNode):
            sys.exit(0)

        if isinstance(node, BlockNode):
            child_env = Environment(parent=env)
            res = None
            for stmt in node.statements:
                res = self.evaluate(stmt, child_env)
            return res

        if isinstance(node, IfNode):
            if self.evaluate(node.condition, env):
                return self.evaluate(node.then_branch, env)
            elif node.else_branch:
                return self.evaluate(node.else_branch, env)
            return None

        if isinstance(node, WhileNode):
            while self.evaluate(node.condition, env):
                self.evaluate(node.body, env)
            return None

        if isinstance(node, TryCatchNode):
            try:
                return self.evaluate(node.try_block, env)
            except Exception as ex:
                catch_env = Environment(parent=env)
                catch_env.define(node.error_var, str(ex))
                return self.evaluate(node.catch_block, catch_env)

        if isinstance(node, BinaryOpNode):
            left = self.evaluate(node.left, env)
            right = self.evaluate(node.right, env)
            if node.op == TokenType.PLUS: return left + right
            if node.op == TokenType.MINUS: return left - right
            if node.op == TokenType.STAR: return left * right
            if node.op == TokenType.SLASH: return left / right
            if node.op == TokenType.GT: return left > right
            if node.op == TokenType.LT: return left < right
            if node.op == TokenType.GTE: return left >= right
            if node.op == TokenType.LTE: return left <= right
            if node.op == TokenType.EQ: return left == right
            if node.op == TokenType.NEQ: return left != right

        raise RuntimeError(f"Unhandled AST node: {type(node).__name__}")