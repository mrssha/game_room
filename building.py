#from room_game.description import*
import description
from subject import *

class Room:
    # name=""
    # description = ""
    # doors = {}
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.doors = {}
        self.content = {}

    def bind(self, dir, room):
        if dir in self.doors:
            raise Exception("Направление уже задано")
        self.doors[dir] = room
        room.doors[self.reverse_dir(dir)] = self

    def reverse_dir(self,dir):
        if dir == "west": return "east"
        if dir == "east": return "west"
        if dir == "north": return "south"
        if dir == "south": return "north"

    def add_content(self,subj):
        if isinstance(subj, Subject):
            self.content[subj.name]=subj
            #self.content.append(subj)

        else:
            raise Exception("Добавляемый элемент {} не является предметом.".format(subj))


def create_rooms():
    room1 = Room("Столовая", description.ROOM_DESCRIPTION["Столовая"])
    room2 = Room("Холл", description.ROOM_DESCRIPTION["Холл"])
    room3 = Room("Спальня", description.ROOM_DESCRIPTION["Спальня"])
    room4 = Room("Кухня", description.ROOM_DESCRIPTION["Кухня"])
    room5 = Room("Коридор", description.ROOM_DESCRIPTION["Коридор"])
    room6 = Room("Зал", description.ROOM_DESCRIPTION["Зал"])

    room1.bind("west", room4)
    room1.bind("north", room2)
    room1.bind("east", room6)
    room5.bind("east", room3)
    room5.bind("west", room2)
    room5.bind("south", room6)

    room6.add_content(gobelin1)
    room4.add_content(match1)
    room1.add_content(candle1)
    return room2



def execute_command(command, room):

    def look_around(room):
        #print("я нахожусь в комнате "+ room.name)
        assert len(room.doors)>0, "Ошибка: в текущей комнате нет двери"
        for dir,another_room in room.doors.items():
            print("Я вижу дверь на " + dir + ". За этой дверью находится " + another_room.name )
        return [False, room]


    def go(dir,room):
        if dir in room.doors:
            return [True, room.doors[dir]]
        print("В направлении " + dir + " нет дверей.")
        return [False, room]


    def find(room):
        if len(room.content)==0:
            print("В этой комнате нет ничего интересного")
        else:
            list_content=""
            for subj in room.content.keys():
                list_content= list_content + subj + ", "
                print("В этой комнате вы находите:", list_content)
        return [False, room]


    def look_at_this(room, name_subject):
        if name_subject in room.content:
            subj = room.content[name_subject]
            print(subj.description)
        else:
            print("В этой комнате нет предмета  " + name_subject)
        return [False, room]


    def take_this(room, name_subject):
        if name_subject in room.content:
            subj = room.content[name_subject]
            if "takeable" in subj.prop:
                BASKET[name_subject] = subj
                print ("Предмет ", name_subject, "добавлен в вашу корзину")
                del room.content[name_subject]
            else:
                print("Вы не можете взять с собой " + name_subject, "Попробуйте что-нибудь другое")
        else:
            print("В этой комнате нет предмета  " + name_subject)
        return [False, room]

    def act_fire(room):
        name_subj1 = input("Какой предмет вы хотите зажечь? ")
        name_subj2 = input("С помощью чего будете зажигать? ")
        if name_subj1 in BASKET and name_subj2 in BASKET:
            subj1 = BASKET[name_subj1]
            if "fireable" in subj1.prop and "fire" in BASKET[name_subj2].prop:
                desc = subj1.description
                subj1.description = desc + " Горит."
                subj1.prop.remove("fireable")
                subj1.prop.append("burning")
                BASKET[name_subj1] = subj1
                print("Вы зажгли обект", name_subj1)
                return [False, room]
            print("Действие невозможно")
        else:
            print("У вас есть не все из перечисленных предметов")
        return [False, room]


    if command == "act fire":
            return act_fire(room)

    if command[:5] == "take ":
        return take_this(room, command[5:])

    if command[:8] == "look at ":
        return look_at_this(room, command[8:])

    if command == "look around":
        return look_around(room)

    if command[:3]=="go ":
        return go(command[3:],room)

    if command == "find":
        return find(room)

    print("Вы ввели неверную команду. Введите еще раз.")
    return [False, room]

