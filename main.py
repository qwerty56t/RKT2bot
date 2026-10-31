import discord from discord.ext import commands from flask import Flask from threading import Thread
تشغيل خادم ويب وهمي لإبقاء المنصة تعمل مجاناً
app = Flask('')
@app.route('/') def home(): return "البوت يعمل بنجاح!"
def run_web(): app.run(host='0.0.0.0', port=8080)
def keep_alive(): t = Thread(target=run_web) t.start()
إعداد صلاحيات البوت
intents = discord.Intents.default() intents.message_content = True intents.members = True intents.presences = True
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event async def on_ready(): print(f'تم تشغيل البوت بنجاح باسم: {bot.user.name}') await bot.change_presence(activity=discord.Game(name="!ping لتجربتي"))
@bot.command() async def ping(ctx): await ctx.send('Pong! 🏓 البوت يعمل بنجاح!')
تشغيل الخادم الوهمي قبل تشغيل البوت
keep_alive()
تشغيل البوت بالتوكن الخاص بك
bot.run('MTU2NjE5Mzg2MTkyNjMzMDQxMQ.G7JCD7.mMTJrX6REbyCsJsGfErC1csNnV9YOXNFg17Mn8')
