import pandas as pd
import json

# Read csv file
df = pd.read_csv("question_json.csv")

empty_answers = df[df["answer"].isna()]
non_empty_answers = df[df["answer"].notna()]

# Create JSON objects for each row
empty_answer_json = [{"question": row['question'], "answer": ""} for _, row in empty_answers.iterrows()]
non_empty_answer_json = [{"question": row['question'], "answer": row['answer']} for _, row in non_empty_answers.iterrows()]

# Write the JSON objects to separate files
with open('empty_answers.json', 'w') as empty_file:
    json.dump(empty_answer_json, empty_file, indent=4)

with open('non_empty_answers.json', 'w') as non_empty_file:
    json.dump(non_empty_answer_json, non_empty_file, indent=4)
