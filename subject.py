from room_game.description import*


class Candle:
    def __init__(self, description):
        self.description = description
        self.prop = ["fireable"]

class Match:
    def __init__(self, description):
        self.description = description
        self.prop = ["fire"]

class Gobelin:
    def __init__(self, description):
        self.description = description
        self.prop = ["fireable"]

def act_fire(subj1,subj2):
    if "fireable" in subj1.prop and "fire" in subj2.prop:
        subj1.description = "Горящая спичка"
        subj1.prop.remove("fireable")
        subj1.prop.append("burning")
        return [subj1,subj2]
    if "fireable" in subj2.prop and "fire" in subj1.prop:
        return
    print("Действие невозможно")
    return [subj1,subj2]





def create_subject(id, description):
   if id=="Свеча":
       return Candle(description)
   if id=="Спичка":
       return Match(description)
   if id=="Гобелен":
       return Gobelin(description)



# не нужен наверное False здесь
def execute_action(action,subject):
   def look_at_this(subject):
       #print("я нахожусь в комнате "+ room.name)
       print(subject.description)
       return [False, subject]

   if action == "Рассмотреть":
       return look_at_this(subject)

   print("Вы ввели неверное действие. Повторите попытку.")
   return [False, subject]
