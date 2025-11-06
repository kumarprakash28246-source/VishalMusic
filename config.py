import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

# Load environment variables from .env file
load_dotenv()

# ────────────────────────────────────────────────────────────────────────────────
# 🎵 𝗩𝗜𝗦𝗛𝗔𝗟 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 - 𝗖𝗢𝗡𝗙𝗜𝗚𝗨𝗥𝗔𝗧𝗜𝗢𝗡 🎶
# ✨ 𝗦𝗽𝗲𝗰𝗶𝗮𝗹 & 𝗦𝘁𝘆𝗹𝗶𝘀𝗵 𝗘𝗱𝗶𝘁𝗶𝗼𝗻 ✨
# ────────────────────────────────────────────────────────────────────────────────

# ── 🎵 𝗖𝗼𝗿𝗲 𝗕𝗼𝘁 𝗖𝗼𝗻𝗳𝗶𝗴 ──────────────────────────────────────────────────────
API_ID = int(getenv("API_ID", "26493077"))
API_HASH = getenv("API_HASH", "6586f0276c7748e54684719bdd247d90")
BOT_TOKEN = getenv("BOT_TOKEN")

OWNER_ID = int(getenv("OWNER_ID", "7044783841"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "Its_me_Vishall")
BOT_USERNAME = getenv("BOT_USERNAME", "VaishalixMusic_Robot")
BOT_NAME = getenv("BOT_NAME", "𝐕𝐈𝐒𝐇𝐀𝐋 ✘ 𝐌𝐔𝐒𝐈𝐂")
ASSUSERNAME = getenv("ASSUSERNAME", "𝐕𝐈𝐒𝐇𝐀𝐋 ✘ 𝐀𝐒𝐒𝐈𝐒𝐓𝐀𝐍𝐓")

# ── 🗄️ 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲 & 𝗟𝗼𝗴𝗴𝗶𝗻𝗴 ──────────────────────────────────────────────────
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", "-1002425220992"))

# ── ⚡ 𝗟𝗶𝗺𝗶𝘁𝘀 ─────────────────────────────────────────────────────────────────
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "300"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1200"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "157286400"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1288490189"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "30"))

# ── 🌐 𝗘𝘅𝘁𝗲𝗿𝗻𝗮𝗹 𝗔𝗣𝗜𝘀 ────────────────────────────────────────────────────────
COOKIE_URL = getenv("COOKIE_URL")
API_URL = getenv("API_URL")
API_KEY = getenv("API_KEY")
DEEP_API = getenv("DEEP_API")

# ── 🚀 𝗛𝗼𝘀𝘁𝗶𝗻𝗴 ──────────────────────────────────────────────────────────────
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

# ── 🔄 𝗨𝗽𝗱𝗮𝘁𝗲𝘀 ──────────────────────────────────────────────────────────────
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/ItsMeVishal0/VishalMusic.git")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

# ── 📞 𝗦𝘂𝗽𝗽𝗼𝗿𝘁 ──────────────────────────────────────────────────────────────
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ItsMeVishalBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/ItsMeVishalSupport")

# ── 🤖 𝗔𝘀𝘀𝗶𝘀𝘁𝗮𝗻𝘁 ───────────────────────────────────────────────────────────
AUTO_LEAVING_ASSISTANT = False
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "3600"))

# ── 🐞 𝗗𝗲𝗯𝘂𝗴 ─────────────────────────────────────────────────────────────────
DEBUG_IGNORE_LOG = True

# ── 🎧 𝗦𝗽𝗼𝘁𝗶𝗳𝘆 ───────────────────────────────────────────────────────────────
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "22b6125bfe224587b722d6815002db2b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "c9c63c6fbf2f467c8bc68624851e9773")

# ── 🔗 𝗦𝗲𝘀𝘀𝗶𝗼𝗻𝘀 ─────────────────────────────────────────────────────────────
STRING1 = getenv("STRING_SESSION")
STRING2 = getenv("STRING_SESSION2")
STRING3 = getenv("STRING_SESSION3")
STRING4 = getenv("STRING_SESSION4")
STRING5 = getenv("STRING_SESSION5")

