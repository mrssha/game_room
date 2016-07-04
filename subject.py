import description


BASKET = {}

class Subject:
    pass

class Candle(Subject):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.prop = ["fireable", "takeable"]

class Match(Subject):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.prop = ["fire", "takeable"]

class Gobelin(Subject):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.prop = ["fireable"]

def create_subject(name, description):
   if name=="Свеча":
       return Candle(name, description)
   if name=="Спичка":
       return Match(name, description)
   if name=="Гобелен":
       return Gobelin(name, description)

match1 = create_subject("Спичка", description.SUBJECT_DESCRIPTION["Спичка"])
candle1 = create_subject("Свеча", description.SUBJECT_DESCRIPTION["Свеча"])
gobelin1= create_subject("Гобелен", description.SUBJECT_DESCRIPTION["Гобелен"])
gobelin2= create_subject("Гобелен", description.SUBJECT_DESCRIPTION["Гобелен"])



"""
def execute_action(action,subject):
   def look_at_this(subject):
       #print("я нахожусь в комнате "+ room.name)
       print(subject.description)
       return [False, subject]

   if action == "Рассмотреть":
       return look_at_this(subject)

   print("Вы ввели неверное действие. Повторите попытку.")
   return [False, subject]
"""