# -*- coding: utf-8 -*-
from slackbot.bot import listen_to
from slackbot.bot import respond_to
#from pyparsing import Forward, Optional, oneOf, ZeroOrMore, Regex
from pyparsing import *
import re
from expr_ast import AstGenerator
#import parse

ast = AstGenerator()

DEFAULT_REPLY = 'I can only understand formulas (composed {0,1,2,3,4,5,6,7,8,9,(,),+,-,*,/}'

# 3. expression
"""
number = Regex(r"\d+(\.\d*)?([eE][+-]?\d+)?")
term = Forward()
factor = Forward()
expression = Optional(oneOf("+ -")) + term + ZeroOrMore(oneOf("+ -") + term)
term << (factor + ZeroOrMore(oneOf("* /") + factor))
factor << (number | "(" + expression + ")")
"""
number = Regex(r"\d+(\.\d*)?([eE][+-]?\d+)?")
UNARY, BINARY, TERNARY = 1, 2, 3
factor = number
expression = infixNotation(
    factor,
    [
        (oneOf("+ -"), UNARY, opAssoc.RIGHT, ast.make_unary_op), # 符号が最優先
        (oneOf("* /"), BINARY, opAssoc.LEFT, ast.make_binary_op), # 掛け算割り算は足し算より優先
        (oneOf("+ -"), BINARY, opAssoc.LEFT, ast.make_binary_op),
    ]
)

expr_regex = '[0-9()+*-/ ]+'
expr_matcher = re.compile(expr_regex)


# 参加チャンネルの特定のワードに反応
@listen_to('hello')
@respond_to('hello')
def reaction1(message):
	#message.send('world!')
	message.send('hello!!!\nPlease give me a calculaiton formula as soon as possible!!!')

# メンションに返事 - 計算
"""
@respond_to('[0-9]+[\+\-\*\/][0-9]+')
def reaction_calc(message):
	formura = parse.parse("{:d}{[\+\-\*\/]}{:d}", message.body[u'text'])
	if formura[1] == u'+': # add
		result = formura[0] + formura[2]
	if formura[1] == u'-': # sub
		result = formura[0] - formura[2]
	if formura[1] == u'*': # mul
		result = formura[0] * formura[2]
	if formura[1] == u'/': # div
		result = formura[0] / formura[2]
	message.reply(str(result))
"""

# メンションに返事 - 計算, 計算式に使用される文字の部分集合全て(多分)
@respond_to('[0-9\+\-\*\/()]')
def reaction_calc(message):
	expr = message.body[u'text']
	if expr_matcher.fullmatch(expr):
		try:
			result = expression.parseString(expr)
			#print(result, type(result), result[0], type(result[0]))
			val = result[0]
			if isinstance(val, str):
				val = int(val)
			else:
				val = ast.calc(val)
			#print(val)
			#message.reply(str(result))
			message.reply(str(val))
		except:
			message.reply("throw exception. maybe syntax error.")
	else:
		message.reply(DEFAULT_REPLY)

