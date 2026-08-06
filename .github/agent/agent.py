import os, subprocess
from dotenv import load_dotenv
load_dotenv()
CHANNEL_NAME = os.getenv("CHANNEL_NAME", "@im_most_pro")
print(f"Agent chal gaya for {CHANNEL_NAME}")
