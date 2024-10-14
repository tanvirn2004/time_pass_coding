print("welcome to test your love score by your names ")
name1= input("name 1 : ")
name2= input(" name 2 :")
combine_names = name1 + name2
lower_names = combine_names.lower()
t = combine_names.count("t")
r = combine_names.count("r")
u = combine_names.count("u")
e = combine_names.count("e")
first_name_score = t + r + u + e
l = combine_names.count("l")
o = combine_names.count("o")
v = combine_names.count("v")
e = combine_names.count("e")
second_name_score = l + o + v + e
score = int(str(first_name_score) + str(second_name_score))
if score < 10 or score > 90:
    print(f"our score is {score}, you guys go together like coke and mentos" )
elif score >=40 and score <=50 :
    print(f"our score is {score}, you guys are alright together" )
else:

    print(f"Your love score is {score} ")