import librosa
import soundfile as sf
import os
import noisereduce as nr

resampled_dir = r"/NLP/audio_data/resampled"
denoised_dir = r"/NLP/audio_data/denoised"


if not os.path.exists(denoised_dir):
    os.makedirs(denoised_dir)


audio_files = [f"resampled_sample{i}.wav" for i in range(1, 11)]


for audio_file in audio_files:
    try:

        resampled_path = os.path.join(resampled_dir, audio_file).replace("\\", "/")
        denoised_path = os.path.join(denoised_dir, f"denoised_{audio_file}").replace("\\", "/")


        if not os.path.exists(resampled_path):
            print(f"File not found: {resampled_path}")
            continue


        print(f"Loading {resampled_path}")
        audio, sr = librosa.load(resampled_path, sr=16000)


        print(f"Reducing noise for {audio_file}")
        reduced_noise = nr.reduce_noise(y=audio, sr=sr)

        sf.write(denoised_path, reduced_noise, sr)
        print(f"Denoised {audio_file} and saved to {denoised_path}")

    except Exception as e:
        print(f"Error processing {audio_file}: {str(e)}")
        continue