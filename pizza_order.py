print("Congratulations!, you've got a job at python pizaa! Your first job is to build "
      "an automatic pizza order program")
s_pizza = 15
m_pizza = 20
l_pizza = 25
s_pep = 2
l_m_pep = 3
cheese = 1
print(f"pizza prizes small pizza: {s_pizza}, medium  pizza: {m_pizza}, large pizza :{l_pizza}")

order = input("do you want to order? Type Yes or No: ")
if order == "yes":
    print("what kind of pizza you want? for small pizza type:S, Medium pizza : M and Large pizza = L")
    ordr = input("S, M or L: ")
    if  ordr == "S":
        bill = s_pizza
        print(f"it's {bill} dollar ")

    elif ordr == "M":
        bill = m_pizza
        print(f"it's {bill} dollar ")

    elif ordr == "L":
        bill = l_pizza
        print(f"it's {l_pizza} dollar ")
    else:
        print("wrong order try order again by clicking play buttom ")

    add_pep = input("do you want to add pepperoni in pizza? Type yes or No: ")
    if add_pep == "yes" and ordr == "S":
        bill += 2

    elif add_pep == "yes" and ordr =="M" or add_pep == "yes" and ordr == "L":
        bill += 3
    else:
        print("Okay let's talk about Cheese ")
    cheese= input("do you want to add cheese in pizza? Type yes or no: ")
    if cheese == "yes":
        bill += 1
        print(f"you total bill is  {bill} dollar ")

    elif cheese == "no":
        print(f"your total bill is  {bill} dollar ")
    else:
        print(f"thank you, Your bill is {bill} dollar ")
elif order == "no":
    print(
        "Okay then you can stay here for 10 minutes to decide whether you want to order or not as we are short of space "
        "then leave as  customers are waiting ")
else:
    print("Then please leave as we have short in space")












