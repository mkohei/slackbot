# -*- coding: utf-8 -*-
from slackbot.bot import listen_to
from slackbot.bot import respond_to

# 参加チャンネルの特定のワードに反応
@listen_to('hello')
@respond_to('hello')
def reaction1(message):
	#message.send('world!')
	message.send("hello...\nUnless you want, I will never forget you... \n```\ncommands\n    -> memo+(contents)\n    -> show\n    -> clear```")
 
# メンションに返事
@respond_to(u'^memo\+')
def reaction2(message):
	s = message.body[u'text']
	f = open('memo.txt', mode='a')
	f.write(s[5:] + '\n')
	f.close()
	message.reply("I remembered...")

@respond_to(u'show')
def reaction3(message):
	f = open('memo.txt', mode='r')

	s = '```\n'
	for row in f:
		s = s + row
	message.reply(s + '```')	

@respond_to(u'clear')
def reaction4(message):
    f = open('memo.txt', mode='w')
    f.write('')
    f.close()
    message.reply("I did not want to forget you...\nI lost my memory...")

