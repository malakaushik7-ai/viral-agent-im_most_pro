import librosa

def get_beat_points(audio_path, edit_duration=15):
    print(f"[BEAT SYNC] Analyzing: {audio_path}")
    y, sr = librosa.load(audio_path)
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    sync_points = [t for t in beat_times if t < edit_duration][::2]
    print(f"[BEAT SYNC] BPM: {tempo:.0f} | Cut Points: {len(sync_points)}")
    return sync_points
