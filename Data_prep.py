import librosa
import soundfile as sf
import os


source_dir = r"/NLP/audio_data/raw"
target_dir = r"/NLP/audio_data/resampled"


if not os.path.exists(target_dir):
    os.makedirs(target_dir)


audio_files = [f"sample{i}.wav" for i in range(1, 11)]


for audio_file in audio_files:

    source_path = os.path.join(source_dir, audio_file)
    target_path = os.path.join(target_dir, f"resampled_{audio_file}")


    audio, sr = librosa.load(source_path, sr=16000)


    sf.write(target_path, audio, sr)
    print(f"Resampled {audio_file} and saved to {target_path}")