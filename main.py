import discum


bot=discum.Client(token="ODczNTU2MDY0MDk5MDA4NTYy.YS4MvA.PVt-_nMzRavGWpqJgkCrQD6zTqs")

@bot.gateway.command
def pingpong(resp):
    if resp.event.message:
        m = resp.parsed.auto()
        if m['channel_id'] == '881703492476084281':
         if m['content'] == '<@&905398336008384542>':   
            bot.sendMessage(m['channel_id'], '!d bump')



bot.gateway.run(auto_reconnect=True)