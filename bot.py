import discord
from dictionary import Dictionary

class MyClient(discord.Client):

    def __init__(self):
        self.__dict = Dictionary()
        super().__init__()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('?help'):
            help_mes = ''
            help_mes += 'You can search for the definition of a word by\n'
            help_mes += '?def <word>\n' 
            help_mes += '{0.author.mention}'.format(message)
            await message.channel.send(help_mes)
        
        elif message.content.startswith('?def'):
            cont = message.content
            parsed = cont.split()
            try:
                defin = self.__dict.definition(parsed[1])
            except:
                defin = 'There is no such word like "' + str(parsed[1]) + '".'

            await message.channel.send(defin)