# ── 🎨 𝗠𝗲𝗱𝗶𝗮 𝗔𝘀𝘀𝗲𝘁𝘀 ─────────────────────────────────────────────────────────
START_VIDS = [
    "https://files.catbox.moe/7rie2i.mp4",
    "https://files.catbox.moe/j3ba3f.mp4",
    "https://files.catbox.moe/mfeisv.mp4",
    "https://files.catbox.moe/ot88at.mp4",
    "https://files.catbox.moe/bv29a4.mp4",
    "https://files.catbox.moe/pndpqt.mp4",
    "https://files.catbox.moe/tu8l7e.mp4",
    "https://files.catbox.moe/7ygvch.mp4",
    "https://files.catbox.moe/jh55tl.mp4",
]

STICKERS = [
    "CAACAgUAAx0Cd6nKUAACASBl_rnalOle6g7qS-ry-aZ1ZpVEnwACgg8AAizLEFfI5wfykoCR4h4E",
    "CAACAgUAAx0Cd6nKUAACATJl_rsEJOsaaPSYGhU7bo7iEwL8AAPMDgACu2PYV8Vb8aT4_HUPHgQ",
]

HELP_IMG_URL = "https://files.catbox.moe/yg2vky.jpg"
PING_VID_URL = "https://telegra.ph/file/528d0563175669e123a75.mp4"
PLAYLIST_IMG_URL = "https://files.catbox.moe/xxzlq3.jpg"
STATS_VID_URL = "https://files.catbox.moe/ch7geb.mp4"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/48shlf.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/48shlf.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/48shlf.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/48shlf.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/48shlf.jpg"
SPOTIFY_ARTIST_IMG_URL = SPOTIFY_ALBUM_IMG_URL = SPOTIFY_PLAYLIST_IMG_URL = YOUTUBE_IMG_URL

# ── ⚡ 𝗛𝗲𝗹𝗽𝗲𝗿𝘀 ──────────────────────────────────────────────────────────────
def time_to_seconds(time: str) -> int:
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# ── 💫 𝗕𝗼𝘁 𝗜𝗻𝘁𝗿𝗼𝗱𝘂𝗰𝘁𝗶𝗼𝗻 𝗠𝗲𝘀𝘀𝗮𝗴𝗲𝘀 ──────────────────────────────────────────
AYU = [
    "❤️", "💞", "🩷", "💋", "🌹", "💫", "💖", "✨", "💘", "💝",
    "💕", "💗", "💓", "💟", "❣️", "🌸", "🌼", "💐", "🪷", "🌺",
    "💎", "🌙", "🌟", "🌈", "🦋", "🥰", "😍", "😘", "😚", "😻",
    "🤍", "💛", "💚", "💙", "💜", "🖤", "🤎", "🩵", "🩶", "💏",
    "💑", "💍", "💌", "💎", "🌹", "💖", "💘", "💝", "💗", "💞",
    "❤️‍🔥", "❤️‍🩹", "💓", "💟", "💃", "🕺", "🎶", "🎵", "🎧", "💫",
    "✨", "🌈", "🌸", "🌺", "🌷", "🌼", "🍀", "🥂", "🍫", "🍓",
    "🍒", "🍑", "🫶", "🤗", "🤭", "🥹", "💃", "🎀", "💄", "💅",
    "🕊️", "🐦", "🌌", "🎇", "🎆", "🌠", "🪩", "🎉", "🎊", "🥳",
    "💞", "💖", "💘", "💝", "💗", "💓", "❤️", "💋", "🌹", "✨",
    "💫", "🌈", "🦋", "💟", "💍", "💎", "🌸", "🥰", "😍", "💌"
]

