import json
import os
import discord
import random

# 1. Define the path to the JSON file
base_path = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_path, 'config.json')

# 2. Open and read JSON file
with open(config_path, 'r', encoding='utf-8') as f:
    config = json.load(f)

def save_config():
    with open(config_path, 'w', encoding='utf-8') as f:
        # indent=4 makes the file easier to be read by others
        json.dump(config, f, indent=4, ensure_ascii=False)

# 3. Define the bot client
class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message): # ignore messages from the bot itself
    if message.author == self.user:
        return

#------------------------------------------------------------------------------------#

    if message.content.startswith('$commands'):
        await message.channel.send('$setrole @role - set the default role for new users that will join the server\n' \
                                   '$toggle_emojis - enable/disable the emoji addition to the new users nicknames\n' \
                                   '$setemojis list - change the emoji list that Noah is using when changing the nicknames of new users that will join the server')

#------------------------------------------------------------------------------------#

    if message.content.startswith('$setrole'):
       # Verify if the user has Administrator role
       if not message.author.guild_permissions.administrator:
          await message.channel.send("❌ Only admins can use this command")
          return
       
       # Split the message in 2 parts: ['$setrole', 'ID_ROLE']
       parts = message.content.split()
       if len(parts) < 2:
          await message.channel.send("Use: `$setrole ID_ROLE`")
          return
       
       # Extract the ID (remove characters: < @ & >)
       new_role_id = parts[1].replace('<','').replace('>','').replace('@', '').replace('&', '')

       # Update the variable in config.
       config["default_role"] = new_role_id

       save_config()

       await message.channel.send(f"✅ The default roll has been updated!")

#------------------------------------------------------------------------------------#

    if message.content.startswith('$toggle_emojis'):
       # Verify if the user has Administrator role
       if not message.author.guild_permissions.administrator:
          await message.channel.send("❌ Only admins can use this command")
          return
       
      # Toggle the boolean value
       if config["emoji_toggle"]:
          config["emoji_toggle"] = not config["emoji_toggle"]
       else:
          config["emoji_toggle"] = not config["emoji_toggle"]

       save_config()

       await message.channel.send(f"✅ Emoji toggle is now set to: {config['emoji_toggle']}")

#------------------------------------------------------------------------------------#

    if message.content.startswith('$setemojis'):
       # Verify if the user has Administrator role
       if not message.author.guild_permissions.administrator:
          await message.channel.send("❌ Only admins can change the emoji list.")
          return

       # Split the message: first part is the command, second part is the rest of the text
       # split(None, 1) împarte mesajul în maximum două bucăți
       parts = message.content.split(None, 1)

       if len(parts) < 2:
          await message.channel.send("Utilize: `$setemojis 🔥 ⭐ 🛡️` (use spaces between emojis)")
          return

       # Take the rest of the message and transform it into a list
       # .split() without arguments will separate the text after each empty space.
       new_list = parts[1].split()

       # Update list
       config["emoji_list"] = new_list
            
       # Save the new structure in config.json
       save_config()
            
       await message.channel.send(f"✅ The list has beeen updated! Here is the new list: {new_list}")

#------------------------------------------------------------------------------------#

  async def on_member_join(self, member):
    # Role ID conversion to int
    role = member.guild.get_role(int(config["default_role"]))
    if role:
        try:
            await member.add_roles(role)
        except discord.Forbidden:
           print("I dont have the permission to add roles!")

    if config["emoji_toggle"]:
         # Nickname logic
         base_name = member.display_name # display_name automaticaly take nick or name
         new_nick = f"{base_name} {random.choice(config['emoji_list'])}"
        
         try:
            await member.edit(nick=new_nick[:32]) # Discord limit is 32 characters
         except discord.Forbidden:
            print(f"Can't change the name of {member.name}.")

#------------------------------------------------------------------------------------#

# 4. Intent Activation
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = MyClient(intents=intents)
client.run('TOKEN') # Discord bot token.

