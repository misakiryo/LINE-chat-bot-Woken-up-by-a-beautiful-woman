import json
from linebot import LineBotApi
from linebot.models import TextSendMessage

file = open("ここにLINEAPIから持ってきたjsonファイルを入れる", "r")
info = json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    USER_ID = info['USER_ID']
    messages = TextSendMessage(text = "おはよう〜朝だよ♡ \n 今日も一緒に頑張ろうね(*´ω｀*)")
    line_bot_api.push_message(USER_ID, messages=messages)
    
if __name__ =="__main__":
    main()