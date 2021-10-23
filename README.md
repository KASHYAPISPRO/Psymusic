
<h2 align="centre">PsyMusic R0 🎵</h2>

<p align="center">
  <img src="https://telegra.ph/file/c582a472c359bcc5cc470.jpg">
</p>

<h3>Requirements 📝</h3>

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

### Deploy To Heroku</h4>

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/PSYR3X/Psymusic)



### Commands 🛠
#### For all in group
- `/play` - reply to youtube url or song file to play song
- `/ytp <song name>` - play song without youtube url or song file (best method)
- `/song <song name>` - download songs you want quickly
- `/search <query>` - search videos on youtube with details

#### Admins only
- `/pause` - pause song play
- `/resume` - resume song play
- `/skip` - play next song
- `/end` - kills playing song


### Commands for Sudo Users ⚔️
- `/userbotleaveall` - removes assistant from all chats
- `/gcast <reply to message>` - globally brodcast replied message to all chats
- `/pmpermit [on/off]` - enable/disable pmpermit message

#### Pmpermit
- `.a` - approove someone to pm you
- `.da` - disapproove someone to pm you
- You can add a custom pmpermit message by adding var `PMMSG` and adding your message through env vars (for heroku, Settings/Edit vars)

+ Sudo Users can execute any command in any groups


## Credits
- DaisyXMusic 
- Callmusic 
- this is forked from dihanofficial/sophiamusic-v6

#### Contributors
- [Dihan Randila](https://github.com/dihanofficial): Dev / Owner
- [InukaAsith](https://github.com/InukaAsith): Dev 

#### Special Credits
- [Roj Serbest](http://github.com/rojserbest): Callsmusic Developer

This bot is based on the original work done by [Rojserbest](http://github.com/rojserbest),and sophiamusic Without thier hardwork psyMusic won't exist. 
Psymusic is a modified version of [Callsmusic](https://github.com/callsmusic/callsmusic) fit for my need

- [StarkGang](https://github.com/StarkGang/)
- [SpEcHiDe](https://github.com/SpEcHiDe/)
- [The Hamker Cat](https://github.com/thehamkercat)
- [Laky(for PyTgCalls)](https://github.com/Laky-64)
- [Dan (for pyrogram)](https://github.com/delivrance)


#### Open Source codes used in this project 
- https://github.com/callsmusic/callsmusic : Source code used here as base
- https://github.com/DevsExpo/FridayUserbot/blob/master/main_startup/helper_func/basic_helpers.py : Functioms from line 275 to 351
- https://github.com/TheHamkerCat/WilliamButcherBot/blob/dev/wbb/modules/music.py : From lines 170 to 178


> This project exists thanks to these awesome developers and their codes and contributions.
> And credits goes to all who supported, all who helped and API & environmental requirement package devs and all projects helped in making this project.
> i did nothing else than changing strings for my need
