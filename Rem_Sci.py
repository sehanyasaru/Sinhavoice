import librosa
import soundfile as sf
import os
from pydub import AudioSegment
import numpy as np


denoised_dir = r"/NLP/audio_data/denoised"
vad_dir = r"/NLP/audio_data/vad_processed"


if not os.path.exists(vad_dir):
    os.makedirs(vad_dir)


audio_files = [f"denoised_resampled_sample{i}.wav" for i in range(1, 11)]


for audio_file in audio_files:
    try:

        denoised_path = os.path.join(denoised_dir, audio_file).replace("\\", "/")
        vad_path = os.path.join(vad_dir, f"vad_{audio_file}").replace("\\", "/")

        if not os.path.exists(denoised_path):
            print(f"File not found: {denoised_path}")
            continue

        print(f"Loading {denoised_path}")
        audio = AudioSegment.from_wav(denoised_path)
        audio_no_silence = audio.strip_silence(silence_len=25, silence_thresh=-60, padding=20)
        audio_array = np.array(audio_no_silence.get_array_of_samples(), dtype=np.float32) / (2**15)
        sample_rate = audio.frame_rate

        sf.write(vad_path, audio_array, sample_rate)
        print(f"Processed {audio_file} with VAD and saved to {vad_path}")

    except Exception as e:
        print(f"Error processing {audio_file}: {str(e)}")
        continue