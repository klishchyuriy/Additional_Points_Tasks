with open("students.txt", "r") as file:
    students = [(line.split()[0], int(line.split()[1])) for line in file]

total_score = sum(score for _, score in students)
scores = [score for _, score in students]
score_counts = {score: scores.count(score) for score in set(scores)}

average_score = total_score / len(students)
highest_score = max(scores)
lowest_score = min(scores)
mode_score = max(score_counts, key=score_counts.get)

with open('student_results.txt', 'w') as file:
    file.write('Student Scores:\n')
    file.writelines([f'{name}: {score}\n' for name, score in students])

    file.write('\nStatistics:\n')
    file.write(f'Average Score: {average_score:.2f}\n')
    file.write(f'Highest Score: {highest_score}\n')
    file.write(f'Lowest Score: {lowest_score}\n')
    file.write(f'Mode Score: {mode_score}\n')

print('Task completed. Check the "student_results.txt" file for results.')
