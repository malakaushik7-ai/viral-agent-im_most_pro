import os
from dotenv import load_dotenv
load_dotenv()

CHANNEL_NAME = os.getenv("CHANNEL_NAME", "@im_most_pro")
EDITS_PER_RUN = 5
NO_AI_CLIPS = True

def main():
    print(f"✅ Agent started for {CHANNEL_NAME}")
    print(f"Making {EDITS_PER_RUN} edits with watermark only")

if __name__ == "__main__": 
    main()
