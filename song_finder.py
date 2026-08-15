import yt_dlp
import os

MOOD_MAP = {
    "aura": ["phonk", "drift phonk"],
    "fight": ["aggressive phonk", "epic trap"],
    "sad": ["slowed reverb", "sad phonk"],
    "horror": ["horror phonk"],
    "meme": ["funk", "brazilian funk"]
}

def get_mood(prompt):
    prompt = prompt.lower()
    if "sad" in prompt: return "sad"
    if "fight" in prompt or "vs" in prompt: return "fight"
    if "funny" in prompt: return "meme"
    if "horror" in prompt: return "horror"
    return "aura"

def download_trending_song(prompt, output_path="temp_song.mp3"):
    mood = get_mood(prompt)
    query = f"trending {MOOD_MAP[mood][0]} 2026 no copyright"

    print(f"[SONG FINDER] Mood: {mood} | Query: {query}")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch1:{query}"])

    return {"path": output_path, "mood": mood}
