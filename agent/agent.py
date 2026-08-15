from song_finder import download_trending_song
from beat_sync import get_beat_points

class ViralAgent:
    def __init__(self):
        pass

    def run(self, prompt):
        print(f"[VIRAL AGENT] Prompt: {prompt}")

        # Step 1: Song dhundo
        song = download_trending_song(prompt)

        # Step 2: Beat nikalo
        beats = get_beat_points(song["path"])

        # Step 3: Agla step yahi se call hoga
        return {"song": song, "beats": beats, "status": "Ready for Mix Edit"}
