# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass

class Male(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Objects")

class Female(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Light Objects")

def getGender(name):
    if "A/L" in name:
        return Male()
    else:
        return Female()


# Pythn dynamically set the data type for the gender variable
# sometimes it becomes male object
# sometimes it becomes female object
gender = getGender("Khairi A/L Abu Bakar")
gender.doCarryObjects()
print(type(gender))

gender = getGender("Aida A/P Abu Bakar")
gender.doCarryObjects()
print(type(gender))

# python so clever, how python can identify that khairi and aida is male and female respectively without mentionning
