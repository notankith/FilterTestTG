class script(object):
    START_TXT = """<b><i>Heyy There! {},
I am a User-Friendly Bot Used To Provide Files Of Any Movies/Series & Anime :) </b></i>"""
    HELP_TXT = """<b>Hey {}
These Are My Additional Plug-ins. </b>"""
    ABOUT_TXT = """<b>✯ Name: {}
✯ Owned By: <a href=https://t.me/ExaBots>ExaBots</a>
✯ LIBRARY: PYROGRAM
✯ LANGUAGE: PYTHON 3
✯ DATABASE: MONGO DB
✯ BOT SERVER: VPS
✯ BUILD STATUS: v1.0.1 [ Stable ]</b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Confidential Project. Contact Owner For Source Code.  
- Contact - @BigGunDaddy  

<b>Developers:</b>
- <a href=https://t.me/ExaBots>ExaBots</a>"""
    TELEGRAPH = """Reply to any photo or video using by /telegraph to get the link."""
    TOOLS = """TOOLS:

/news - {text}
/paste - {reply}"""
    LYRICS = """Usage Lyrics:

/lyrics - {song name}"""
    QRCODE = """Usage qr code:

/qr - {text}"""
    SONG = """usage song: 

/song - {song name}"""
    IMAGINE = """ How to Use example
<code>/imagine a boy and girl looking a sky </code>
You Can Create Your like pictures using by This command /imagine """
    TRANSLATE = """Usages:
/tr reply message and ml like this

<code> /tr ml </code>"""
    PROMOTE = """<b>Yᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ᴍᴇᴍʙᴇʀs ɪɴ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴀᴅᴍɪɴ
 
Bʏ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ. 
/promote 


Yᴏᴜ ᴄᴀɴ ʀᴇᴍᴏᴠᴇ ᴛʜᴇᴍ ʙʏ ᴀᴅᴍɪɴ ᴜsɪɴɢ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ /demote</b>"""
    IMG = """ You Can Serch Image Using This command /img
Example: <code> /image Tony stark </code>"""
    FONT_TXT = """ To Use This Function

/font {your_text}

ᴇɢ:- /font Hello """
    STICKER = """ Use This Plug-In to Find Stickers!.
• ᴜꜱᴀɢᴇ :ᴛᴏ ɢᴇᴛ ꜱᴛɪᴄᴋᴇʀ
 
⭕ ʜᴏᴡ ᴛᴏ ᴜꜱᴇ
◉ Reply To Any Sticker [/stickerid]"""
    TTS = """ Help:  TTS 🎤 module:
Translate text to speech
Commands and Usage:
• /tts  : convert text to speech"""
    BUG_TXT = """Report Any Bugs or Issues With The Code By /bug Command. """
    FEED = """Use /feedback To Give Feedback Or Any Improvments To The Bot. 
"""
    AI = """AI
/openai {query}
"""
    FUNS = """FUNS HELP

/truth - [message]
/dare - [message]
/joke - [message]
"""
    ECHO = """ A Random Plug-In Added For Fun.

 /echo {text}
 """
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    ENHANCE = """Reply To A Photo To Enhance That Photo!"""
    CARBON = """HELP: Carbon

Beautify your code using carbon!

USAGE:
➢ /carbon [text] - Create carbon from the given text."""
    BUTTON_TXT = """Help: <b>Buttons</b>

- bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/....)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    PONG_TXT = """ For Testing Bot PING!

ᴄᴏᴍᴍᴀɴᴅꜱ:
• /alive - To Check Bot Status.
• /ping - To Check Bot Ping.

ᴜꜱᴀɢᴇ :
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ɪɴ ᴘᴍ ᴀɴᴅ ɢʀᴏᴜᴘꜱ
• ᴛʜɪꜱ ᴄᴏᴍᴍᴀɴᴅꜱ ᴄᴀɴ ʙᴇ ᴜꜱᴇᴅ ʙᴜʏ ᴇᴠᴇʀʏᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘꜱ ᴀɴᴅ ʙᴏᴛꜱ ᴘᴍ
• ꜱʜᴀʀᴇ ᴜꜱ ꜰᴏʀ ᴍᴏʀᴇ ꜰᴇᴀᴛᴜʀᴇꜱ"""
    PIN_TXT = """ ᴩɪɴ ᴍᴏᴅᴜʟᴇ
ᴩɪɴ ᴀ ᴍᴇꜱꜱᴀɢᴇ...

Pin Related Commands Found Here! :)

📌ᴄᴏᴍᴍᴀɴᴅꜱ ᴀɴᴅ ᴜꜱᴀɢᴇ📌

/pin :- ᴛᴏ ᴩɪɴ ᴛʜᴇ ᴍᴇꜱꜱᴀɢᴇ ᴏɴ ʏᴏᴜʀ ᴄʜᴀᴛꜱ
/unpin :- ᴛᴏ ᴜɴᴩɪɴ ᴛʜᴇ ᴄᴜʀʀᴇᴇɴᴛ ᴩɪɴɴᴇᴅ ᴍᴇꜱꜱᴀɢ
/unpin_all :- ᴛᴏ ᴜɴᴩɪɴ ᴛʜᴇ ᴄᴜʀʀᴇᴇɴᴛ ᴩɪɴɴᴇᴅ ᴀʟʟ ᴍᴇꜱꜱᴀɢ"""
    CAPTION = """
