def atk():
    print("You are attacking GER, choose 5 move combo!")
    s = ["1.Light Punch", "2. Heavy Punch", "3. Light Kick", "4. Heavy Kick", "5. Stab"]
    for j in s:
        print(j)


e = []
k = ["Light Punch", "Heavy Punch", "Light Kick", "Heavy Kick", "Stab"]
i = 0
while i < 5:
    atk()
    m = input("Enter your move : ")
    if m == "1" or m == "2" or m == "3" or m == "4" or m == "5":
        e.append(k[int(m) - 1])
        i += 1
    else:
        print("Not a possible move!")
print(e)
# def ger_counter():
