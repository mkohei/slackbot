# -*- coding: utf-8 -*-
from slackbot.bot import listen_to
from slackbot.bot import respond_to
from pyparsing import Forward, Optional, oneOf, ZeroOrMore, Regex
import re
#import parse

DEFAULT_REPLY = 'I can only understand formulas (composed {0,1,2,3,4,5,6,7,8,9,(,),+,-,*,/}'

# 3. expression
number = Regex(r"\d+(\.\d*)?([eE][+-]?\d+)?")
term = Forward()
factor = Forward()
expression = Optional(oneOf("+ -")) + term + ZeroOrMore(oneOf("+ -") + term)
term << (factor + ZeroOrMore(oneOf("* /") + factor))
factor << (number | "(" + expression + ")")

expr_regex = '[0-9()+*-/]+'
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
		message.reply(str(expression.parseString(expr)))
	else:
		message.reply(DEFAULT_REPLY)

