
![pipe](https://github.com/user-attachments/assets/c92b399a-273c-4f67-97d3-fd17acfbc670)
# Audio Processing Pipeline 🎵

## Overview

This project implements a pipeline for processing audio files, including resampling, noise reduction, voice activity detection (VAD), and MFCC feature extraction. It processes a set of WAV audio files through multiple stages to prepare them for further analysis or machine learning tasks, such as speech recognition or audio classification. 🚀

## Features

- **Resampling**: Resamples audio files to a consistent 16kHz sample rate using `librosa`. 🔄
- **Noise Reduction**: Applies noise reduction with the `noisereduce` library. 🎧
- **Voice Activity Detection (VAD)**: Removes silence from audio files using `pydub`. ✂️
- **MFCC Feature Extraction**: Extracts Mel-frequency cepstral coefficients (MFCCs) for audio analysis using `librosa`. 📊
- **Modular Pipeline**: Processes multiple audio files in a structured directory-based workflow. 🗂️

## Project Structure

- `Data_prep.py`: Resamples raw audio files to 16kHz and saves them to the `resampled` directory. 🔄
- `Noice_redu.py`: Applies noise reduction to resampled audio files and saves them to the `denoised` directory. 🎧
- `Rem_Sci.py`: Performs VAD to remove silence and saves processed files to the `vad_processed` directory. ✂️
- `Feature_extraction.py`: Extracts MFCC features from VAD-processed files and saves them as NumPy arrays in the `features` directory. 📊
- `audio_data/`: Directory structure for audio files:
  - `raw/`: Stores raw input WAV files (e.g., `sample1.wav` to `sample10.wav`). 📂
  - `resampled/`: Stores resampled audio files. 📂
  - `denoised/`: Stores noise-reduced audio files. 📂
  - `vad_processed/`: Stores VAD-processed audio files. 📂
  - `features/`: Stores MFCC feature files (`.npy`). 📂
- `images/`: Directory for images (e.g., `pipeline-diagram.png`). 🖼️

## Prerequisites

- Python 3.11.9 🐍
- Required libraries:

  ```bash
  pip install librosa soundfile pydub noisereduce numpy
  ```
- FFmpeg (required for `pydub`):
  - Install FFmpeg and add it to your system PATH. On Windows, download from FFmpeg's official site or install via a package manager (e.g., `apt install ffmpeg` on Ubuntu, `brew install ffmpeg` on macOS).

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/audio-processing-pipeline.git
   cd audio-processing-pipeline
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Install FFmpeg**:

   - Follow the instructions for your operating system to install FFmpeg.
   - Verify installation:

     ```bash
     ffmpeg -version
     ```

4. **Prepare Audio Files**:

   - Place your raw WAV files (e.g., `sample1.wav` to `sample10.wav`) in the `audio_data/raw/` directory.
   - Update the `audio_files` list in each script if your file names differ.

5. **Create Directory Structure**:

   - Ensure the `audio_data` directory exists with subdirectories:

     ```bash
     mkdir -p audio_data/raw audio_data/resampled audio_data/denoised audio_data/vad_processed audio_data/features
     ```

## Usage

1. **Run the Pipeline**:

   - Execute the scripts in sequence to process the audio files:

     ```bash
     python Data_prep.py
     python Noice_redu.py
     python Rem_Sci.py
     python Feature_extraction.py
     ```
   - Each script processes files from the previous stage and saves outputs to the corresponding directory.

2. **Script Details**:

   - **Data_prep.py**: Resamples raw audio files to 16kHz and saves them as `resampled_sampleX.wav`.
   - **Noice_redu.py**: Reduces noise in resampled files and saves them as `denoised_resampled_sampleX.wav`.
   - **Rem_Sci.py**: Removes silence from denoised files using VAD and saves them as `vad_denoised_resampled_sampleX.wav`.
   - **Feature_extraction.py**: Extracts MFCC features (13 coefficients) from VAD-processed files and saves them as `mfcc_vad_denoised_resampled_sampleX.npy`.

3. **Example Output**:

   - After running `Feature_extraction.py`, you’ll find MFCC feature files in `audio_data/features/`. Example:

     ```bash
     audio_data/features/mfcc_vad_denoised_resampled_sample1.npy
     ```
   - To load and inspect MFCCs:

     ```python
     import numpy as np
     mfccs = np.load("audio_data/features/mfcc_vad_denoised_resampled_sample1.npy")
     print(mfccs.shape)  # Example: (13, num_frames)
     ```

## Dependencies

- `librosa`: For audio processing and MFCC extraction. 🎵
- `soundfile`: For reading and writing audio files. 💾
- `pydub`: For VAD and silence removal. ✂️
- `noisereduce`: For noise reduction. 🎧
- `numpy`: For numerical operations and saving MFCCs. 🔢

## Notes

- Ensure all audio files are in WAV format and named `sample1.wav` to `sample10.wav` in the `raw` directory, or update the `audio_files` list in each script. 📍
- The pipeline assumes a 16kHz sample rate for consistency; adjust `sr=16000` in scripts if needed. ⚙️
- VAD parameters in `Rem_Sci.py` (`silence_len=25`, `silence_thresh=-60`, `padding=20`) can be tuned for better silence detection. 🔧
- If an audio file fails to process, the scripts will skip it and log the error. 🛠️
- For large datasets, consider parallel processing or batch scripts to optimize performance. ⚡

## Contributing

1. Fork the repository. 🍴
2. Create a new branch (`git checkout -b feature-branch`). 🌱
3. Make your changes and commit (`git commit -m "Add feature"`). ✍️
4. Push to the branch (`git push origin feature-branch`). 🚀
5. Create a pull request. 🤝

## 
