import random
person1 = []
person1win = []
person2 = []
person2win = []
attempt = 0
total = 30
serves = 0

while attempt < total:
    def deuce():
        number = random.uniform(0,1)
        person1 = []
        person2 = []
        if len(person1) == 2 and len(person2) < 1:
            person1win.append(number)
            person1 = []
            person2 = []
            serves = 0
            attempt = attempt + 1
        elif len(person1) < 1and len(person2) == 2:
            person2win.append(number)
            person1 = []
            person2 = []
            serves = 0
            attempt = attempt + 1
        elif len(person1) == 1 and len(person2) == 1:
            deuce()
        else:
            if number <= 0.67:
                person1.append(number)
                serves = serves + 1
            elif number > 0.67:
                person2.append(number)
                serves = serves + 1


    """print("Person 1 ",len(person1))
    print("Person 2 ",len(person2))
    print("Person 1 Wins ", len(person1win))
    print("Person 2 Wins ",len(person2win))"""
    number = random.uniform(0,1)
    if len(person1) == 4 and len(person2) < 3:
        person1win.append(number)
        person1 = []
        person2 = []
        serves = 0
        attempt = attempt + 1
    elif len(person2) == 4 and len(person1) < 3:
        person2win.append(number)
        person1 = []
        person2 = []
        serves = 0
        attempt = attempt + 1
    elif len(person1) == 4 and len(person2) >= 3:
        if number <= 0.67:
            person1.append(number)
            serves = serves + 1
        elif number > 0.67:
            person2.append(number)
            serves = serves + 1
    elif len(person1) == 3 and len(person2) == 3:
        #print("Deuce")
        number = random.uniform(0,1)
        person1 = []
        person2 = []
        if len(person1) == 2 and len(person2) == 0:
            person1win.append(number)
            person1 = []
            person2 = []
            serves = 0
            attempt = attempt + 1
        elif len(person1) == 0 and len(person2) == 2:
            person2win.append(number)
            person1 = []
            person2 = []
            serves = 0
            attempt = attempt + 1
        elif len(person1) == 1 and len(person2) == 1:
            deuce()
        else:
            if number <= 0.67:
                person1.append(number)
                serves = serves + 1
            elif number > 0.67:
                person2.append(number)
                serves = serves + 1

    else:
        if number <= 0.67:
            person1.append(number)
            serves = serves + 1
        elif number > 0.67:
            person2.append(number)
            serves = serves + 1


print("Person 1 has won ", len(person1win), "games.")
print("Person 2 has won ", len(person2win), "games.")
print("You will have won $", len(person1win) * 3)
print("You will have lost $", len(person2win) * 10)


if len(person1win) * 3 > len(person2win) * 10:
    person11 = len(person1win) * 3
    person22 = len(person2win) * 10
    print("You should take the bet. You will win roughly $", person11 - person22)

elif len(person1win) * 3 < len(person2win) * 10:
    person11 = len(person1win) * 3
    person22 = len(person2win) * 10
    print("You should not take the bet. You will loose roughly $", person22 - person11)
