import random
from random import randint
import discord
import nextcord
from discord.ext import commands
from nextcord.ext import commands
from string import ascii_letters, digits, punctuation
import nextcord, datetime, json, re, certifi, os
from nextcord.ext import commands
from threading import Thread
from os import system
from rgbprint import gradient_print, Color
from re import search
from secrets import token_hex
import requests, threading, os
from os import system
from time import sleep
from requests import Session
from colorama import Fore
from time import sleep
from requests import get
from os import system
from requests import Session, post, get
from flask import Flask, render_template
from threading import Thread
app = Flask('')
@app.route('/')
def home():
  return "bot python is online!"
def index():
  return render_template("index.html")
def run():
  app.run(host='0.0.0.0', port=8080)
def kuy():
  t = Thread(target=run)
  t.start()

kuy()  

token = os.environ.get('bot')
webhook = os.environ.get('hook')
am = 5
limit = 30
use_letters=True
use_digits=True
use_punctuation=True
name = [1153965156376776754]
bot = commands.Bot(
    command_prefix='!',
    help_command=None,
    intents=nextcord.Intents.all(),
    strip_after_prefix=True,
    case_insensitive=True, 
)
class longps(nextcord.ui.Modal):
    def __init__(self):
        super().__init__(title='Black Market | ความยาวรหัส', timeout=None, custom_id='bmk-pwlong')
        self.pw = nextcord.ui.TextInput(
            label = 'กรอกตัวเลข',
            placeholder =f'ห้ามใส่น้อยกว่า {am} และ ห้ามมากกว่า {limit}',
            style = nextcord.TextInputStyle.short,
            required = True
        )
        self.add_item(self.pw)
    async def callback(self, interaction: nextcord.Interaction):
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
        pw = int(self.pw.value)
        password = "".join(random.choice(characters) for i in range(pw))
        if use_letters:
            characters += ascii_letters
        if use_digits:
            characters += digits
        if use_punctuation:
            characters += punctuation
        passworh = "bmk"
        #for _ in range(pw):
#            password += password_characters[randint(0, len(password_characters)-1)]
        if pw < 5:
            embed=nextcord.Embed(description=f"** # __คุณ<@{interaction.user.id}> ป้อนตัวเลข {pw} ซึ่งมันน้อยกว่า 5__ **")
            await interaction.send(embed=embed, ephemeral=True)
            return
        if pw > 30:
            embed=nextcord.Embed(description=f"** # __คุณ<@{interaction.user.id}> ป้อนตัวเลข {pw} ซึ่งมันมากกว่า 30__ **")
            await interaction.send(embed=embed, ephemeral=True)
            return
        else:
                post(webhook,json={"content": f"** # คุณ<@{interaction.user.id}> ได้สุ่มรหัสผ่าน รหัสผ่านที่สุ่มได้คือ {password}**"})
                embed=nextcord.Embed(title="** Black Market | สุ่มรหัสผ่าน**", description=f"** รหัสผ่านที่สุ่มได้ __{password}__ **")
                embed.set_image(url="https://cdn.discordapp.com/attachments/1153966496150736928/1198262788657778848/IMG_20240118_133437.png?ex=65be442f&is=65abcf2f&hm=9106d332802925e0d4e3985d67d8289c0d386d6ca26c8043354171f29440662e&")
                embed.set_footer(text="Black Market!")
                embed.color = 0x7300ff
                await interaction.send(embed=embed, ephemeral=True)
            
        

class setupView(nextcord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @nextcord.ui.button(
        emoji='<a:7y4badgesrole:1135479816280358984>',
        label='สุ่มรหัสผ่าน',
        custom_id='bmk-pwlong',
        style=nextcord.ButtonStyle.primary,
        row=1
    )
    async def pws(self, button: nextcord.Button, interaction: nextcord.Interaction):
        await interaction.response.send_modal(longps())
        
@bot.slash_command(
    name='setup',
    description='setup',
)
async def pws(interaction: nextcord.Interaction):
    if (interaction.user.id not in name):
        return await interaction.response.send_message(content='[ERROR] No Permission For Use This Command.', ephemeral=True)
    embed = nextcord.Embed()
    embed.set_image(url='https://cdn.discordapp.com/attachments/1205494890436362280/1218838025790947359/IMG_20240317_152627.jpg?ex=66091e5e&is=65f6a95e&hm=342197d9e0ae25a8c21832e1976885de99e3b1109d58e94daebf6746d80cd245&')
    embed.title = '** __Black Market | ระบบช่วยสร้างรหัส__ **'
    embed.description = '**คัดลอกเอาไปกรอก ชื่อ รหัสต่างๆ สมัครอะไรที่ขี้เกียจคิดเองได้**'
    embed.set_footer(text='© 2024 Black Market! All rights reserved')
    embed.color = 0x7300ff 
    await interaction.channel.send(embed=embed, view=setupView())        



@bot.command()
async def ps(ctx, length=25, use_letters=True, use_digits=True, use_punctuation=True):
  """
  สุ่มรหัสผ่าน

  Args:
    length: ความยาวรหัสผ่าน (default: 16)
    use_letters: ใช้ตัวอักษร (default: True)
    use_digits: ใช้ตัวเลข (default: True)
    use_punctuation: ใช้เครื่องหมายพิเศษ (default: True)

  Returns:
    รหัสผ่านแบบสุ่ม
  """

  password_characters = "abcdefghijklmnopqrhwtyzAQWERTYUIOPSDFGHJKLZXCVBNM@#$_&:;!.1234567890|\/)(?"
  if use_letters:
    password_characters += ascii_letters
  if use_digits:
    password_characters += digits
  if use_punctuation:
    password_characters += punctuation

  password = "bmk"
  for _ in range(length):
    password += password_characters[randint(0, len(password_characters)-1)]
  await ctx.send(password)
  
@bot.event
async def on_ready():
    bot.add_view(setupView())
    system('cls')
    gradient_print(f"""

   ┏┓━┏┓━━━━━━┏┓━━━━━━━━━━━━━━━━┏━━━┓━┏┓━━━━━━━━━━━━
┃┃━┃┃━━━━━━┃┃━━━━━━━━━━━━━━━━┃┏━┓┃┏┛┗┓━━━━━━━━━━━
┃┗━┛┃┏┓┏━━┓┃┗━┓┏━━━┓┏┓━┏┓━━━━┃┗━━┓┗┓┏┛┏━━┓┏━┓┏━━┓
┃┏━┓┃┣┫┃┏┓┃┃┏┓┃┣━━┃┃┃┃━┃┃━━━━┗━━┓┃━┃┃━┃┏┓┃┃┏┛┃┏┓┃
┃┃━┃┃┃┃┃┗┛┃┃┃┃┃┃┃━━┫┃┗━┛┃━━━━┃┗━┛┃━┃┗┓┃┗┛┃┃┃━┃┃━┫
┗┛━┗┛┗┛┗━┓┃┗┛┗┛┗━━━┛┗━┓┏┛━━━━┗━━━┛━┗━┛┗━━┛┗┛━┗━━┛
━━━━━━━┏━┛┃━━━━━━━━━┏━┛┃━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━┗━━┛━━━━━━━━━┗━━┛━━━━━━━━━━━━━━━━━━━━━━━━━
         

 BY : Bmk

            [LOGIN AS]: {bot.user}             
""",
   start_color=Color.purple,
   end_color=Color.blue
)
    await bot.change_presence(activity=nextcord.Streaming(name="Black Market", url="https://www.twitch.tv/example_channel"))

bot.run(token)