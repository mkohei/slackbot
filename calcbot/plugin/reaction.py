# -*- coding: utf-8 -*-
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import parse
 
# 参加チャンネルの特定のワードに反応
@listen_to('hello')
@respond_to('hello')
def reaction1(message):
	#message.send('world!')
    message.send('hello!!!\nPlease give me a calculaiton formula as soon as possible!!!')

# メンションに返事 - 計算
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