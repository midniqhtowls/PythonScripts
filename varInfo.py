# DON'T FORGET TO ADD THE COMMA (,) BEHIND THE CODE IF THERE IS ONE! (the bot can error if its missing)

# for status, change the blue thing behind discord.Status to the options in the comment below

discord.Status.do_not_disturb, # sets do not disturb status
discord.Status.online, # sets online status
discord.Status.idle, # sets idle status
discord.Status.offline, # sets offline status

# -------

# for activity type, change the blue thing behind discord.ActivityType to the options in the comment below for listening and watching and replace it with discord.Game or discord.Streaming if you want the streaming or playing status, also remove the other ) if you are using game or streaming

activity=discord.Activity(type=discord.ActivityType.watching, name=f"{status}", # this is default, sets watching status, if you want to change the thing your bot is watching then change the status part
activity=discord.Activity(type=discord.ActivityType.listening, name=f"{status}"), # sets listening status, if you want to change the song name, change the status part
activity=discord.Game(name=f"{status}"), # sets playing status, if you want to change the game name, change the status part
activity=discord.Streaming(name=f"{status}", url=f"{status1}"), # sets streaming status, if you want to change the title of the stream, change status, if you want to change the url, change status1