AYUV = [
    "💫🌸 ʜᴇʏ {0} 💖🦋\n\n🌈 ᴛʜɪꜱ ɪꜱ {1} 💎 ʏᴏᴜʀ ᴠɪʙᴇꜱ ᴄᴏɴᴛʀᴏʟʟᴇʀ 🎶✨\n\n╭───★・𝗕𝗢𝗧 𝗦𝗧𝗔𝗧𝗨𝗦・★───╮\n┃ 🌐 𝗣𝗹𝗮𝘁𝗳𝗼𝗿𝗺𝘀: ʏᴏᴜᴛᴜʙᴇ • ꜱᴘᴏᴛɪꜰʏ • ᴀᴘᴘʟᴇᴍᴜꜱɪᴄ • ʀᴇꜱꜱᴏ • ꜱᴏᴜɴᴅᴄʟᴏᴜᴅ 💞\n┃ ⚡ 𝗨𝗽𝘁𝗶𝗺𝗲 : {2} ⏳\n┃ 💖 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 : {3} 📀\n┃ 🔥 𝗖𝗣𝗨 : {4} 💫\n┃ 🩵 𝗥𝗔𝗠 : {5} 🦋\n┃ 🌸 𝗨𝘀𝗲𝗿𝘀 : {6} 💌\n┃ 🌈 𝗖𝗵𝗮𝘁𝘀 : {7} 🕊️\n╰─────────────────────╯\n\n💌✨ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ➪ [»»—⎯⁠⁠⁠⁠‌꯭꯭νιѕнαL𝅃 ₊꯭♡゙꯭. »︎](https://t.me/Its_me_Vishall) 🌹💎",

    "🌷💖 ʜᴇʏᴀ {0} 💫🌈\n\n🎧 ɪ'ᴍ {1} — ʏᴏᴜʀ ᴄʟᴏᴜᴅ ᴍᴜꜱɪᴄ ᴄᴏᴍᴘᴀɴɪᴏɴ 💞✨\n\n╭───☆・𝗙𝗘𝗔𝗧𝗨𝗥𝗘𝗦・☆───╮\n┃ 🎶 ʟɪᴠᴇ ᴍᴜꜱɪᴄ / ᴠɪᴅᴇᴏ ꜱᴛʀᴇᴀᴍ 💎\n┃ 🌈 ꜱᴜᴘᴇʀꜰᴀꜱᴛ ᴠᴄ ᴘʟᴀʏᴇʀ ⚡\n┃ 💖 ᴀᴜᴛᴏ ʀᴇꜱᴜᴍᴇ + ʟᴏ-ʟᴀɢ ᴍᴏᴅᴇ 🩵\n┃ 🌹 ᴄʟᴇᴀɴ ɢᴜɪ + ɴᴏ ᴘʀᴏᴍᴏ 🕊️\n╰─────────────────────╯\n\n📊 𝗦𝗧𝗔𝗧𝗨𝗦:\n💫 𝗨𝗽𝘁𝗶𝗺𝗲 : {2}\n💖 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 : {3}\n⚡ 𝗖𝗣𝗨 : {4}\n🩵 𝗥𝗔𝗠 : {5}\n🌸 𝗨𝘀𝗲𝗿𝘀 : {6}\n🌈 𝗖𝗵𝗮𝘁𝘀 : {7}\n\n💎 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ➪ [»»—⎯⁠⁠⁠⁠‌꯭꯭νιѕнαL𝅃 ₊꯭♡゙꯭. »︎](https://t.me/Its_me_Vishall) 🌸✨"
]

# ── 🚫 𝗕𝗮𝗻𝗻𝗲𝗱 𝗨𝘀𝗲𝗿𝘀 ──────────────────────────────────────────────────────
BANNED_USERS = filters.user()

# ── 📦 𝗥𝘂𝗻𝘁𝗶𝗺𝗲 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲𝘀 ──────────────────────────────────────────────────
adminlist, lyrical, votemode, autoclean, confirmer = {}, {}, {}, [], {}

# ── ✅ 𝗩𝗮𝗹𝗶𝗱𝗮𝘁𝗶𝗼𝗻 ───────────────────────────────────────────────────────────
if SUPPORT_CHANNEL and not re.match(r"^https?://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHANNEL URL. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^https?://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Invalid SUPPORT_CHAT URL. Must start with https://")

if not COOKIE_URL:
    raise SystemExit("[ERROR] - COOKIE_URL is required.")

# Only allow these cookie link formats
if not re.match(r"^https://(batbin\.me|pastebin\.com)/[A-Za-z0-9]+$", COOKIE_URL):
    raise SystemExit("[ERROR] - Invalid COOKIE_URL. Use https://batbin.me/<id> or https://pastebin.com/<id>")


print("""
╔════════════════════════════════════╗
║🎵 𝗩𝗜𝗦𝗛𝗔𝗟 𝗠𝗨𝗦𝗜𝗖 𝗕𝗢𝗧 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗘𝗗𝗜𝗧𝗜𝗢𝗡  
║       ✦ 𝗖𝗼𝗻𝗳𝗶𝗴 𝗟𝗼𝗮𝗱𝗲𝗱 𝗦𝘂𝗰𝗰𝗲𝘀𝘀! ✦   
╚════════════════════════════════════╝
""")
