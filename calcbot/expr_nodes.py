# coding=utf-8

""" ノードたち """

class ASTNode(object):
    SPACER = " "
    _fields = ()

    def __repr__(self):
        return "{}({})".format(
            self.__class__.__name__,
            ', '.join(["%s=%s" % (field, getattr(self, field)) for field in self._fields])
        )

    def _p(self, v, indent):
        print("{}{}".format(self.SPACER * indent, v))

    def dumps(self, indent=0):
        self._p(self.__class__.__name__ + '(', indent)
        for field in self._fields:
            self._p(field + '=', indent + 1)
            value = getattr(self, field)
            if type(value) == list:
                for value2 in value:
                    if isinstance(value2, ASTNode):
                        value2.dumps(indent + 2)
                    else:
                        self._p(value2, indent + 2)
            else:
                if value:
                    if isinstance(value, ASTNode):
                        value.dumps(indent + 2)
                    else:
                        self._p(value, indent + 2)
        self._p(')', indent)

# Variables
# Expressions
class Expr(ASTNode):
    _fields = ('value', )
    def __init__(self, value):
        self.value = value


# unary operators
class UnaryOp(ASTNode):
    _fields = ('op', 'right')
    def __init__(self, op, right):
        self.op = op
        self.right = right

class Neg(UnaryOp):
    pass


# binary operators
class BinOp(ASTNode):
    _fields = ('left', 'right')
    def __init__(self, left, op, right):
        self.left = left
        self.right = right

class Add(BinOp):
    pass

class Sub(BinOp):
    pass

class Mult(BinOp):
    pass

class Div(BinOp):
    pass



