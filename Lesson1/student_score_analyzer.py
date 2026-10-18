# Student Score Analyzer
# I use for loop to let it accept "several" inputs from the user.
# At first, I planned to use only if, elif, and else, but because the instruction mentioned “several” students, I decided to use a for loop to handle multiple students efficiently.

PASSING_SCORE = 75

Scores = []

num_students = int(input("Enter the number of students: "))

for  i in range(num_students):
    score = int(input("Enter score of Student " + str(i + 1) + ": "))
    Scores.append(score)

print ()
print("Student Scores:")

for score in Scores:
    print(score) 


total = 0
highest = Scores [0]
lowest = Scores [0]  
passed_count = 0
failed_count = 0

print ()

for i in range (num_students):
    score = Scores[i]

    if score >= PASSING_SCORE:
        status= "Passed" 
        passed_count = passed_count + 1
    else:
        status= "Failed"
        failed_count = failed_count + 1

    if score >= 90:
        remarks = "Excellent"
    elif score >= 80:
        remarks = "Very Good"
    elif score >= 75:
        remarks = "Good"
    else:
        remarks = "Failed"

    if status == "Failed":
        print("Student", i+1, ":",score, "- Failed" )
    else:
        print("Student", i+1, ":",score, "-", remarks, "-", status)



    total = total + score

    if score > highest:
        highest = score

    if score < lowest:
        lowest = score

    average = total / num_students

    print ()
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Passed:", passed_count)