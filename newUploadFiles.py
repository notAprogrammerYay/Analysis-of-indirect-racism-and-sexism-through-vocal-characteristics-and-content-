import os
import subprocess

# Φάκελοι με κατηγορίες και αρχεία ήχου
CATEGORIES = {
    'sexism': '/Users/annatolia/Desktop/myenv/ml/in_here/myenv_py39/sexism',
    'racism': '/Users/annatolia/Desktop/myenv/ml/in_here/myenv_py39/racism',
    'irony': '/Users/annatolia/Desktop/myenv/ml/in_here/myenv_py39/irony',
}

# Επιλογές WhisperX
MODEL = "medium"
LANGUAGE = "el"
COMPUTE_TYPE = "float32"  # Ρύθμιση για μεγαλύτερη συμβατότητα
OUTPUT_SUFFIX = "transcriptions_summary"  # Τελικό όνομα αρχείου εξόδου

# Διαχείριση κατηγοριών
for category, folder_path in CATEGORIES.items():
    print(f"Processing category: {category}")

    # Λίστα αρχείων .mp3 στον φάκελο
    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
    if not audio_files:
        print(f"No audio files found in category '{category}'. Skipping.")
        continue

    output_file = os.path.join(folder_path, f"{OUTPUT_SUFFIX}_{category}.txt")

    with open(output_file, "w") as summary_file:
        for audio_file in audio_files:
            audio_path = os.path.join(folder_path, audio_file)
            print(f"Transcribing: {audio_path}")

            try:
                # Εκτέλεση WhisperX με υποστήριξη float32
                result = subprocess.run(
                    [
                        "whisperx",
                        audio_path,
                        "--model", MODEL,
                        "--language", LANGUAGE,
                        "--compute_type", COMPUTE_TYPE,  # Χρήση float32
                        "--output_dir", folder_path,
                        "--output_format", "txt"  # Εξαγωγή μόνο σε txt
                    ],
                    capture_output=True,
                    text=True
                )

                if result.returncode == 0:
                    print(f"Transcription completed: {audio_file}")
                    # Καταγραφή επιτυχούς μεταγραφής
                    summary_file.write(f"File: {audio_file}\n")
                    summary_file.write(f"Output: {result.stdout}\n\n")
                else:
                    print(f"Failed to transcribe: {audio_file}")
                    print(f"Error: {result.stderr}")
                    # Καταγραφή αποτυχίας
                    summary_file.write(f"File: {audio_file}\n")
                    summary_file.write(f"Error: {result.stderr}\n\n")

            except Exception as e:
                print(f"Error processing {audio_file}: {str(e)}")
                summary_file.write(f"File: {audio_file}\n")
                summary_file.write(f"Error: {str(e)}\n\n")

    print(f"Transcriptions saved to {output_file}")

print("All categories processed.")
