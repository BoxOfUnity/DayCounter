import os
import time
import threading
import discord
from dotenv import load_dotenv

threads = []
threadsMap = {}
def StartNewThread(uid):
    print("!!SNT ACTIVATED!!")
    threadClass = threading.start_new_thread(bpu().main(), ())
    threads.append[threadClass]
    threadsMap.append[threadClass:uid]

class bpu:


    def main(self):
        global threads
        global threadsMap
        global StartNewThread
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')

        client = discord.Client()



        @client.event
        async def on_ready():
            channel = client.get_channel(952585287509364746)
            await channel.send("Online")
   

        class vars:
            channel_to_count = 0
            keyed = False
            daycount = 526



    


        @client.event
        async def on_message(message):  #3
            
                        
            print("message recieved from", message.author.id)
            print("message: "+message.content)
            start_command = "setchanneltothis"

            if vars.keyed == False and message.content.lower() == start_command:
                print("keyword has been detected.")
                vars.keyed = True
                await message.channel.send("yezzir!!")
                

            elif vars.keyed == True:
                while True:
                    time.wait(10) #86400 = 24h
                    await message.channel.send(vars.daycount)
                    

            

        

        client.run(TOKEN) #1

bpu().main()