<b>📂 Fɪʟᴇ ɴᴀᴍᴇ : </b> {file_name}"""

    IMDB_TEMPLATE_TXT = """
<b>Query: {query}
IMDb Data:

🏷 Title: <a href={url}>{title}</a>
🎭 Genres: {genres}
📆 Year: <a href={url}/releaseinfo>{year}</a>
🌟 Rating: <a href={url}/ratings>{rating}</a> / 10</b>"""

    FLTERS_TXT = """
<b>Heyy {}, These Are My Typed Of Filters.</b>"""
    
    FILE_STORE_TXT = """
<b>File Store Is The Feature Which Will Create A Shareable Link Of A Single Or Multiple Files.
</b>

Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /batch - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ʙᴀᴛᴄʜ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ғɪʟᴇs.</code>
• /link - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ sɪɴɢʟᴇ ғɪʟᴇ sᴛᴏʀᴇ ʟɪɴᴋ.</code>
• /pbatch - <code>Jᴜsᴛ ʟɪᴋᴇ /batch, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇs ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴs.</code>
• /plink - <code>Jᴜsᴛ ʟɪᴋᴇ /link, ʙᴜᴛ ᴛʜᴇ ғɪʟᴇ ᴡɪʟʟ ʙᴇ sᴇɴᴅ ᴡɪᴛʜ ғᴏʀᴡᴀʀᴅ ʀᴇsᴛʀɪᴄᴛɪᴏɴ.</code>"""
    
    GLOBAL_TXT = """ <b>Wᴇʟᴄᴏᴍᴇ ᴛᴏ Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs. Gʟᴏʙᴀʟ Fɪʟᴛᴇʀs ᴀʀᴇ ᴛʜᴇ ғɪʟᴛᴇʀs sᴇᴛ ʙʏ ʙᴏᴛ ᴀᴅᴍɪɴs ᴡʜɪᴄʜ ᴡɪʟʟ ᴡᴏʀᴋ ᴏɴ ᴀʟʟ ɢʀᴏᴜᴘs.</b>
   
   Aᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:
• /gfilter - <code>Tᴏ ᴄʀᴇᴀᴛᴇ ᴀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /gfilters - <code>Tᴏ ᴠɪᴇᴡ ᴀʟʟ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀs.</code>
• /delg - <code>Tᴏ ᴅᴇʟᴇᴛᴇ ᴀ ᴘᴀʀᴛɪᴄᴜʟᴀʀ ɢʟᴏʙᴀʟ ғɪʟᴛᴇʀ.</code>
• /delallg - <code>ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴀʟʟ ɢʟᴏʙᴀʟ ꜰɪʟᴛᴇʀꜱ.</code>"""
   
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    RENDERING_TXT = """
ʟɪᴠᴇ sʏsᴛᴇᴍ sᴛᴀᴛᴜs 

❂ RAM ●●●●●●●◌◌◌
✇ CPU ●●●●●●●◌◌◌
✪ DATA TRAFFIC ●●●●◌◌◌◌◌◌ 🛰

ᴠ2.7.1 [sᴛᴀʙʟᴇ] """
    DICS_TXT = """ <b><code>This is A Private Project.

All The Files In This Bot Are Freely Available On The Internet Or Posted By Somebody Else. 
Just For Easy Searching This Bot Is Indexing Files Which Are Already Uploaded On Telegram. 
We Respect All The Copyright Laws And Works In Compliance With DMCA And EUCD. 
If Anything Is Against Law Please Contact Me So That It Can Be Removed ASAP. 
It Is Forbidden To Download, Stream, Reproduce, Or By Any Means, Share, Or Consume, Content Without Explicit Permission From The Content Creator Or Legal Copyright Holder. 
If You Believe This Bot Is Violating Your Intellectual Property, Contact The Respecting Channels For Removal. 
The Bot Does Not Own Any Of These Contents, It Only Index The Files From Telegram.
 </code> """

    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Tony Stark 

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>
• /group_broadcast - <code>to broadcast a message to all groups</code>
• /eval - <code>run python codes</code>
• /sh - <code>install package or other use and code run</code>
• /restart - <code>restart the bot</code>
"""
    ALRT_TXT = """HELLO! {},

This Isn't Your Request!
Request Yourself :)"""

    OLD_ALRT_TXT = """Hey {},
You are using one of old message,
Request Again"""

    CUDNT_FND = """<b>I Couldn't Find Anything Related To That. Did You Mean Any One Of These?</b>"""

    I_CUDNT = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    I_CUD_NT = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    MVE_NT_FND = """<b>I ᴄᴏᴜʟᴅɴ'ᴛ ғɪɴᴅ ᴀɴʏᴛʜɪɴɢ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ.</b>"""

    TOP_ALRT_MSG = """Checking For Query In Database:) """
    
    NORSLTS = """
#NoResults 

ID <b>: {}</b>

Name <b>: {}</b>

Message <b>: {}</b>"""
    
    STATUS_TXT = """★ Total Files: <code>{}</code>
★ Total Users: <code>{}</code>
★ Total Chats: <code>{}</code>
★ Database Storage: <code>{}</code> MiB
★ Database Free Space: <code>{}</code> Mi"""
    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !
📅 Dᴀᴛᴇ : <code>{}</code>
⏰Tɪᴍᴇ : <code>{}</code>
🌐 Tɪᴍᴇᴢᴏɴᴇ : <code>Asia/Kolkata</code></b>"""
    
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
  
