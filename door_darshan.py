import discord
from discord.ext import commands
from time import sleep
import RPi.GPIO as io
import os
from gtts import gTTS, lang
from playsound import playsound
# from bottle import run
# from door_page import app

if __name__ == '__main__':
    
    relay1 = 32
    relay2 = 33
    io.setmode(io.BOARD)
    io.setwarnings(False)
    io.setup(relay1,io.OUT)
    io.setup(relay2,io.OUT)
    
    # run(app, host='localhost', port=8081)
    
    try:
        with open('door_info.txt', 'r') as file:
            lines = file.readlines()
            door_status = lines[0].strip().split(' = ')[1].strip()
            last_access = lines[1].strip().split(' = ')[1].strip()
            if door_status == 'Open':
                door_opened = True
                io.output(relay1,1)
                sleep(0.5)
                io.output(relay2,1)
                sleep(0.5)
                io.output(relay1,0)
                person = last_access.split(" ")[2]
                print(f"Door is last opened by {person}.")
                
            else:
                door_opened = False
    except:
        door_opened = False
            
    class MyNewHelp(commands.HelpCommand):
        def __init__(self):
            super().__init__()
        
        async def send_bot_help(self, mapping):
            filtered = await self.filter_commands(self.context.bot.commands, sort=True)
            names = [command.name for command in filtered]
            available_commands = "List of all commands:\n" + "\n".join(names) + "\n\nType .help <command> for further help on each command."
            # embed = discord.Embed(description=available_commands)
            await self.context.send(available_commands)
            
        async def send_command_help(self, command):
            await self.context.send("Name: " + str(command.name) + "\nDescription: " + str(command.description))
            
    bot = commands.Bot(command_prefix=".", intents=discord.Intents.all(), help_command=MyNewHelp())
    
    @bot.event
    async def on_ready():
        channel = bot.get_channel(1140013299728134225)
        await channel.send("Door-Darshan is online!")
    
    # @bot.event
    # async def on_disconnect():
        # channel = bot.get_channel(1140013299728134225)
        # await channel.send("Door-Darshan is disconnected!")

    @bot.command(name="hello", description="Displays welcome message.\nCommand: .hello")
    async def hello(ctx):
        await ctx.reply("Hello! Door-Darshan welcomes you")
        
    @bot.command(name="o", description="Opens the door.\nCommand: .o")
    async def o(ctx):
        global door_opened, last_access
        if not door_opened:
            door_opened = True
            io.output(relay1,1)
            sleep(0.5)
            io.output(relay2,1)
            sleep(0.5)
            io.output(relay1,0)
            await ctx.send(f"Door is opened by {ctx.author.display_name}.")
            print(f"Door is opened by {ctx.author.display_name}.")
            last_access = f"Opened by {ctx.author.display_name}"
            sleep(2)
            print(f"Door is last opened by {ctx.author.display_name}.")
            with open('door_info.txt', 'w') as file:
                file.write(f"door_status = Open\n")
                file.write(f"last_access = Opened by {ctx.author.display_name}\n")
        else:
            await ctx.send(f"Door is already open")

    @bot.command(name="c", description="Closes the door.\nCommand: .c")
    async def c(ctx):
        global door_opened, last_access
        if door_opened:
            door_opened = False
            # io.output(relay1,0)
            io.output(relay2,0)
            await ctx.send(f"Door is closed by {ctx.author.display_name}.")
            print(f"Door is closed by {ctx.author.display_name}.")
            last_access = f"Closed by {ctx.author.display_name}"
            sleep(2)
            print(f"Door is last closed by {ctx.author.display_name}.")
            with open('door_info.txt', 'w') as file:
                file.write(f"door_status = Closed\n")
                file.write(f"last_access = Closed by {ctx.author.display_name}\n")
        else:
            await ctx.send(f"Door is already closed")
    
    @bot.command(name="list_access", description="Lists the name of users in the Access list.\nCommand: .list_access")
    async def list_access(ctx):
        with open('/home/door/MagicMirror/modules/MMM-HTMLBox/lab_access.html') as f:
            lines = f.readlines()
        l = list(lines[12][3:].split("<br>"))
        reply = "1. " + l[0]
        for i in range(1, len(l)):
            reply += "\n" + str(i+1) + ". " + l[i]
        await ctx.reply(reply)
    
    @bot.command(name="add_access", description="Adds the given user details to the Access list.\nCommand: .add_access <position> <name> <any other detail (optional)>")
    async def add_access(ctx, arg1: int, arg2: str, arg3=None) -> None:
        with open('/home/door/MagicMirror/modules/MMM-HTMLBox/lab_access.html', 'r') as f:
            lines = f.readlines()
        l = list(lines[12][3:].split("<br>"))
        if arg3:
            user = arg2 + " (" + arg3 + ")"
        else:
            user = arg2
        l.insert(arg1-1, user)
        lines[12] = lines[12][:3] + '<br>'.join(l)
        with open('/home/door/MagicMirror/modules/MMM-HTMLBox/lab_access.html', 'w') as f:
            f.writelines(lines)
        reply = "Updated Access List:\n1. " + l[0]
        for i in range(1, len(l)):
            reply += "\n" + str(i+1) + ". " + l[i]
        await ctx.reply(reply)
    
    @bot.command(name="remove_access", description="Removes the user from the Access list.\nCommand: .remove_access <position>")
    async def remove_access(ctx, arg1: int) -> None:
        with open('/home/door/MagicMirror/modules/MMM-HTMLBox/lab_access.html', 'r') as f:
            lines = f.readlines()
        l = list(lines[12][3:].split("<br>"))
        l.pop(arg1-1)
        lines[12] = lines[12][:3] + '<br>'.join(l)
        with open('/home/door/MagicMirror/modules/MMM-HTMLBox/lab_access.html', 'w') as f:
            f.writelines(lines)
        reply = "Updated Access List:\n1. " + l[0]
        for i in range(1, len(l)):
            reply += "\n" + str(i+1) + ". " + l[i]
        await ctx.reply(reply)
    
    @bot.command(name="reboot", description="Reboots the Raspberry Pi\nCommand: .reboot")
    async def reboot(ctx):
        role = discord.utils.get(ctx.guild.roles, name="mod")
        if role in ctx.author.roles:
            await ctx.send("Door-Darshan will reboot now. It will not be available for use for 5-10 mins.")
            os.system('echo 123 | sudo -S reboot now')
        else:
            await ctx.send("Permission denied. You need to be a mod for rebooting the computer.")
            
    @bot.command(name="shutdown", description="Shuts down the Raspberry Pi\nCommand: .shutdown")
    async def shutdown(ctx, password: str):
        role = discord.utils.get(ctx.guild.roles, name="mod")
        await ctx.message.delete()
        if role in ctx.author.roles:
            if password == "darshan":
                await ctx.send("Door-Darshan is now shutting down. It will not be available for use until it's powered on manually.")
                os.system('echo 123 | sudo -S shutdown -h now')
            else:
                await ctx.reply("Password is incorrect.")
        else:
            await ctx.reply("Permission denied. You need to be a mod for shutting down the computer.")
    
    @bot.command(name="announce", description="Announces the text you send to the RTC Lab\nCommand: .announce <text>")
    async def announce(ctx, text: str, language="en"):
        role = discord.utils.get(ctx.guild.roles, name="mod")
        if role in ctx.author.roles:
            if language not in lang.tts_langs():
                await ctx.send("Provided language is not available. The announcement will be done in English.")
                language = 'en'
            tts = gTTS(text, lang=language)
            tts.save('abc.mp3')
            playsound('/home/door/MagicMirror/modules/MMM-PythonPrint/abc.mp3')
            await ctx.send("Text announced.")
        else:
            await ctx.send("Permission denied. You need to be a mod for using announce.")
       
    token = "Your Discord Token. Github does not allow to publish tokens"
    bot.run(token)
    
