from OpsAi import Ai
from pyrogram import Client,filters

API_ID = 23507256
API_HASH = "7618aa57fcf8b9d81b5d5e668030d685"
TOKEN = "6817446540:AAFCvAtRLf7JINikL24ky41pUdfYb93Ty1Y:"
@app = Client("ChatGpt", api_id=API_ID,api_hash=API_HASH,bot_token=TOKEN) 
@app.on_message(filters.command("start"))
async def StartMsg(_,msg):
 await msg.reply("Hello: I am ChatGpt") 
@app.on_message(filters.command("بوت",""))
async def YesSir(_,msg):
 await msg.reply("مرحبا بك عزيزي : اسمي هو ميجا")
@app.on_message(filters.private & ~filters.reply)
async def echo(bot, msg):
    a = msg.text
    s = Ai(query = a)
    await bot.send_message(chat_id=msg.chat.id, text=s.chat()) 
@app.on_message(filters.text)
async def reply(bot, msg):
  try:
    if  msg.reply_to_message.from_user.is_bot:
    	a = msg.text
    	s = Ai(query = a)
    	await msg.reply_text(text=s.chat(),quote=True)
  except:pass
@app.on_message(filters.regex(r"^ميجا (.+)"),group=-1)
async def reply_with_text(bot, msg):
    a = msg.text.split(None,1)[1]
    s = Ai(query = a)
    await msg.reply_text(text=s.chat(),quote=True)
    
    
 
print("Run..")   
@app.run()
Client.run()
