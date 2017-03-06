# coding=utf-8

""" AST (abstract syntax tree : 抽象構文木) """

from expr_nodes import *

class AstGenerator(object):

    def __init__(self):
        self.symbol_table = {}

    # unary operators
    def make_unary_op(self, tokens=None):
        tokens = tokens.asList()[0]
        op = tokens[0]
        _op_map = {
            '-': Neg
        }
        cls = _op_map[op]
        return cls(op, tokens[1])

    # binary operators
    def make_binary_op(self, tokens=None):
        _op_map = {
            '+': Add,
            '-': Sub,
            '*': Mult,
            '/': Div,
        }

        def convert(l):
            stack = []
            l = iter(l)
            for e in l:
                if e in _op_map:
                    cls = _op_map[e]
                    left = stack.pop()
                    right = next(l)
                    stack.append(cls(left, e, right))
                else:
                    stack.append(e)
            return stack.pop()

        tokens = tokens.asList()[0]
        return convert(tokens)

    def calc(self, node):
        #print(type(node))
        if isinstance(node, str):
            return int(node)
        elif isinstance(node, Neg): # unary operator
            return -1 * self.calc(node.right)
        elif isinstance(node, Add): # binary operator
            return self.calc(node.left) + self.calc(node.right)
        elif isinstance(node, Sub):
            return self.calc(node.left) - self.calc(node.right)
        elif isinstance(node, Mult):
            return self.calc(node.left) * self.calc(node.right)
        elif isinstance(node, Div):
            return self.calc(node.left) / self.calc(node.right)
        else:
            raise Exception("ASTCalcException : " + str(node))

