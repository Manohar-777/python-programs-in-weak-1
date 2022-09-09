
d_marks = {}
avg_marks = {}
avg_course = {}
for i in range(1,6): # We loop for 5 students
    d_marks[f'Student {i} (courses 1-4)'] = list(map(int, input(f"Student {i} (courses 1-4): ").split())) # Split the string and creates an integer list
    avg_marks[f'Average of Student {i}'] = sum(d_marks[f'Student {i} (courses 1-4)']) / len(d_marks[f'Student {i} (courses 1-4)']) #Create average dictionary for Students
    for j in range(1, len(d_marks[f'Student {i} (courses 1-4)'])+1):
        if f'Course {j} sum' in avg_course: # if course sum already in dictionary then add it to previous. 
            avg_course[f'Course {j} sum'] += d_marks[f'Student {i} (courses 1-4)'][j-1]
        else:
            avg_course[f'Course {j} sum'] = d_marks[f'Student {i} (courses 1-4)'][j-1] # if course sum not in dictionary then create one. 

print("The Highest average mark of students =", max(avg_marks.values()))
print("The Highest average mark of courses =", max(avg_course.values())/ len(d_marks))

