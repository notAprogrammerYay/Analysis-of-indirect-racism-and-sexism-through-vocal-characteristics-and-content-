import os
import subprocess

# Λίστα φακέλων προς επεξεργασία
CATEGORIES = {
    'sexism': '/Users/annatolia/Desktop/myenv/ml/in_here/myenv_py39/sexism',
    'racism': '/Users/annatolia/Desktop/myenv/ml/in_here/myenv_py39/racism',
    'irony': '/Users/annatolia/Desktop/myenv/ml/in_here/myenv_py39/irony',
}

# Διαχείριση όλων των κατηγοριών
for category, folder_path in CATEGORIES.items():
    print(f"Processing category: {category}")
    transcript_ids_file = os.path.join(folder_path, f'transcript_ids_{category}.txt')
    transcriptions_summary_file = os.path.join(folder_path, f'transcriptions_summary_{category}.txt')

    transcriptions = {}

    # Εύρεση και μεταγραφή όλων των .mp3 αρχείων στον φάκελο
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.mp3'):  # Φιλτράρισμα για .mp3 αρχεία
            file_path = os.path.join(folder_path, file_name)
            output_file = os.path.join(folder_path, f"{os.path.splitext(file_name)[0]}_transcription.txt")

            # Εκτέλεση WhisperX
            try:
                subprocess.run(
                    [
                        "whisperx",
                        file_path,
                        "--model", "medium",  # Επέλεξε το μοντέλο που θέλεις (tiny, base, small, medium, large)
                        "--language", "el",  # Ελληνικά
                        "--compute_type", "float32",  # Χρήση float32 για αποφυγή προβλήματος
                        "--output_dir", folder_path
                    ],
                    check=True
                )
                print(f"Transcribed: {file_name}")
                transcriptions[file_name] = output_file
            except subprocess.CalledProcessError as e:
                print(f"Failed to transcribe: {file_name} - {e}")

    # Αποθήκευση των μεταγραφών ανά κατηγορία
    with open(transcriptions_summary_file, 'w') as f:
        for file_name, transcript_path in transcriptions.items():
            f.write(f"{file_name}: {transcript_path}\n")

    print(f"Processed {len(transcriptions)} files for category '{category}'. Transcriptions saved to {transcriptions_summary_file}.")

print("All categories processed.")
