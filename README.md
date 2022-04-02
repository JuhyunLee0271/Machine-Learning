KOBERT
- /KoBERT.ipynb: Use "KoBERT" and "Google Colab" to analyze the emotions of worry/joy/sadness/anger/neutrality for short text like diary.

- /emotion_data_filtering.ipynb: Extract only worry/joy/sadness/anger/neutrality from single and continuous conversation datasets and save them as "emotion_data.csv"

- /emotion_data.csv: Dataset for "fine-tuning" of KoBERT downloaded from AI HUB "한국어 감정 정보가 포함된 단발성 대화" (https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-009), "한국어 감정 정보가 포함된 연속적 대화" (https://aihub.or.kr/opendata/keti-data/recognition-laguage/KETI-02-010)

- /kobert_train_log.txt: Logs tested after adjusting "Hyperparameter" and "Dataset Modification" in Colab

Music
- /dataset_filtering.ipynb: After filtering 700,000 music metadata from genres such as Ballad, R&B, Dance, Indie, Idol, and after 10s, approximately 80,000 music metadata are saved in @cleaned_song_meta.json.

- /playlist_processing.ipynb: Using the Metadata of music in @cleaned_song_meta.json and tags for each playlist in @train.json, add 10 tags that appear the most in each music and add count as many as the number of tags included in the playlist to give "weight"

- /tag_clustering.ipynb: With "K-means clustering", Do classification of mood or characteristics using tags of each music (developing)

