# slackbot達を起動
bots:
	make calc
	make memo

# test bot
test: bot_test/bot.py
	python bot_test/bot.py &
# calculation bot
calc: calcbot/bot.py
	python calcbot/bot.py &
# memo bot
memo: memobot/bot.py
	python memobot/bot.py &

# slackbotのための新しいディレクトリの作成
new:
	mkdir new
	mkdir new/plugin
	cp bot_test/bot.py new/
	cp bot_test/slackbot_settings.py new/
	cp bot_test/plugin/__init__.py new/plugin/
	cp bot_test/plugin/reaction.py new/plugin/
