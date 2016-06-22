from room_game.description import*

class Room:
   # name=""
   # description = ""
   # doors = {}
   def __init__(self, name, description):
       self.name = name
       self.description = description
       self.doors = {}
       self.content = []

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


def create_rooms():
   room1 = Room("Столовая", ROOM_DESCRIPTION["Столовая"])
   room2 = Room("Холл", ROOM_DESCRIPTION["Холл"])
   room3 = Room("Спальня", ROOM_DESCRIPTION["Спальня"])
   room4 = Room("Кухня", ROOM_DESCRIPTION["Кухня"])
   room5 = Room("Коридор", ROOM_DESCRIPTION["Коридор"])

   room1.bind("west", room4)
   room1.bind("north",room2)
   room5.bind("east",room3)
   room5.bind("west",room2)
   room5.bind("north", room1)
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

   def find_subjects(room):
       if len(room.content)==0:
           print("В этой комнате нет ничего интересного")
       else:
           list_content=""
           for sub in room.content:
               list_content= list_content + sub + ", "
               print("В этой комнате вы находите:", list_content)
       return [False, room]


   if command == "look around":
       return look_around(room)

   if command[:3]=="go ":
       return go(command[3:],room)

   if command == "find_subjects":
       return find_subjects(room)

   print("Вы ввели неверную команду. Введите еще раз.")
   return [False, room]

