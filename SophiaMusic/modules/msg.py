import os
from SophiaMusic.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**Hello 👋 [{}](tg://user?id={})!**\n\n🤖 I am not a very advanced bot created for playing music in the voice chats of Tg Groups & Channels.\n\n✅ Type /help for more info. \n\nCurrently this bot is under psyrex production. \n\nyou cant add it any where hehehe"
      HELP_MSG = [
        ".",
f"""
**Hey 👋 Welcome back to {PROJECT_NAME}
⚪️ {PROJECT_NAME} can play music in group's voice chat as well as channel voice chats
⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Setting up**
1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry
**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group
**Commands**
**=>> Song Playing 🎧**
- /play: Plays the requestd song
- /play [yt url] : Plays audio from given yt url
- /play [reply yo audio]: Plays replied audio
- /splay: Plays song via jio saavn
- /ytplay: Directly plays song via Youtube Music
**=>> Playback ⏯**
- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Kills media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist
*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
""",
        
f"""
**=>> Channel Music Play 🛠**
⚪️ For linked group admins only:
- /cplay [song name] - plays song you requested
- /csplay [song name] - plays song you requested via jio saavn
- /cplaylist - Shows now playing list
- /cccurrent - Shows now playing song
- /cplayer - opens music player settings panel
- /cpause - pause track
- /cresume - resume track
- /cskip - plays next song
- /cend - Kills music play
- /userbotjoinchannel - invite assistant to your chat
channel is also can be used instead of c ( /cplay = /channelplay )
⚪️ If you don't like to play in linked group:
1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group.
""",

f"""
**=>> More tools 🧑‍🔧**
- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. </ Try if bot isn't recognize admin />
- /userbotjoin: Invites @{ASSISTANT_NAME} Userbot to your chat
- /auth [reply to user] - Authorize User
- /deauth [reply to user] - DeAuthorize user
Authorized users can execute admin commands in authorized group
**=>> Commands for Sudo Users ⚔️**
 - /userbotleaveall - remove assistant from all chats
 - /gcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups
"""
      ]
