#TODO: Make items in marketplace vary by price 
#TODO: Make altar usable in house when created
#TODO: Add enemy wild animal encounters in forest
#TODO: Add positive wild animal encounters in forest -- [ADDED CAT]
#TODO: Add story and conflict
#TODO: Add consequences for not completing villager quests
#TODO: Add place in village to check suspicion
#TODO: Add Cat Toy item


if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    os.chdir(sys._MEIPASS)

    
import sys
import random
import os
import traceback
import pickle
import pygame
from collections import Counter

class color: 
   PURPLE = '\033[95m'  
   CYAN = '\033[96m'    
   DARKCYAN = '\033[36m' 
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   PINK = '\033[35m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class useful_stuff:
   def counterSubset(list1, list2):
        c1, c2 = Counter(list1), Counter(list2)
        for k, n in c1.items():
            if n > c2[k]:
                return False
        return True

class cat:
   def __init__(self,name,hunger,affection):
      self.debug_testing = False
      self.name = ""
      self.hunger = 0 #min 0 (not hungry), max 20 (very hungry)
      self.affection = 20 #min 0 max 10
      self.hastoy = False
      self.toywear = 10 #10 good, 0 broken
   def disp_stats(self):
      print("Hunger: " + str(self.hunger) + "/20" + " " + "Affection: " + str(self.affection) + "/20" + " Has toy: " + str(self.hastoy))
   def reset(self):
      self.name = ""
      self.hunger = 0
      self.affection = 20

