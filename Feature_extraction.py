import librosa
import librosa.feature
import numpy as np
import os


vad_dir = r"C:\Users\User\Desktop\FYP development\NLP\audio_data\vad_processed"
features_dir = r"C:\Users\User\Desktop\FYP development\NLP\audio_data\features"


if not os.path.exists(features_dir):
    os.makedirs(features_dir)

audio_files = [f"vad_denoised_resampled_sample{i}.wav" for i in range(1, 11)]


sample_rate = 16000
n_mfcc = 13


for audio_file in audio_files:
    try:

        vad_path = os.path.join(vad_dir, audio_file).replace("\\", "/")
        feature_path = os.path.join(features_dir, f"mfcc_{audio_file.replace('.wav', '.npy')}").replace("\\", "/")


        if not os.path.exists(vad_path):
            print(f"File not found: {vad_path}")
            continue


        print(f"Loading {vad_path}")
        audio, sr = librosa.load(vad_path, sr=sample_rate)


        print(f"Extracting MFCC features for {audio_file}")
        mfccs = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)


        np.save(feature_path, mfccs)
        print(f"Saved MFCC features to {feature_path}")

    except Exception as e:
        print(f"Error processing {audio_file}: {str(e)}")
        continue