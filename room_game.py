import building
def game_circle():
   new_room = True
   current_room = building.create_rooms()
   while True:
       if new_room:
           print("Вы находитесь в комнате", current_room.name)
           print(current_room.description)
           print("Введите команду")
       a = input(":")
       if a.strip() == "quit":
           break
       result = building.execute_command(a.strip(),current_room)
       new_room = result[0]
       current_room = result[1]




a = print("Введите команду, для выхода наберить quit")
game_circle()