class Player:
    def __init__(self,health,storage,basket,basketsize,disks,day,time,reputation,townsfolk_helped,cansleep,hascat):
       self.health = 20
       self.max_health = 20
       self.storage = []
       self.basket = []
       self.basketsize = 8
       self.disks = 10
       self.day = 1
       self.time = 420 #420 mins = 7 AM, 1320 mins = 12 AM
       self.reputation = 5 #min 0 max 10
       self.danger = 0
       self.townsfolk_helped = 0
       self.cansleep = False
       self.passed_out = False
       self.hascat = False
    def disp_stats(self):
       hhmm = '{:02d}:{:02d}'.format(*divmod(player.time, 60))
       print("Health: " + str(player.health) + "/20"," Disks: " + str(player.disks)," Day: " + str(player.day)," Time: " + str(hhmm))
    def disp_storage(self):
       raritycolor = ""
       for letter in Counter(player.storage):
          if letter in items.uncommon_tree_items or letter in items.uncommon_path_items or letter in items.uncommon_creek_items:
             raritycolor = color.GREEN
          elif letter in items.rare_tree_items or letter in items.rare_path_items or letter in items.rare_creek_items:
             raritycolor = color.YELLOW
          elif letter in items.common_tree_items or letter in items.common_path_items or letter in items.common_creek_items:
             raritycolor = ""
          else:
             raritycolor = color.DARKCYAN
          print(raritycolor + letter+color.END + ":",Counter(player.storage)[letter])
       #print(type(Counter(player.storage)))
       #print(*player.storage, sep = "\n")
    def disp_basket(self):
       for letter in Counter(player.basket):
          raritycolor = ""
          if letter in items.uncommon_tree_items or letter in items.uncommon_path_items or letter in items.uncommon_creek_items:
             raritycolor = color.GREEN
          elif letter in items.rare_tree_items or letter in items.rare_path_items or letter in items.rare_creek_items:
             raritycolor = color.YELLOW
          elif letter in items.common_tree_items or letter in items.common_path_items or letter in items.common_creek_items:
             raritycolor = ""
          else:
             raritycolor = color.DARKCYAN
          print(raritycolor + letter+ color.END + ":",Counter(player.basket)[letter])
    def inc_time(self,mins):
       if player.hascat == True:
          rand_deplete_stats = random.randint(0,75)
          if rand_deplete_stats <= 25:
             pass
          elif rand_deplete_stats > 25 and rand_deplete_stats <= 60:
             if C.hunger < 20:
                C.hunger = C.hunger + 1
             if C.affection > 0 and C.hastoy == False:
                C.affection = C.affection - 1
          if C.hunger >= 15 or C.affection <= 3:
             print(color.RED + "MEOWWWW..." + color.END)
             print(color.RED + "Oh no! Did you forget to take care of your cat?" + color.END)
             print(color.RED + "You better hurry up and do that before they run away!" + color.END)
          if C.hunger >= 20 and C.affection <= 0:
             print(color.RED + "Meow..." + color.END)
             print(color.RED + "Oh no.. you must've forgot to take care of your cat." + color.END)
             print(color.RED + "Looks like they've gone off looking for a better home." + color.END)
             player.hascat = False
             C.reset()
       player.time = player.time + mins
       if player.time >= 840:
          player.cansleep = True
       if player.time == 1140:
          print(color.RED + "You are running low on time." + color.END)
          print(color.RED + "You have 3 hours to get to bed before your health suffers." + color.END)
       if player.time == 1200:
         print(color.RED + "You are running low on time." + color.END)
         print(color.RED + "You have 2 hours to get to bed before your health suffers." + color.END)
       if player.time == 1260:
          print(color.RED + "You are running low on time." + color.END)
          print(color.RED + "You have 1 hour to get to bed before your health suffers." + color.END)
       if player.time >= 1320:
          print(color.RED + "You didn't go to bed, did you?" + color.END)
          print(color.RED + "You are reminded of your own morrtality as you collapse on the ground." + color.END)
          print(color.RED + "The forest spirits may take care of you this time, but there will be consequences tomorrow." + color.END)
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          player.passed_out = True
          next_day()
    def item_info(self):
       rarity = ""
       itemtype = ""
       print("Type the name of the item you would like to know more about.")
       print("Press X to go back.")
       itemname = str(input(">>> ")).lower()
       if itemname not in player.storage and itemname not in player.basket and itemname != "x":
          print("Not a valid item.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          player.item_info()
       elif itemname != "x":
          if itemname in items.common_tree_items or itemname in items.common_path_items or itemname in items.common_creek_items:
             rarity = "Common"
          elif itemname in items.uncommon_tree_items or itemname in items.uncommon_path_items or itemname in items.uncommon_creek_items:
             rarity = "Uncommon"
          elif itemname in items.rare_tree_items or itemname in items.rare_path_items or itemname in items.rare_creek_items:
             rarity = "Rare"
          else:
             rarity = "Unknown"
          if itemname in items.askables:
             itemtype = "Creatable Item"
          elif itemname in items.buyables:
             itemtype = "Buyable Item"
          elif itemname in items.cat_items:
             itemtype = "Cat Food Item"
          else:
             itemtype = "Foraged Item"
          print("Rarity: " + rarity + " ----"+ " Type: " + itemtype)
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          player.item_info()
       else:
          player.arrange_storage()
    def arrange_storage(self):
       os.system("cls")
       choice = False
       moveditem = ""
       if not player.storage:
          print("You have no items in storage!")
       if not player.basket:
          print("You have no items in your basket!")
       if not player.storage and not player.basket:
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()
       while choice == False:
          print(color.PURPLE + "Arrange Storage" + color.END)
          print(color.PURPLE + "[1]" + color.END + "Empty Basket")
          print(color.PURPLE + "[2]" + color.END + "Fill Basket")
          print(color.PURPLE + "[3]" + color.END + "Toss Storage Item")
          print(color.PURPLE + "[4]" + color.END + "Toss Basket Item")
          print(color.PURPLE + "[5]" + color.END + "View Storage")
          print(color.PURPLE + "[6]" + color.END + "View Basket")
          print(color.PURPLE + "[7]" + color.END + "Go Back")
          option = input(color.PURPLE + ">>> " + color.END).lower()
          if option == "1" or option == "empty basket":
             print("Here are the items in your basket.")
             print("You have " + str(player.basketsize - len(player.basket)) + " spaces in your basket.")
             player.disp_basket()
             print("Type the name of the item you wish to move to storage.")
             print("Or, press A to move all items to storage.")
             moveditem = str(input(">>> ")).lower()
             if moveditem not in player.basket and moveditem != "a":
                print("Not a valid item.")
                pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
             elif moveditem != "a":
                player.basket.remove(moveditem)
                player.storage.append(moveditem)
             else:
                print("Emptied basket.")
                pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                player.storage.extend(player.basket)
                player.basket.clear()
             player.arrange_storage()
          elif option == "2" or option == "fill basket":
             print("You have " + str(player.basketsize - len(player.basket)) + " spaces in your basket.")
             if len(player.basket) >= player.basketsize:
                print("You cannot fill your basket without emptying it first!")
             else:
                player.disp_storage()
                print("Type the name of the item you wish to move to the basket.")
                moveditem = str(input(">>> ")).lower()
                if moveditem not in player.storage:
                   print("Not a valid item.")
                   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                else:
                   if player.storage.count(moveditem) > 1:
                      print("How many do you want to move?")
                      numitems = int(input(">>> "))
                      if numitems > player.storage.count(moveditem) or numitems < 1:
                         print("You can't do that.")
                      elif numitems <= player.storage.count(moveditem):
                         for i in range(numitems):
                            player.storage.remove(moveditem)
                            player.basket.append(moveditem)
                      else:
                         print("You can't do that.")
                   else:
                      player.storage.remove(moveditem)
                      player.basket.append(moveditem)
                player.arrange_storage()
          elif option == "3" or option == "toss storage item":
             player.disp_storage()
             print("Type the name of the item you wish to toss.")
             moveditem = str(input(">>> ")).lower()
             if moveditem not in player.storage:
                print("Not a valid item.")
                pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                player.arrange_storage()
             else:
                if player.storage.count(moveditem) > 1:
                      print("How many do you want to toss?")
                      numitems = int(input(">>> "))
                      if numitems > player.storage.count(moveditem) or numitems < 1:
                         print("You can't do that.")
                      elif numitems <= player.storage.count(moveditem):
                         for i in range(numitems):
                            player.storage.remove(moveditem)
                      else:
                         print("You can't do that.")
                else:
                   player.storage.remove(moveditem)
                player.arrange_storage()
          elif option == "4" or option == "toss basket item":
             player.disp_basket()
             print("Type the name of the item you wish to toss.")
             moveditem = str(input(">>> ")).lower()
             if moveditem not in player.basket:
                print("Not a valid item.")
                pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                player.arrange_storage()
             else:
                if player.storage.count(moveditem) > 1:
                      print("How many do you want to move?")
                      numitems = int(input(">>> "))
                      if numitems > player.storage.count(moveditem) or numitems < 1:
                         print("You can't do that.")
                      elif numitems <= player.storage.count(moveditem):
                         for i in range(numitems):
                            player.basket.remove(moveditem)
                      else:
                         print("You can't do that.")
                else:
                  player.basket.remove(moveditem)
                player.arrange_storage()
          elif option == "5" or option == "view storage":
             player.disp_storage()
             player.item_info()
             pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
             player.arrange_storage()
          elif option == "6" or option == "view basket":
             player.disp_basket()
             player.item_info()
             pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
             player.arrange_storage()
          elif option == "7" or option == "go back":
             choice = True
             house()
          else:
             print("Not a valid answer.")
             pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
             player.arrange_storage()
             
      
class items:
   all_creatables = ["love potion","curse talisman","money charm",
                      "health potion","sweet tea","deadly poison",
                      "vegetable soup","bread loaf","sweet perfume",
                      "candle","strong incense","luck charm",
                      "protection amulet","berry juice","berry pie",
                      "bitter tea","mild poison","mushroom soup","wreath","altar",
                     "large basket","cat toy"]
   
   askables = ["love potion","curse talisman","money charm",
                      "health potion","sweet tea","deadly poison",
                      "vegetable soup","bread loaf","sweet perfume",
                      "candle","strong incense","luck charm",
                      "protection amulet","berry juice","berry pie",
                      "bitter tea","mild poison","mushroom soup","wreath"]
   
   offerables = ["bread loaf","strong incense","berry pie","berry juice",
                 "sweet perfume","vegetable soup","mushroom soup"]

   cat_items = ["fish","cat food","cat toy"]


   common_tree_items = ["stick","pine needles","oak bark","acorns","cedar resin"]
   uncommon_tree_items = ["honey","beeswax","morel","laetiporus"]
   rare_tree_items = ["fly agaric"]


   common_path_items = ["clovers","dandelion","rosemary","green sage","lemonbalm",
                        "lavender","blackberries","raspberries"]
   uncommon_path_items = ["rose petals","hemlock","chamomile","ginger","wild carrot",
                          "wild onion","wild garlic"]
   rare_path_items = ["belladonna berries"]
   

   common_creek_items = ["stick","pebbles","morel","oak bark","clovers"]
   uncommon_creek_items = ["violets","snake shed","thorny branch"]
   rare_creek_items = ["animal bone"]

   buyables = ["flour","sugar","string","potato","olive oil",
                "dragon's blood resin","salt","cloth"]

   craftlist = [["rose petals","rose petals","lemonbalm","violets","berry juice"], #love potion
    ["thorny branch","pine needles","hemlock","snake shed"],   #curse talisman
    ["luck charm","oak bark"],  #money charm
    ["sweet tea","lemonbalm","ginger"], #health potion
    ["sugar","chamomile","lemonbalm","honey"], #sweet tea
    ["hemlock","hemlock","hemlock","belladonna berries"], #deadly poison
    ["wild carrot","wild onion","potato","potato",     #vegetable soup
                      "wild carrot","wild garlic"],
    ["flour","flour","rosemary"],  #bread loaf
    ["rose petals","rose petals","rose petals","olive oil", #sweet perfume
                     "lavender","lavender","violets"],
    ["beeswax","beeswax","beeswax","string"], #candle
    ["cedar resin","dragon's blood resin",    #strong incense
                      "dragon's blood resin"],
    ["acorns","acorns","clovers","clovers","dandelion","cloth"], #luck charm
    ["rosemary","rosemary","cloth","string","green sage", #protection amulet
                         "salt"],
    ["blackberries","blackberries","raspberries","raspberries"], #berry juice
    ["flour","berry juice","berry juice","sugar","salt"], #berry pie
    ["pine needles","ginger","pine needles"],  #bitter tea
    ["fly agaric","belladonna berries","fly agaric"], #mild poison
    ["morel","morel","laetiporus","laetiporus","salt"],#mushroom soup
    ["stick","stick","stick","violets","violets"], #wreath
    ["animal bone","animal bone","snake shed","stick","stick","pebbles","candle"], #altar
    ["stick","stick","stick","stick","stick","stick","string","cloth","oak bark"],#large basket
    ["stick","string","string","pebbles"] #cat toy
      
    ]

    
def house():
    os.system("cls")
    choice = False
    yn = ""
    while choice == False:
       print("""
                (                                 
        ________[]_                             
       /^=^-^-^=^-^\                   
      /^-^-^-^-^-^-^\               
     /__^_^_^_^^_^_^_\              
      |  .==.       |     
    ^^|  |LI|  [}{] |^^^^
    &&|__|__|_______|&&
                              """)

       print(30 * "-" , "Your House" , 30 * "-")
       print(color.PURPLE + "[1]" + color.END + "Go Outside")
       print(color.PURPLE + "[2]" + color.END + "Sleep")
       print(color.PURPLE + "[3]" + color.END + "Info")
       print(color.PURPLE + "[4]" + color.END + "Storage")
       print(color.PURPLE + "[5]" + color.END + "Create")
       print(color.PURPLE + "[6]" + color.END + "Save Game")
       if player.hascat == True:
          print(color.PURPLE + "[7]" + color.END + "Cat")
       print(72 * "-")
       option = input(color.PURPLE + ">>> " + color.END).lower()
       if option == "1" or option == "go outside":
          choice = True
          forest()
       elif option == "2" or option == "sleep":
          if player.cansleep == True:
             print("Do you really want to sleep?")
             print(color.CYAN + "[1]" + color.END + "Yes")
             print(color.CYAN + "[2]" + color.END + "No")
             yn = str(input(">>> ")).lower()
             if yn == "1" or yn == "yes":
                 print("You lie down...")
                 while player.health < 20:
                    player.health = player.health + 1
                 choice = True
                 next_day()
          else:
             print("Wait, what? It's not time to sleep!")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()
          if yn == "2" or yn == "no":
             choice = False
          else:
             print("Not a valid answer")
             choice = False
       elif option == "3" or option == "info":
          player.disp_stats()
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()
       elif option == "4" or option == "storage":
          player.arrange_storage()
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()
       elif option == "5" or option == "create":
          os.system('cls')
          create()
       elif (option == "7" or option == "cat") and player.hascat == True:
          kitty()
       elif option == "6" or option == "save game":
          save_game()
       else:
          print("That is not an acceptable answer.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()


def kitty():
   os.system("cls")
   choice = False
   while choice == False:
      print(r"""
                      |\_/|   
                      \` ..\
                 __,.-" =__Y=
               ."        )
         _    /   ,    \/\_
        ((____|    )_-\ \_-`
         `-----'`-----` `--`""")
      print(30 * "-" , cat.name , 30 * "-")
      print(color.PURPLE + "[1]" + color.END + "Pet")
      print(color.PURPLE + "[2]" + color.END + "Feed")
      print(color.PURPLE + "[3]" + color.END + "Stats")
      print(color.PURPLE + "[4]" + color.END + "Rename")
      print(color.PURPLE + "[5]" + color.END + "Go Back")
      if "cat toy" in player.storage:
          print(color.PURPLE + "[6]" + color.END + "Play")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "pet":
         print("You pet " + cat.name + "!")
         print(color.PINK + "Purrr..." + color.END)
         if C.affection < 20:
            C.affection = C.affection + 2
            print(cat.name + " is more affectionate towards you!")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            kitty()
      elif option == "2" or option == "feed":
         if not any(item in items.cat_items for item in player.storage):
            print("You have no food to give!")
            print("Food must be in storage before feeding.")
         else:
            print("Here are your options.")
            for thing in Counter(player.storage):
               if thing in items.cat_items:
                  print(thing+":",Counter(player.storage)[thing])
            print("Enter the name of the type of food.")
            foodname = str(input(">>> ")).lower()
            player.storage.remove(foodname)
            C.hunger = C.hunger - 4
            print("Fed " + cat.name + "!")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            kitty()
      elif option == "3" or option == "stats":
         C.disp_stats()
         print("")
         print("Remember, you must take care of your cat!")
         print("You wouldn't want " + cat.name + " to run away!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         kitty()
      elif option == "4" or option == "rename":
         print("New name?")
         cat.name = str(input(">>> "))
         print("Ok!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         kitty()
      elif option == "5" or option == "go back":
         choice = True
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         house()
      elif option == "6" or option == "play":
          player.storage.remove("cat toy")
          print("You gave " + cat.name + " a toy!")
          C.hastoy = True
          print(cat.name + " won't require affection as much")
          print("until the toy wears out.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          kitty()   
      else:
         print("Not an acceptable answer.")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         kitty()

     

def create():
   os.system("cls")
   creatable_ints = []
   creatables = []
   os.system("cls")
   itemname = ""
   for c,i in enumerate(items.craftlist):
      can_create = useful_stuff.counterSubset(items.craftlist[c],player.storage)
      if can_create == True:
         creatable_ints.append(c)
   for j in creatable_ints:
      creatables.append(items.all_creatables[j])
   if not creatables:
      print("You cannot create anything with what you have.")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      house()
   print("Here are the items you can create:")
   print("")
   for letter in Counter(creatables):
          print(letter+":",Counter(creatables)[letter])
   print("")
   print("Enter the name of the item to create it, else 'x' to quit.")
   while itemname not in creatables:
      itemname = str(input(">>> ")).lower()
      if itemname == "x":
         house()
      if itemname not in creatables:
         print("Not a valid item")
   for k,l in zip(creatables,creatable_ints):
      if k == itemname:
         materials = items.craftlist[l]
   print("Materials: ")
   print(*materials, sep = "\n")
   print("Create?")
   print("[1] Yes     [2] No")
   choice = str(input(">>> ")).lower()
   valid = False
   while valid == False:
      if choice == "1" or choice == "yes":
         valid = True
         #remove materials from storage, put the created thing into storage
         for m,n in enumerate(items.all_creatables):
            if n == itemname:
               list_to_remove_from = items.craftlist[m]
         for p in list_to_remove_from:
            player.storage.remove(p)
         player.storage.append(itemname)
         if itemname == "large basket":
            player.basketsize = 16
            items.all_creatables.remove(itemname)
            player.storage.remove(itemname)
            print(color.PURPLE + "Upgraded Basket!" + color.END)
      elif choice == "2" or choice == "no":
         valid = True
         create()
      else:
         print("Not a valid answer")
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   house()  

def forest():
   os.system('cls')
   choice = False
   while choice == False:
       print(color.GREEN + r"""
                    ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
 \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_ """ + color.END)
       print(30 * "-" , "Forest" , 30 * "-")
       print(color.PURPLE + "[1]" + color.END + "Look Around")
       print(color.PURPLE + "[2]" + color.END + "Go to Town")
       print(color.PURPLE + "[3]" + color.END + "Foraging Basket")
       print(color.PURPLE + "[4]" + color.END + "Go Home")
       print(color.PURPLE + "[5]" + color.END + "Info")
       print(72 * "-")
       option = input(color.PURPLE + ">>> " + color.END).lower()
       if option == "1" or option == "look around":
          choice = True
          look_forest()
       elif option == "2" or option == "go to town":
          choice = True
          player.inc_time(30)
          town()
       elif option == "3" or option == "foraging basket":
          print("Here are the items in your basket.")
          print("You have " + str(player.basketsize - len(player.basket)) + " spaces in your basket.")
          player.disp_basket()
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          forest()
       elif option == "4" or option == "go home":
          choice = True
          player.inc_time(30)
          house()
       elif option == "5" or option == "info":
          player.disp_stats()
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          forest()
       else:
          print("That is not an acceptable answer.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          forest()

def look_forest():
   os.system("cls")
   choice = False
   while choice == False:
      print("Where do you want to look?")
      print(color.PURPLE + "Look near..." + color.END)
      print(color.PURPLE + "[1]" + color.END + "Fallen Trees")
      print(color.PURPLE + "[2]" + color.END + "Path")
      print(color.PURPLE + "[3]" + color.END + "Creek")
      print(color.PURPLE + "[4]" + color.END + "Go Back")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "fallen trees":
         choice = True
         forage(1)
      elif option == "2" or option == "path":
         choice = True
         forage(2)
      elif option == "3" or option == "creek":
         forage(3)
      elif option == "4" or option == "go back":
         choice = True
         forest()
      else:
         print("That is not an acceptable answer.")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)

def forage(place):
   os.system("cls")
   choice = False
   while choice == False:
      print(color.PURPLE + "......" + color.END)
      print(color.PURPLE + "[1]" + color.END + "Forage")
      print(color.PURPLE + "[2]" + color.END + "Go Back")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "forage":
         player.inc_time(30)
         print("Looking...")
         animal_chance_encounter(place)
         if place == 1: #fallen trees
            encounter = random.randint(0,100)
            if encounter <= 60:
               item_got = random.choice(items.common_tree_items)
            elif encounter > 60 and encounter < 90:
               item_got = random.choice(items.uncommon_tree_items)
            elif encounter >= 90:
               item_got = random.choice(items.rare_tree_items)
         elif place == 2: #path
            encounter = random.randint(0,100)
            if encounter <= 60:
               item_got = random.choice(items.common_path_items)
            elif encounter > 60 and encounter < 90:
               item_got = random.choice(items.uncommon_path_items)
            elif encounter >= 90:
               item_got = random.choice(items.rare_path_items)
         elif place == 3: #creek
            encounter = random.randint(0,100)
            if encounter <= 60:
               item_got = random.choice(items.common_creek_items)
            elif encounter > 60 and encounter < 90:
               item_got = random.choice(items.uncommon_creek_items)
            elif encounter >= 90:
               item_got = random.choice(items.rare_creek_items)
         print(color.BOLD + "You got: " + str(item_got) + "!" + color.END)
         if len(player.basket) < player.basketsize:
            player.basket.append(item_got)
            print("You have " + str(player.basketsize - len(player.basket)) + " spaces left in your basket.")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            forage(place)
         else:
            print("...There's no room in your basket! You discard the item.")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            forage(place)
      if option == "2" or option == "go back":
         choice = True
         look_forest()

def animal_chance_encounter(place):
   yn = ""
   otherchoice = False
   choice = False
   rand_animal_enc = random.randint(0,300)
   if cat.debug_testing == True:  #CAT DEBUG TESTING
      rand_animal_enc = 3         #FORCES CAT ENCOUNTER
   if rand_animal_enc <= 3 and player.hascat == False:
      flee_chance = random.randint(0,100)
      print("....")
      print(color.BOLD + "Oh look! It's a cat!" + color.END)
      while choice == False:
         print(r"""
                      |\_/|          
                      \` ..\
                 __,.-" =__Y=
               ."        )
         _    /   ,    \/\_
        ((____|    )_-\ \_-`
         `-----'`-----` `--`""")
         print(color.PURPLE + "[1]" + color.END + "Pet")
         print(color.PURPLE + "[2]" + color.END + "Go Back")
         option = input(color.PURPLE + ">>> " + color.END).lower()
         if option == "1" or option == "pet":
            choice = True
            print("You pet the cat!")
            if flee_chance <= 20:
               print("...It got scared and ran away!")
               pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
               forage(place)
            else:
               print(color.PINK + "..Meow?" + color.END)
               print("It looks like it wants to come with you!")
               print(color.PINK + "Purrr.." + color.END)
               while otherchoice == False:
                  print("Accept the kitty?")
                  print(color.PURPLE + "[1]" + color.END + "Yes")
                  print(color.PURPLE + "[2]" + color.END + "No")
                  yn = input(color.PURPLE + ">>> " + color.END).lower()
                  if yn == "1" or yn == "yes":
                     otherchoice = True
                     print("The kitty will follow you home!")
                     player.hascat = True
                     print("Name the kitty:")
                     cat.name = str(input(">>> "))
                     print("Ok!")
                     print("You can now find FISH at the creek!")
                     print("You can now buy CAT FOOD at the marketplace!")
                     items.common_creek_items.append("fish")
                     items.common_creek_items.append("fish")
                     items.buyables.append("cat food")
                     pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                     forage(place)
                  elif yn == "2" or yn == "no":
                     otherchoice = True
                     print("The kitty accepts your choice and wanders away.")
                     pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                     forage(place)
                  else:
                     print("Not a valid answer.")
         elif option == "2" or option == "go back":
            choice = True
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            forage(place)
         else:
            print("Not a valid answer.")
   else:
      return

def town():
   os.system("cls")
   choice = False
   while choice == False:
      print(r"""~         ~~          __
          _T      .,,.    ~--~ ^^
    ^^   // \                    ~
         ][O]    ^^      ,-~ ~
      /''-I_I         _II____
   __/_  /   \ ______/ ''   /'\_,__
     | II--'''' \,--:--..,_/,.-{ },
   ; '/__\,.--';|   |[] .-.| O{ _ }
   :' |  | []  -|   ''--:.;[,.'\,/
   '  |[]|,.--'' '',   ''-,.    |
     ..    ..-''    ;       ''. '""")
      print("What do?")
      print(color.PURPLE + "[1]" + color.END + "Marketplace")
      print(color.PURPLE + "[2]" + color.END + "Go Back")
      print(color.PURPLE + "[3]" + color.END + "Info")
      print(color.PURPLE + "[4]" + color.END + "Run Errand")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "marketplace":
         choice = True
         player.inc_time(30)
         marketplace()
      elif option == "2" or option == "go back":
         choice = True
         forest()
      elif option == "3" or option == "info":
         player.disp_stats()
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         town()
      elif option == "4" or option == "run errand":
         if encounter == False:
            print("You have no errands to run today.")
         else:
            choice = True
            errand()
      else:
         print("That is not an acceptable answer.")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)

def marketplace():
   os.system("cls")
   choice = False
   common_price = 2
   uncommon_price = 5
   rare_price = 10
   numitems = 1
   while choice == False:
      print(r"""
    _______
   <_4 sale_>       
      ^|^             
       | """)
      print("Welcome to the Marketplace!")
      print("Here you can Sell the items you brought with you!")
      print(color.PURPLE + "[1]" + color.END + "Sell")
      print(color.PURPLE + "[2]" + color.END + "Buy")
      print(color.PURPLE + "[3]" + color.END + "Go Back")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "sell":
         print("What would you like to sell?")
         player.disp_basket()
         print("Type the name of the item.")
         sellitem = str(input(">>> ")).lower()
         if sellitem not in player.basket:
            print("Not a valid item.")
         else:
            if player.basket.count(sellitem) > 1:
                print("How many do you want to sell?")
                numitems = int(input(">>> "))
                if numitems > player.basket.count(sellitem) or numitems < 1:
                   print("You can't do that.")
                elif numitems <= player.basket.count(sellitem):
                   for i in range(numitems):
                      player.basket.remove(sellitem)
                else:
                   print("You can't do that.")
            else:
                player.basket.remove(sellitem)
            if sellitem in items.common_tree_items or sellitem in items.common_path_items or sellitem in items.common_creek_items:
               print("I can give you " + str(common_price * numitems) + " Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + (common_price * numitems)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.uncommon_tree_items or sellitem in items.uncommon_path_items or sellitem in items.uncommon_creek_items:
               print("I can give you " + str(common_price * numitems)+" Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + (common_price * numitems)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.rare_tree_items or sellitem in items.rare_path_items or sellitem in items.rare_creek_items:
               print("I can give you " + str(common_price * numitems)+" Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + (common_price * numitems)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.all_creatables:
               randprice = random.randint(1,10)
               print("A created item? Prices may vary day to day.")
               print("I can give you " + str(randprice) + " Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + randprice
                  player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
         marketplace()
      elif option == "2" or option == "buy":
         print("Great! Take a look at what we have.")
         print(*items.buyables, sep = "\n")
         print("")
         print("Prices vary, today everything is " + str(randbuyprice) + " Disks.")
         print("Type the name of the item you want to buy, else X to go back.")
         buyitem = str(input(">>> ")).lower()
         if buyitem not in items.buyables and buyitem != "x":
            print("Not a valid item.")
         elif buyitem == "x":
            marketplace()
         else:
            if len(player.basket) == player.basketsize:
               print("You have no room in your basket for that!")
               pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
               marketplace()
            else:
               print("Have a nice day!")
               player.basket.append(buyitem)
               player.disks = player.disks - randbuyprice
               pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
               marketplace()
      elif option == "3" or option == "go back":
         choice = True
         town()
      else:
         print("That is not an acceptable answer.")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)

def next_day():
   os.system("cls")
   print(color.YELLOW + r"""   '
          .      '      .
    .      .     :     .      .
     '.        ______       .'
       '  _.-"`      `"-._ '
        .'                '.
 `'--. /                    \ .--'`
      /                      \
     ;                        ;
- -- |                        | -- -
     |                        |
     ;            ,_          ;
 .-'  \       ;._.}{__       /  '-.
    _.-""- .' # '. `  `.-"{}<._
          / #  #  \     \  x   `"
     ----/         \_.-'|--X----
     -=_ |         |    |- X.  =_
    - __ |_________|_.-'|_X-X##
        `'-._|_|;:;_.-'` '::.  `"-
     .:;.      .:.   ::.     '::.""" + color.END)

   
   player.day = player.day + 1
   randbuyprice = random.randint(5,20)
   player.cansleep = False
   if player.hascat == True:
      cat.hunger = cat.hunger + 3
      if C.hastoy == True:
          C.toywear = C.toywear - 1
          if C.toywear <= 0:
              C.hastoy = False
   if player.day == 10:
      end_game()
   player.time = 420
   if player.passed_out == True:
      player.health = player.health - 5
      if player.health <= 0:
          death = "Exhaustion"
          game_over(death)
   player.passed_out = False
   print("It's the next day.")
   print(color.BOLD + "Time to wake up!" + color.END)
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   townsfolk_rand_encounter()

def townsfolk_rand_encounter():
   global offered_disks
   global encounter
   global randitem
   rand_enc = random.randint(0,100)
   randitem = random.choice(items.askables)
   offered_disks = random.randint(2,10)
   for c,i in enumerate(items.askables):
      if i == randitem:
         materials = items.craftlist[c]
   if rand_enc <= 40:
      encounter = True
      os.system("cls")
      print(color.BOLD + "*KNOCK KNOCK*" + color.END)
      print("...")
      print("You hear knocking at your door!")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      print("You open the door..")
      print(color.CYAN + "I'm from the town! I've come to you because I really need help with something!" + color.END)
      print(color.CYAN + "Can you please make me a " + str(randitem) + "?" + color.END)
      print(color.CYAN + "It's important..." + color.END)
      print(color.CYAN + "To make it, you will need:" + color.END)
      for letter in Counter(materials):
          print(letter+":",Counter(materials)[letter])
      print("")
      print(color.CYAN + "And I'll need it by the end of the day." + color.END)
      print(color.CYAN + "I'll be in the town if you need me.." + color.END)
      print(color.CYAN + "But if you really can't make it, then that's fine, I guess." + color.END)
      print(color.CYAN + "I'll give you " + str(offered_disks) + " Disks " + " for it though!" + color.END)
      print(color.CYAN + "Anyways, bye!" + color.END)
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      house()
   else:
      encounter = False
      house()

def errand():
   player.inc_time(30)
   os.system("cls")
   valid = False
   print(color.CYAN + "Oh, hello! It's me from this morning!" + color.END)
   print(color.CYAN + "Do you want to give me the " + str(randitem) + " I requested?" + color.END)
   while valid == False:
      print(color.PURPLE + "[1]" + color.END + "Yes")
      print(color.PURPLE + "[2]" + color.END + "No")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "yes":
         if randitem not in player.basket:
            print(color.CYAN + "You don't even have the item!" + color.END)
            print(color.CYAN + "Come back later if you can..." + color.END)
         else:
            print(color.CYAN + "Oh! My " + str(randitem) + "!" + color.END)
            player.basket.remove(randitem)
            print(color.CYAN + "Thanks! Here's your " + str(offered_disks) + " Disks!" + color.END)
            player.disks = player.disks = offered_disks
            encounter = False
            valid = True
            player.townsfolk_helped = player.townsfolk_helped + 1
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
      elif option == "2" or option == "no":
         print(color.CYAN + "No?.. Well, okay then." + color.END)
         valid = True
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         town()
      else:
         print("Not a valid answer.")

def game_over(death):
    os.system("cls")
    print(color.BOLD + "You died...." + color.END)
    print(color.BOLD + "Of.. " + death + color.END)
    print("Maybe the forest life isn't for you!")
    print("You can always try again, though.")
    print(color.BOLD + "Here are your in-game stats:" + color.END)
    print("Disks: " + str(player.disks))
    print("Townsfolk helped: " + str(player.townsfolk_helped))
    print(color.BOLD + "Thanks for playing!" + color.END)
    print(color.PURPLE + " Game Ended" + color.END)
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)


def end_game():
   os.system("cls")
   print(color.BOLD + "That's the end of the game so far!" + color.END)
   print(color.BOLD + "I hope you enjoyed it!" + color.END)
   print(color.BOLD + "Here are your in-game stats:" + color.END)
   print("Disks: " + str(player.disks))
   print("Townsfolk helped: " + str(player.townsfolk_helped))
   print(color.BOLD + "Thanks for playing!" + color.END)
   print(color.PURPLE + " Game Ended" + color.END)
   try:
       sys.exit(0)
   except SystemExit:
       os._exit(0)

def save_game():
   os.system("cls")
   choice = False
   while choice == False:
      print("Would you like to save the game?")
      print(color.PURPLE + "[1]" + color.END + "Yes")
      print(color.PURPLE + "[2]" + color.END + "No")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "yes":
         choice = True
         Player_Save = player
         Cat_Save = C
         Data_Save = [Player_Save, Cat_Save]
         with open("Save File","wb") as file:
            pickle.dump(Data_Save,file)
         print("Game Saved!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         house()
      elif option == "2" or option == "no":
         print("Alright...")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         house()
      else:
         print("That is not an acceptable answer.")

def load_game():
   global player
   global C
   if os.path.isfile('Save File') == False:
      print("There is nothing to load. Exiting...")
      sys.exit()
   else:
       with open("Save File","rb") as file:
          savedata = pickle.load(file)
       player = savedata[0]
       C = savedata[1]
       pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
       house()

   
def opening_game():
   os.system("cls")
   global randbuyprice
   global player
   global C
   randbuyprice = random.randint(5,20)
   print(color.PURPLE + "Welcome to FORAGING SIMULATOR." + color.END)
   print(color.PURPLE + "A game where you live on the edge of a forest." + color.END)
   print(color.PURPLE + "Some call you wise, others call you a witch." + color.END)
   print(color.PURPLE + "But really, your passion is FORAGING items, as well as CRAFTING new ones." + color.END)
   print(color.PURPLE + "You can help people, or hurt them, the choice will be yours." + color.END)
   print(color.PURPLE + "But in the end, the fate of the small town is in your hands." + color.END)
   print("")
   print(color.PURPLE + "You have ONE MONTH." + color.END)
   print(color.PURPLE + "Good luck." + color.END)
   print("")
   print("")
   print("-------------------------------------------------------------------------------")
   print("Hello! This is actually a testing version of FORAGING SIMULATOR!")
   print("You'll have 10 days in this one, and you won't get to see the main storyline or conflicts.")
   print("Though it is hopefully still somewhat fun, the purpose of this release is to TEST gameplay!")
   print("Please report any bugs or obvious issues to...alexneely8@gmail.com")
   print("Unless you know me, the creator, already. In which case..you can just tell me.")
   print("If the game crashes for any reason, you can find the bug report in the exceptions.log file!")
   print("-------------------------------------------------------------------------------")
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   os.system("cls")
   print("-------------------------------------------------------------------------------")
   print("Hello again! Sorry to keep you waiting from the game!")
   print("You have an option here to BETA TEST the CAT feature.")
   print("While a CAT is a rare random encounter, enabling CAT TEST..")
   print("Will guarantee the encounter to be triggered, so you can report any bugs to me!")
   print("Turn CAT TEST on?")
   print("[1] Yes  [2] No")
   cattest = str(input(">>> ")).lower()
   if cattest == "1" or cattest == "yes":
      cat.debug_testing = True
   elif cattest == "2" or cattest == "no":
      cat.debug_testing = False
   else:
      print("That's not a valid answer, so CAT TEST will be off.")
      cat.debug_testing = False
   print("-----------------------------------------------------------------------------")
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   player = Player(20,[],[],8,10,1,420,5,0,False,False)
   C = cat("",2,5)
   house()

def start_game():
   os.system("cls")
   pygame.mixer.init()
   pygame.mixer.music.load('theme.wav')
   pygame.mixer.music.play(3)
   print(color.GREEN+r"""
   ________
                        .-'~~~-.
   FORAGING           .'o  oOOOo`.
                    :~~~-.oOo   o`.
   SIMULATOR         `. \ ~-.  oOOo.
   _________           `.; / ~.  OO:
                       .'  ;-- `.o.'
                      ,'  ; ~~--'~
                      ;  ;
_______\|/__________\\;_\\//___\|/________"""+color.END)
   print("")
   print("")
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   pygame.mixer.music.stop()
   choice = False
   while choice == False:
      os.system("cls")
      print(color.PURPLE + "Options:" + color.END)
      print(color.PURPLE + "[1] " + color.END + "New Game")
      print(color.PURPLE + "[2] " + color.END + "Load Game")
      print(color.PURPLE + "[3] " + color.END + "Exit")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "new game":
         choice = True
         opening_game()
      elif option == "2" or option == "load game":
         choice = True
         load_game()
      elif option == "3" or option == "exit":
         print(color.PURPLE + "Entering reality...." + color.END)
         choice = True
         sys.exit()
      else:
         print("That is not an acceptable answer.")

def main():
   start_game()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(color.PURPLE + " Game Ended" + color.END)
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    except:
        with open("exceptions.log", "a") as logfile:
            traceback.print_exc(file=logfile)
        raise

################################################################

         #TEST FUNCTIONS GO BELOW

################################################################

      
def test_crafting():
   player.storage.append("rose petals")
   player.storage.append("rose petals")
   player.storage.append("lemonbalm")
   player.storage.append("berry juice")
   player.storage.append("thorny branch")
   player.storage.append("pine needles")
   player.storage.append("hemlock")
   print("-----TESTING: Here is the start inventory-----")
   player.disp_storage()
   print("-----ENDTEST-----")
   create()
   print("-----TESTING: Here is the end inventory-----")
   player.disp_storage()
   print("-----ENDTEST-----")

def test_time():
   do_test = True
   print("------TESTING----")
   print("Time (in mins): " + str(player.time))
   print("Stats (including time in hours and mins):")
   player.disp_stats()
   print("Press X to advance time by 30 mins.")
   print("Press Z to advance time by an hour.")
   print("Press C to quit.")
   while do_test == True:
      testinput = str(input(">>> "))
      if testinput.lower() == "x":
         player.inc_time(30)
         print("Stats (including time in hours and mins):")
         player.disp_stats()
      elif testinput.lower() == "z":
         player.inc_time(60)
         print("Stats (including time in hours and mins):")
         player.disp_stats()
      elif testinput.lower() == "c":
         break
   print("-----ENDTEST----")





   
