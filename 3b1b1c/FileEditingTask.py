with open("students.txt", "r") as file:
    lines = file.readlines()

students = []
for line in lines:
    name, score = line.strip().split()
    students.append((name, int(score)))

total_score = 0
scores = []
score_counts = {}
for student in students:
    score = student[1]
    total_score += score
    scores.append(score)
    if score in score_counts:
        score_counts[score] += 1
    else:
        score_counts[score] = 1

average_score = total_score / len(students)
highest_score = max(scores)
lowest_score = min(scores)

mode_score = max(score_counts, key=score_counts.get)
