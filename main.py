import discord from discord.ext import commands
إعداد صلاحيات الـ Intents التي قمنا بتفعيلها سابقاً
intents = discord.Intents.default() intents.message_content = True intents.members = True intents.presences = True
تحديد رمز الأوامر للبوت (البريفكس هنا هو !) واسم البوت
bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event async def on_ready(): print(f'تم تشغيل البوت بنجاح باسم: {bot.user.name}') # وضع حالة البوت في الديسكورد (يلعب حالياً...) await bot.change_presence(activity=discord.Game(name="!ping لتجربتي"))
أمر تجريبي بسيط للتأكد من استجابة البوت
@bot.command() async def ping(ctx): await ctx.send('Pong! 🏓 البوت يعمل بنجاح!')
تشغيل البوت باستخدام التوكن الخاص بك مباشرة
bot.run('MTU2NjE5Mzg2MTkyNjMzMDQxMQ.G7JCD7.mMTJrX6REbyCsJsGfErC1csNnV9YOXNFg17Mn8')
