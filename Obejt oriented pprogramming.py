class person:
    def __init__(self, name, yearOfBirth, monthOfBirth, dayOfBirth):
        import datetime
        an = datetime.datetime.now()
        self.currentYear = an.year
        self.currentMonth = an.month
        self.currentDay = an.day

        self.yearOfBirth = yearOfBirth
        self.monthOfBirth = monthOfBirth
        self.dayOfBirth = dayOfBirth
        self.name = name

    def calculateAge(self):# Based on the fact a month is 30 days

        deltaDay = int(self.currentDay) - int(self.dayOfBirth) 
        deltaMonth = int(self.currentMonth) - int(self.monthOfBirth)
        deltaYear = int(self.currentYear) - int(self.yearOfBirth)

        if deltaDay < 0 :
            deltaDay = deltaDay + 30 ; deltaMonth = deltaMonth - 1
        if deltaMonth < 0 :
            deltaMonth = deltaMonth + 12 ; deltaYear = deltaYear - 1
        totalDay = deltaDay + deltaMonth * 30 + deltaYear * 365
        introduce = f"Hello I'm {self.name} and I'm {deltaYear} years {deltaMonth} months {deltaDay} days old.\nI lived {totalDay} day in total."
        return introduce

try: 
    name = input("What is your name? : ")
    birthOfYear = int(input("What is your birth year? :"))
    birthOfMonth = int(input("What is your birth month? :"))
    birthOfDay = int(input("What is your birh day? :"))
except: 
    print("ERROR!\nPlease try again:( ")
p1 = person(name, birthOfYear, birthOfMonth, birthOfDay)
p1age = p1.calculateAge()
print(p1age)

