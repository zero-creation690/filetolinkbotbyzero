import re
from typing import Set, Optional, List, Dict
from Script import script  # Custom script file with caption & other settings

# 🚀 Bot Session and Token Information
SESSION = 'Webavbot'  # Pyrogram client session name

API_ID = 20288994  # Telegram API ID
API_HASH = 'd702614912f1ad370a0d18786002adbf'  # Telegram API Hash
BOT_TOKEN = '8404573397:AAHHN_v5kfMi8aH_ATvIk4AsLLbQDKieIcY'  # Telegram Bot Token

# 👑, Channels & Logs
BIN_CHANNEL = -1003180324078  # File storage channel
LOG_CHANNEL = -1003180324078  # General log channel
PREMIUM_LOGS = -1003180324078  # Premium user actions log
VERIFIED_LOG = -1003180324078  # Verified user actions log
SUPPORT_GROUP = -1003180324078

# add admin IDs 11111 2222 3333 and add auth channel IDs -100XXX -100XXX -100XXX
ADMINS = [8304706556]  # List of admin user IDs
AUTH_CHANNEL = [-1003180324078]  # Allowed channels for authorization

# username add without @
OWNER_USERNAME = 'Zeroboy216'  # Owner's username
BOT_USERNAME = 'filetolink678bot'  # Bot's username

# 🔗 Channel & Support Links
CHANNEL = 'https://t.me/AV_BOTz_UPDATE'  # Updates channel
SUPPORT = 'https://t.me/AV_SUPPORT_GROUP'  # Support group
HOW_TO_VERIFY = 'https://t.me/'  # Verification guide link
HOW_TO_OPEN = 'https://t.me/'  # File access guide link

# ✅ Feature Toggles (True/False)
VERIFY = False  # Enable user verification
FSUB = True  # Force Subscribe feature
ENABLE_LIMIT = True  # Enable file limits
BATCH_VERIFY = False  # Verify files in batch
IS_SHORTLINK = False  # Enable channel shortlink creation
MAINTENANCE_MODE = False  # Put bot in maintenance
PROTECT_CONTENT = False  # Enable content protection
PUBLIC_FILE_STORE = True  # Public or private file visibility
BATCH_PROTECT_CONTENT = False  # Batch file protection

# 🔗 Shortlink Configuration
SHORTLINK_URL = 'techvjlink.site'  # Shortener site
SHORTLINK_API = 'd73e70a35dc3877fa14afbf51fa8ec312c94780c'  # API key for shortlink

# 💾 MongoDB Connection Information
DB_URL = "mongodb+srv://zerocreative966_db_use:jCg1ckVQk4JCBI4K@filetolink.xkjyqdk.mongodb.net/?retryWrites=true&w=majority&appName=Filetolink"  # MongoDB connection URI
DB_NAME = "cluster0"  # MongoDB database name

# 📸 all Media (Images)
QR_CODE = 'https://graph.org/file/6afb4093d5ec5c4176979.jpg'  # QR Code image
VERIFY_IMG = "https://graph.org/file/1669ab9af68eaa62c3ca4.jpg"  # Verify success image
AUTH_PICS = 'https://envs.sh/AwV.jpg'  # Auth step image
PICS = 'https://envs.sh/_pM.jpg'  # Default info image
FILE_PIC = 'https://i.ibb.co/bj4My0bW/photo-2025-07-21-02-15-21-7529360175656861700.jpg' # file image 

# 📝 File Captions
FILE_CAPTION = f"{script.CAPTION}"  # Caption for single file
BATCH_FILE_CAPTION = f"{script.CAPTION}"  # Caption for batch files
CHANNEL_FILE_CAPTION = f"{script.CAPTION}"  # Caption for channel posts

# ⏱️ Time & Rate Limit Settings
PING_INTERVAL = 1200  # Ping interval in seconds (20 minutes)
SLEEP_THRESHOLD = 60  # Threshold for sleep delay
RATE_LIMIT_TIMEOUT = 600  # Rate limit time (10 mins)
MAX_FILES = 5  # Max files allowed per user
VERIFY_EXPIRE = 60  # Time (in hours) after which verification expires

# ⚙️ Worker Configuration
WORKERS = 4  # Number of async workers
MULTI_CLIENT = False  # Enable multi-client handling (if needed)

# 🔧 App/Heroku Configuration
name = 'avbotz'  # Project name
APP_NAME = None
ON_HEROKU = False

# 🌐 Server Settings
PORT = 2626  # Port for web server
NO_PORT = False  # Disable port in URL
HAS_SSL = False  # Use HTTPS if True
BIND_ADDRESS = "127.0.0.1"  # Server bind address
FQDN = BIND_ADDRESS  # Full domain name or fallback to bind address
PORT_SEGMENT = ":2626/"  # Port in URL if not disabled
PROTOCOL = "http"  # Protocol for URL
URL = f"{PROTOCOL}://{FQDN}{PORT_SEGMENT}"  # Final generated base URL
