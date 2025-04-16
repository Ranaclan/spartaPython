x = 2
y = 5.4
z = " there's now a number 25.4 unless we put a space in!"
print(str(x) + str(y) + str(z))

int_string = "6"
int_string = int(int_string)
print(type(int_string))
int_string = float(int_string)
print(type(int_string))

years = 7
height_cm = 60.2
# print these variables in an f-string so that it outputs this to the screen:

print(f"Lassie is {years} years old and {height_cm} cm tall.")

pi = 3.14159265359
print(f"{round(pi, 3)}")
print(f"{round(pi, 5)}")

score = 16
max_score = 26
score_as_decimal = score/max_score
print(f"You scored {score_as_decimal}")
print(f"You scored {score_as_decimal * 100}%")
print(f"You scored {round(score_as_decimal * 100, 2)}%")
print(f"You scored {round(score_as_decimal * 100)}%")