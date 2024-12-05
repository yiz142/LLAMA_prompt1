# src/data_loader.py

import os
import pandas as pd

def load_dbpedia_dataset(test_file_path, class_file_path):
    """Load the DBpedia dataset."""
    with open(class_file_path, "r", encoding="utf-8") as f:
        classes = [line.strip() for line in f.readlines()]
    class_map = {str(i + 1): cls for i, cls in enumerate(classes)}
    df = pd.read_csv(
        test_file_path,
        header=None,
        names=["class", "title", "content"],
        encoding="utf-8",
    )
    df["class"] = df["class"].astype(str).map(class_map)
    return df

def load_nyt_dataset(data_dir):
    """Load the NYT dataset."""
    phrase_file = os.path.join(data_dir, 'phrase_text.txt')
    topics_file = os.path.join(data_dir, 'topics.txt')
    topics_label_file = os.path.join(data_dir, 'topics_label.txt')

    with open(phrase_file, 'r', encoding='utf-8') as f:
        phrases = [line.strip() for line in f]
    with open(topics_file, 'r', encoding='utf-8') as f:
        topics = [line.strip() for line in f]
    with open(topics_label_file, 'r', encoding='utf-8') as f:
        topic_labels = [int(line.strip()) for line in f]

    topic_mapping = {i: name for i, name in enumerate(topics)}
    data = []
    for i, phrase in enumerate(phrases):
        topic = topic_mapping.get(topic_labels[i], "Unknown")
        data.append({
            'text': phrase,
            'class': topic,
        })
    return data, topics

def load_yelp_dataset(file_path):
    """Load the Yelp dataset."""
    class_map = {
        "1": "Very Negative",
        "2": "Negative",
        "3": "Neutral",
        "4": "Positive",
        "5": "Very Positive"
    }
    df = pd.read_csv(
        file_path,
        header=None,
        names=["class", "review"],
        encoding="utf-8",
    )
    df["class"] = df["class"].astype(str).map(class_map)
    return df
