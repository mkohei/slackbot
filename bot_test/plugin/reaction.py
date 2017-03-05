# -*- coding: utf-8 -*-
from slackbot.bot import listen_to
from slackbot.bot import respond_to
 
# 参加チャンネルの特定のワードに反応
@listen_to('hello')
def reaction1(message):
	#message.send('world!')
    message.send('hello!!!')
 
# メンションに返事
@respond_to(u'水曜')
def reaction2(message):
	message.reply('どうでしょう')