# from Levenshtein import ratio
import difflib
import csv
import os

SETTINGS_DIR = os.path.dirname(__file__)
question = []
answer = []
total_line = 0
with open(os.path.join(SETTINGS_DIR, "database/"+ "QA-pairs.csv"), encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            question.append(row[0])
            answer.append(row[1])
            line_count += 1
total_line = line_count-1

def getAproximateAnswer(q):
    max_score = 0
    for i in range(total_line):
        score = difflib.SequenceMatcher(a=question[i].lower(), b=q).ratio()
        if score >= 0.9: # I'm sure, stop here
            return answer[i]
        elif score > max_score: # I'm unsure, continue
            max_score = score
            curr_answer = answer[i]
    if max_score > 0.8:
        return curr_answer
    return "Sorry, I didn't get you."