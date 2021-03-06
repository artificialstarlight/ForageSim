#TODO: Make more items usable
#TODO: make spirits give you tasks like the townsfolk do

    
import sys
import random
import os
import traceback
import pickle
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
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

class achievements:
    a_list = []
    def add_achievement(string):
        achievements.a_list.append(string)
        achievements.a_list = list(dict.fromkeys(achievements.a_list))
        
class cat:
   def __init__(self,name,hunger,affection,hastoy,toywear,hasitem):
      self.name = ""
      self.hunger = 0 #min 0 (not hungry), max 20 (very hungry)
      self.affection = 20 #min 0 max 20
      self.hastoy = False
      self.toywear = 10 #10 good, 0 broken
      self.hasitem = False
   def disp_stats(self):
      if self.hastoy == False:
          hastoystr = "No"
      else:
          hastoystr = "Yes"
      print("Hunger: " + str(self.hunger) + "/20" + " " + "Affection: " + str(self.affection) + "/20" + " Has toy: " + hastoystr)
   def reset(self):
      self.name = ""
      self.hunger = 0
      self.affection = 20

class Player:
    def __init__(self,health,storage,basket,basketsize,disks,day,time,reputation,spirit_reputation,townsfolk_helped,cansleep,hascat,hasaltar,immune,recipes,spirit_immune,encounter,housetype,numkilled):
       self.health = 20
       self.max_health = 20
       self.storage = []
       self.basket = []
       self.basketsize = 8
       self.disks = 10
       self.day = 1
       self.time = 420 #420 mins = 7 AM, 1320 mins = 12 AM
       self.reputation = 6 #min 0 max 10
       self.spirit_reputation = 6
       self.townsfolk_helped = 0
       self.cansleep = False
       self.passed_out = False
       self.hascat = False
       self.hasaltar = False
       self.immune = False
       self.recipes = []
       self.spirit_immune = False
       self.encounter = False
       self.housetype = "regular"
       self.numkilled = 0
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
    def disp_offerables(self):
        for letter in Counter(player.storage):
          raritycolor = ""
          if letter in items.uncommon_tree_items or letter in items.uncommon_path_items or letter in items.uncommon_creek_items:
             raritycolor = color.GREEN
          elif letter in items.rare_tree_items or letter in items.rare_path_items or letter in items.rare_creek_items:
             raritycolor = color.YELLOW
          elif letter in items.common_tree_items or letter in items.common_path_items or letter in items.common_creek_items:
             raritycolor = ""
          else:
             raritycolor = color.DARKCYAN
          if letter in items.offerables:
              print(raritycolor + letter+ color.END + ":",Counter(player.storage)[letter])

    def inc_time(self,mins):
       if player.hasaltar == True:
          if player.spirit_reputation <= 3:
             print(color.RED + "The forest spirits are angry..."+ color.END)
          if player.spirit_reputation <= 0:
             true_ending2()
       if player.reputation <=3:
           print(color.RED + "The townspeople are angry..."+ color.END)
       if player.reputation <= 0:
           os.system("cls")
           pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
           burn_stake()
       if player.hascat == True:
          rand_deplete_stats = random.randint(0,75)
          if rand_deplete_stats <= 25:
             pass
          elif rand_deplete_stats > 25 and rand_deplete_stats <= 40:
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
             achievements.add_achievement("Terrible pet owner: Didn't take care of your cat")
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
          achievements.add_achievement("Forgetful: Forgot to sleep and passed out")
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
          print(color.PURPLE + "[7]" + color.END + "Use Item")
          print(color.PURPLE + "[8]" + color.END + "Go Back")
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
          elif option == "8" or option == "go back":
             choice = True
             house()
          elif option == "7" or option == "use item":
              use_item()
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
                     "large basket","cat toy","mushroom house","flying ointment"]
   askables = ["love potion","curse talisman","money charm",
                      "health potion","sweet tea","deadly poison",
                      "vegetable soup","bread loaf","sweet perfume",
                      "candle","strong incense","luck charm",
                      "protection amulet","berry juice","berry pie",
                      "bitter tea","mild poison","mushroom soup","wreath"]
   offerables = ["bread loaf","strong incense","berry pie","berry juice",
                 "sweet perfume","vegetable soup","mushroom soup","raspberries","blackberries","rose petals",
                 "belladonna berries","animal bone"]
   useables = ["health potion","money charm", "mild poison","deadly poison"]

   cat_items = ["fish","cat food","cat toy"]


   common_tree_items = ["stick","pine needles","oak bark","acorns","cedar resin"]
   uncommon_tree_items = ["honey","beeswax","morel","laetiporus"]
   rare_tree_items = ["fly agaric"]


   common_path_items = ["clovers","dandelion","rosemary","green sage","lemonbalm",
                        "lavender","blackberries","raspberries"]
   uncommon_path_items = ["rose petals","hemlock","chamomile","wild carrot",
                          "wild onion","wild garlic"]
   rare_path_items = ["belladonna berries","ginger"]
   

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
    ["acorns","acorns","clovers","clovers","dandelion"], #luck charm
    ["rosemary","rosemary","string","green sage", #protection amulet
                         "salt"],
    ["blackberries","blackberries","raspberries","raspberries"], #berry juice
    ["flour","berry juice","berry juice","sugar","salt"], #berry pie
    ["pine needles","ginger","pine needles"],  #bitter tea
    ["fly agaric","belladonna berries","fly agaric"], #mild poison
    ["morel","morel","laetiporus","laetiporus","salt"],#mushroom soup
    ["stick","stick","stick","violets","violets"], #wreath
    ["animal bone","animal bone","snake shed","stick","stick","pebbles","candle"], #altar
    ["stick","stick","stick","stick","stick","stick","string","cloth","oak bark"],#large basket
    ["stick","string","string","pebbles"],#cat toy
    ["fly agaric","fly agaric","fly agaric","fly agaric","laetiporus","morel","oak bark","oak bark"], #mushroom house
    ["fly agaric","fly agaric","fly agaric","beeswax","pine needles","pine needles"] # flying ointment
      
    ]

    
def house():
    os.system("cls")
    choice = False
    yn = ""
    if player.hascat == True:
       rand_find_item = random.randint(0,100)
       if rand_find_item <= 10:
          C.hasitem = True
       else:
          C.hasitem = False
    while choice == False:
       if player.housetype == "regular":
          print(r"""
                   (                                 
           ________[]_                             
          /^=^-^-^=^-^\                   
         /^-^-^-^-^-^-^\               
        /__^_^_^_^^_^_^_\              
         |  .==.       |     
       ^^|  |LI|  [}{] |^^^^
       &&|__|__|_______|&&
                                 """)
       elif player.housetype == "mushroom":
          print(r"""
                       
        ('
        '|
        |'
       [::]
       [::]   _......_
       [::].-'      _.-`.
       [:.'    .-. '-._.-`.
       [/ /\   |  \        `-..
       / / |   `-.'      .-.   `-.
      /  `-'            (   `.    `.
     |           /\      `-._/      \
     '    .'\   /  `.           _.-'|
    /    /  /   \_.-'        _.':;:/
  .'     \_/             _.-':;_.-'
 /   .-.             _.-' \;.-'
/   (   \       _..-'     |
\    `._/  _..-'    .--.  |
 `-.....-'/  _ _  .'    '.|
          | |_|_| |      | \  (o)
     (o)  | |_|_| |      | | (\'/)
    (\'/)/  ''''' |     o|  \;:;
     :;  |        |      |  |/)
      ;: `-.._    /__..--'\.' ;:
          :;  `--' :;   :;
          """)

       print(30 * "-" , "Your House" , 30 * "-")
       print(color.PURPLE + "[1]" + color.END + "Go Outside")
       print(color.PURPLE + "[2]" + color.END + "Sleep")
       print(color.PURPLE + "[3]" + color.END + "Info")
       print(color.PURPLE + "[4]" + color.END + "Storage")
       print(color.PURPLE + "[5]" + color.END + "Create")
       print(color.PURPLE + "[6]" + color.END + "Save Game")
       print(color.PURPLE + "[7]" + color.END + "Recipe Book")
       if player.hascat == True:
          print(color.PURPLE + "[8]" + color.END + "Cat")
       if player.hasaltar == True:
           print(color.PURPLE + "[9]" + color.END + "Altar")
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
                 if player.health + 5 <= 20:
                    player.health = player.health + 5
                 elif player.health + 1 <= 20:
                    player.health = player.health + 1
                 choice = True
                 next_day()
          else:
             print("Wait, what? It's not time to sleep!")
             achievements.add_achievement("Early Bird: Tried to sleep before nighttime!")
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
       elif (option == "8" or option == "cat") and player.hascat == True:
          kitty()
       elif (option == "9" or option == "altar") and player.hasaltar == True:
          altar()
       elif option == "6" or option == "save game":
          save_game()
       elif option == "7" or option == "recipe book":
           recipe_book()
       else:
          print("That is not an acceptable answer.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()


def recipe_book():
    os.system("cls")
    raritycolor = ""
    if not player.recipes:
        print("No recipes yet!")
        print("")
        pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
        house()
    recipes_no_repeat = list(dict.fromkeys(player.recipes))
    print("Here are your known recipes to CREATE items.")
    for i in recipes_no_repeat:
        for k,j in enumerate(items.all_creatables):
            if j == i:
                print("")
                print("----- " + i + " -----")
                recipe_list = items.craftlist[k]
                for letter in Counter(recipe_list):
                   if letter in items.uncommon_tree_items or letter in items.uncommon_path_items or letter in items.uncommon_creek_items:
                      raritycolor = color.GREEN
                   elif letter in items.rare_tree_items or letter in items.rare_path_items or letter in items.rare_creek_items:
                      raritycolor = color.YELLOW
                   elif letter in items.common_tree_items or letter in items.common_path_items or letter in items.common_creek_items:
                      raritycolor = ""
                   else:
                      raritycolor = color.DARKCYAN
                   print(raritycolor + letter+color.END + ":",Counter(recipe_list)[letter])
    print("")
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    house()

def altar():
    os.system("cls")
    choice = False
    while choice == False:
        print(r"""

              (\                        (\
              .'.                       .'.
            |=| |=======================| |=|
            | | |        ,`-'.          | | |
            | |_|       ( O O )         |_| |
            |            ( ^ )              |
            | X           HHH             X |
            |_______________________________|
            """)
        print("")
        print(30 * "-" , "Altar" , 30 * "-")
        print(color.PURPLE + "[1]" + color.END + "Make Offering")
        print(color.PURPLE + "[2]" + color.END + "Talk to Spirits")
        print(color.PURPLE + "[3]" + color.END + "Go Back")
        print(72 * "-")
        option = input(color.PURPLE + ">>> " + color.END).lower()
        if option == "1" or option == "make offering":
            if any(item in items.offerables for item in player.storage):
                print("Here are the items you can offer to the forest spirits.")
                player.disp_offerables()
                print("Type the name of the item to offer it. Else, 'x' to quit.")
                to_offer = str(input(">>> ")).lower()
                if to_offer in items.offerables and to_offer in player.storage:
                    player.storage.remove(to_offer)
                    print("Your offering was received.")
                    player.spirit_reputation = player.spirit_reputation + 1
                    altar()
                elif to_offer == "x":
                    altar()
                else:
                    print("Not a valid item.")
                    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                    altar()
            else:
                print("You have nothing to offer.")
                pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                altar()
        elif option == "2" or option == "talk to spirits":
            player.reputation = player.reputation - 1
            print(color.PURPLE + "The forest spirits speak." + color.END)
            print("We are the ones who rule the forest. We take care of it, and are of it.")
            print("We are neither good nor bad.")
            print("Offer to us things we enjoy, and we shall help you...")
            print("But be warned. Townsfolk are wary of beings like us.")
            if player.spirit_reputation > 0 and player.spirit_reputation <= 3:
                print("..You have neglected us.")
                print("You have not given us offerings, you have ignored our requests.")
                print("You cannot live in this forest and refuse to coexist.")
                print("Change your ways..or we will destroy you.")
            elif player.spirit_reputation >4 and player.spirit_reputation <= 7:
                print("..You are in good standing with us.")
                print("We will protect you from the wilds of the forest.")
                print("If you continue to treat us well, we will reward you further.")
            elif player.spirit_reputation <= 0:
                achievements.add_achievement("Oathbreaker: Made the spirits angry!")
                true_ending2()
            else:
                print("..You have treated us well and appeased us with offerings.")
                print("We will grant you the gift of immunity from fire and burns.")
                print("You may find it useful...")
                player.immune = True
                player.spirit_immune = False
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            altar()
        elif option == "3" or option == "go back":
            choice = True
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            house()
        else:
            print("Not an acceptable answer.")
            altar()
                    
def use_item():
    os.system("cls")
    if not any(thing in player.storage for thing in items.useables):
        print("You have no items you can use!")
        pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
        return
    else:
        print("Here are the items you can use.")
        for i in player.storage:
            for k,j in enumerate(items.useables):
                if j == i:
                    print("")
                    print(i)
        print("")
        print("Type the name of the item you wish to USE.")
        print("Or, 'x' to go back.")
        useditem = str(input(">>> ")).lower()
        if useditem not in player.storage and useditem != "x":
           print("Not a valid item.")
           pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
           use_item()
        elif useditem == "x":
           pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
           return
        else:
           if useditem == "health potion":
               if player.health == 20:
                   print("Cannot use health potion at max health!")
                   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                   use_item()
               else:
                   print("Used health potion!")
                   for k in range(5):
                       if player.health < 20:
                          player.health = player.health + 1
                   print("Recovered health!")
                   player.storage.remove(useditem)
           elif useditem == "money charm":
               print("Used money charm!")
               randgain = random.randint(1,6)
               player.disks = player.disks + randgain
               print("Gained " + str(randgain) + " Disks!")
               player.storage.remove(useditem)
           elif useditem == "mild poison":
               print("Used mild poison!")
               player.health = player.health - 5
               print("But why would you do that...")
               print("Lost 5 health!")
               player.storage.remove(useditem)
               if player.health <= 0:
                  game_over("Poisoned yourself, for whatever reason.")
                  achievements.add_achievement("Fool: Consumed posion!")
           elif useditem == "deadly poison":
               print("Are you sure about this one?")
               print("It's called deadly for a reason.")
               yn = ""
               print(color.CYAN + "[1]" + color.END + "Yes")
               print(color.CYAN + "[2]" + color.END + "No")
               yn = str(input(">>> ")).lower()
               if yn == "1" or yn == "yes":
                  achievements.add_achievement("Extreme Fool: Consumed deadly poison!")
                  game_over("Poisoned yourself with a deadly posion. Why would you do that?")
               elif yn == "2" or yn == "no":
                  print("Good. It's probably for the best you don't do that.")
               else:
                  print("Not a valid answer.")
           elif useditem == "flying ointment":
              print("Used flying ointment!")
              achievements.add_achievement("Witch Flight: Created and used flying ointment!")
              player.storage.remove(useditem)
              fly()
           pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
           use_item()
                    
                         
def fly():
   os.system("cls")
   print(color.PURPLE + "And I shall go into a hare.." + color.END)
   print(color.PURPLE + "With sorrow and sych and meickle care.." + color.END)
   print(color.PURPLE + "And I shall go in the Spirit's name.." + color.END)
   print(color.PURPLE + "Ay while I come home again." + color.END)
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   os.system("cls")
   choice = False
   while choice == False:
      print(r"""
                ,\
                \\\,_
                 \` ,\
            __,.-" =__)
          ."        )
       ,_/   ,    \/\_
       \_|    )_-\ \_-`
          `-----` `--`
               """)
      print("")
      print(30 * "-" , "Hare" , 30 * "-")
      print(color.PURPLE + "[1]" + color.END + "Kill Townsperson")
      print(color.PURPLE + "[2]" + color.END + "Help Townsperson")
      print(color.PURPLE + "[3]" + color.END + "Go Back")
      print(72 * "-")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "kill townsperson":
         choice = True
         kill()
      elif option == "2" or option == "help townsperson":
         choice = True
         help_town()
      elif option == "3" or option == "go back":
         choice = True
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         house()
      else:
         print("Not an acceptable answer.")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         fly()

def kill():
   os.system("cls")
   player.numkilled = player.numkilled + 1
   if player.numkilled < 10:
      print("You kill a townsperson. There are " + str(10 - player.numkilled) + " left.")
      achievements.add_achievement("Murderer: Killed a townsperson!")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      house()
   elif player.numkilled >= 10:
      print("You killed all the townspeople...")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      murder_ending()

def help_town():
   print("You help the townspeople!")
   player.reputation = player.reputation + 1
   player.spirit_reputation = player.spirit_reputation - 1
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   if player.spirit_reputation <= 3:
      print(color.RED + "The forest spirits are angry..."+ color.END)
   if player.spirit_reputation <= 0:
      true_ending2()
   if player.reputation <=3:
      print(color.RED + "The townspeople are angry..."+ color.END)
   if player.reputation <= 0:
      os.system("cls")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      burn_stake()
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   house()
   
   
        
def kitty():
   os.system("cls")
   choice = False
   foods = ["fish","cat food"]
   while choice == False:
      print(r"""
                      |\_/|   
                      \` ..\
                 __,.-" =__Y=
               ."        )
         _    /   ,    \/\_
        ((____|    )_-\ \_-`
         `-----'`-----` `--`""")
      print(30 * "-" , C.name , 30 * "-")
      print(color.PURPLE + "[1]" + color.END + "Pet")
      print(color.PURPLE + "[2]" + color.END + "Feed")
      print(color.PURPLE + "[3]" + color.END + "Stats")
      print(color.PURPLE + "[4]" + color.END + "Rename")
      print(color.PURPLE + "[5]" + color.END + "Go Back")
      if "cat toy" in player.storage:
          print(color.PURPLE + "[6]" + color.END + "Play")
      if C.hasitem == True:
         print(color.PURPLE + "[7]" + color.END + "Present")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "pet":
         print("You pet " + C.name + "!")
         print(color.PINK + "Purrr..." + color.END)
         if C.affection + 2 <= 20:
            C.affection = C.affection + 2
            print(C.name + " is more affectionate towards you!")
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
            if foodname in foods:
                player.storage.remove(foodname)
                C.hunger = C.hunger - 4
                print("Fed " + C.name + "!")
            else:
                print("Not a valid food!")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            kitty()
      elif option == "3" or option == "stats":
         C.disp_stats()
         print("")
         print("Remember, you must take care of your cat!")
         print("You wouldn't want " + C.name + " to run away!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         kitty()
      elif option == "4" or option == "rename":
         print("New name?")
         C.name = str(input(">>> "))
         print("Ok!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         kitty()
      elif option == "5" or option == "go back":
         choice = True
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         house()
      elif (option == "6" or option == "play") and "cat toy" in player.storage:
          player.storage.remove("cat toy")
          print("You gave " + C.name + " a toy!")
          C.hastoy = True
          print(C.name + " won't require affection as much")
          print("until the toy wears out.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          kitty()
      elif (option == "7" or option == "present") and C.hasitem == True:
         randitem = random.choice(items.buyables)
         print("Look! " + C.name + " has brought you a present!")
         print("You got a " + str(randitem) + "!")
         print("Added to storage.")
         player.storage.append(randitem)
         C.hasitem = False
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
            achievements.add_achievement("Weaver: Upgraded your basket!")
            print(color.PURPLE + "Upgraded Basket!" + color.END)
         if itemname == "altar":
             player.storage.remove(itemname)
             player.hasaltar = True
             player.reputation = player.reputation - 2
             achievements.add_achievement("Spiritual: Created an altar!")
             print(color.PURPLE + "The ALTAR was now added to your house!" + color.END)
         if itemname == "mushroom house" and player.housetype == "regular":
            player.storage.remove(itemname)
            player.housetype = "mushroom"
            print(color.PURPLE + "You now have a MUSHROOM house!" + color.END)
            achievements.add_achievement("Mushroom Living: Created a mushroom house!")
         if itemname == "mushroom house" and player.housetype == "mushroom":
            print("You already have a mushroom house!")
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
            if encounter <= 70:
               item_got = random.choice(items.common_tree_items)
            elif encounter > 70 and encounter < 95:
               item_got = random.choice(items.uncommon_tree_items)
            elif encounter >= 95:
               item_got = random.choice(items.rare_tree_items)
         elif place == 2: #path
            encounter = random.randint(0,100)
            if encounter <= 70:
               item_got = random.choice(items.common_path_items)
            elif encounter > 70 and encounter < 95:
               item_got = random.choice(items.uncommon_path_items)
            elif encounter >= 95:
               item_got = random.choice(items.rare_path_items)
         elif place == 3: #creek
            encounter = random.randint(0,100)
            if encounter <= 70:
               item_got = random.choice(items.common_creek_items)
            elif encounter > 70 and encounter < 95:
               item_got = random.choice(items.uncommon_creek_items)
            elif encounter >= 95:
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

def cat_chance_encounter(place):
   yn = ""
   otherchoice = False
   choice = False
   if player.hascat == False:
      flee_chance = random.randint(0,100)
      print("....")
      print(color.BOLD + "Oh look! It's a cat!" + color.END)
      achievements.add_achievement("Lucky: Encountered a cat!")
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
               achievements.add_achievement("Unlucky: A cat ran away from you!")
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
                     C.name = str(input(">>> "))
                     print("Ok!")
                     print("You can now find FISH at the creek!")
                     print("You can now buy CAT FOOD at the marketplace!")
                     items.common_creek_items.append("fish")
                     items.common_creek_items.append("fish")
                     items.buyables.append("cat food")
                     achievements.add_achievement("Pet Owner: Adopted a forest cat!")
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

def animal_chance_encounter(place):
    rand_cat_enc = random.randint(0,400)
    rand_enemy_enc = random.randint(0,600)
    if rand_cat_enc <= 3:
        cat_chance_encounter(place)
    if rand_enemy_enc <= 10:
        enemy_chance_encounter(place)

def enemy_chance_encounter(place):
    os.system("cls")
    flee_chance = random.randint(0,100)
    health_lost = random.randint(2,5)
    items_lost = random.randint(1,3)
    print("....")
    print(color.BOLD + "A wild animal appeared!" + color.END)
    print(r"""
                |\_/|,,_____,~~`
                (.".)~~     )`~}}
                 \o/\ /---~\\ ~}}
                   _//    _// ~}
                                """)
    print("....")
    if flee_chance <= 10 or (player.hasaltar == True and player.spirit_reputation > 4):
        print("You escape unharmed.")
        achievements.add_achievement("Evader: Escaped a wild animal!")
    elif flee_chance <= 50 and flee_chance > 10:
        print("You escaped and lost " + str(health_lost) + " health!")
        player.health = player.health - health_lost
    elif len(player.basket) >= 3 and flee_chance > 50:
        print("You escaped and lost " + str(health_lost)+ " health and " + str(items_lost) + " items from your basket!")
        player.health = player.health - health_lost
        for i in range(items_lost):
            player.basket.remove(random.choice(player.basket))
    else:
        print("You escaped and lost " + str(health_lost * 2) + " health!")
        player.health = player.health - (health_lost * 2)
    if player.health <= 0:
        achievements.add_achievement("Weakling: Died to a wild animal attack!")
        game_over(" A wild animal encounter")
    else:
        pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
        forage(place)
        
    
    
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
      print(color.PURPLE + "[5]" + color.END + "Fortune-Teller")
      if player.day % 2 == 0:
         print(color.PURPLE + "[6]" + color.END + "Builder")
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
         if player.encounter == False:
            print("You have no errands to run today.")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
         else:
            choice = True
            errand()
      elif option == "5" or option == "fortune teller":
          fortune_teller()
      elif (option == "6" or option == "builder") and player.day % 2 == 0:
         builder()
      else:
         print("That is not an acceptable answer.")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         town()

def builder():
   os.system("cls")
   print("Hello! I'm the builder!")
   if "mushroom house" not in player.recipes:
      print("I got something real neat here.")
      print("I'll offer you a special recipe..for 20 Disks!")
      print("What do you say?")
      print(color.PURPLE + "[1]" + color.END + "Yes")
      print(color.PURPLE + "[2]" + color.END + "No")
      yn = input(color.PURPLE + ">>> " + color.END).lower()
      if yn == "1" or yn == "yes":
         if player.disks >= 20:
            print("Great, thanks! I've added it to your RECIPE BOOK!")
            player.recipes.append("mushroom house")
            player.disks = player.disks - 20
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
         elif player.disks < 20:
            print("Not enough disks!")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
      elif yn == "2" or yn == "no":
         print("Ok then!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         town()
      else:
         print("Not a valid answer")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         builder()
   elif player.housetype == "mushroom":
      print("I've noticed you're living in a mushroom.")
      print("For 20 Disks, I can build your REGULAR house back again!")
      if yn == "1" or yn == "yes":
         if player.disks >= 20:
            print("Great, thanks!")
            player.disks = player.disks - 20
            player.housetype = "regular"
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
         elif player.disks < 20:
            print("Not enough disks!")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
      elif yn == "2" or yn == "no":
         print("Ok then!")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         town()
      else:
         print("Not a valid answer")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         builder()
   else:
      print("I don't have anything for you at the moment.")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      town()
      
def fortune_teller():
    os.system("cls")
    recipe_chance = random.randint(0,100)
    player.inc_time(30)
    print(color.PURPLE + r"""

                        *    .
        '  +   ___    @    .
            .-" __"-.   +
    *      /:.'`__`'.\       '
        . |:: .'_ `. :|   *
   @      |:: '._' : :| .
      +    \:'.__.' :/       '
            /`-...-'\  '   +
   '       /         \   .    @
     *     `-.,___,.-'
                                """+ color.END)
    print(color.PURPLE+"Hello! Welcome to the Fortune-Teller booth!"+color.END)
    print(".....")
    if player.reputation <= 3:
        print("You'd better watch out. It seems you're not very popular among the townsfolk.")
        print("I've even heard rumors of evil witchcraft and sorcery.")
        print("You haven't been meddling about with spirits, have you?")
        print("You know that's very frowned upon...")
        print("In your future, I see...a burning wooden pillar...screams..pain..")
        print(".....")
        print("My advice is to regain the town's trust before things go wrong.")
    elif player.reputation <= 7 and player.reputation > 3:
        print("I see in your future..the forest..helping us..")
        print("You are in good standing with the townsfolk.")
        print("Nothing should cause you disrupt to your way of life if you continue like this.")
        print("...")
        if recipe_chance <= 30:
            print("Because you're becoming well-liked, you can have a RECIPE.")
            recipe_given = "hhhhhhh"
            while recipe_given not in player.recipes:
                recipe_given = random.choice(items.askables)
                player.recipes.append(recipe_given)
            print("You got the recipe for " + recipe_given + "!")
    elif player.reputation > 7:
        print("I see..you helping others..being a good citizen..")
        print("You are in very good standing with the townsfolk.")
        print("Everyone here seems to like you.")
        print("We will protect you in the case of evil spirits.")
        player.immune = False
        player.spirit_immune = True
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    town()       

    

def marketplace():
   os.system("cls")
   choice = False
   common_price = 2
   uncommon_price = 5
   rare_price = 10
   numitems = 1
   toremove = 0
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
                   print("Ok.")
                else:
                   print("You can't do that.")
            if sellitem in items.common_tree_items or sellitem in items.common_path_items or sellitem in items.common_creek_items:
               print("I can give you " + str(common_price * numitems) + " Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + (common_price * numitems)
                  for i in range(numitems):
                      player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.uncommon_tree_items or sellitem in items.uncommon_path_items or sellitem in items.uncommon_creek_items:
               print("I can give you " + str(uncommon_price * numitems)+" Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + (uncommon_price * numitems)
                  for i in range(numitems):
                      player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.rare_tree_items or sellitem in items.rare_path_items or sellitem in items.rare_creek_items:
               print("I can give you " + str(rare_price * numitems)+" Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + (rare_price * numitems)
                  for i in range(numitems):
                      player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.askables:
               print("A created item? Prices may vary day to day.")
               print("I can give you " + str(randsellprice) + " Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + randsellprice
                  for i in range(numitems):
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
            elif player.disks < randbuyprice:
                print("You don't have enough Disks!")
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
   set_prices()
   player.cansleep = False
   if player.hascat == True:
      C.hunger = C.hunger + 3
      if C.hastoy == True:
          C.toywear = C.toywear - 1
          if C.toywear <= 0:
              C.hastoy = False
   if player.hasaltar == True:
       player.spirit_reputation = player.spirit_reputation - 1
   if player.day == 20:
      end_game()
   player.time = 420
   if player.passed_out == True:
      player.health = player.health - 5
      if player.hasaltar == True:
          player.spirit_reputation = player.spirit_reputation - 1
      if player.health <= 0:
          death = "Exhaustion"
          achievements.add_achievement("Insomniac: Died from lack of sleep!")
          game_over(death)
   player.passed_out = False
   print("It's the next day.")
   print(color.BOLD + "Time to wake up!" + color.END)
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   if player.day != 5:
       townsfolk_rand_encounter()
   else:
       obtain_altar_recipe()

def obtain_altar_recipe():
    os.system("cls")
    print(color.PURPLE + "The forest spirits are trying to tell you something..." + color.END)
    print("We are the spirits of the forest of which you live..")
    print("We would like to accept you as part of the forest life.")
    print('"Build an ALTAR to us and we can protect you!"')
    print("We can help you...")
    player.recipes.append("altar")
    print("ALTAR recipe added to recipe book!")
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    house()

def set_prices():
    global randbuyprice
    global randsellprice
    randbuyprice = random.randint(5,20)
    randsellprice = random.randint(8,15)
    
def townsfolk_rand_encounter():
   global offered_disks
   global randitem
   rand_enc = random.randint(0,100)
   randitem = random.choice(items.askables)
   offered_disks = random.randint(2,10)
   """for c,i in enumerate(items.askables):
      if i == randitem:
         materials = items.craftlist[c]"""
   if rand_enc <= 50:
      player.encounter = True
      os.system("cls")
      print(color.BOLD + "*KNOCK KNOCK*" + color.END)
      print("...")
      print("You hear knocking at your door!")
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      print("You open the door..")
      print(color.CYAN + "I'm from the town! I've come to you because I really need help with something!" + color.END)
      print(color.CYAN + "Can you please make me a " + str(randitem) + "?" + color.END)
      print(color.CYAN + "It's important..." + color.END)
      """print(color.CYAN + "To make it, you will need:" + color.END)
      for letter in Counter(materials):
          print(letter+":",Counter(materials)[letter])"""
      if randitem not in player.recipes:
          player.recipes.append(randitem)
          print("I've added the item to you recipe book!")
      else:
          print("The item should be in your recipe book!")
      print("")
      print(color.CYAN + "And I'll need it by the end of the day." + color.END)
      print(color.CYAN + "I'll be in the town if you need me.." + color.END)
      print(color.CYAN + "But if you really can't make it, then that's fine, I guess." + color.END)
      print(color.CYAN + "I'll give you " + str(offered_disks) + " Disks " + "for it though!" + color.END)
      print(color.CYAN + "Anyways, bye!" + color.END)
      pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
      house()
   else:
      player.encounter = False
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
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
         else:
            print(color.CYAN + "Oh! My " + str(randitem) + "!" + color.END)
            player.basket.remove(randitem)
            print(color.CYAN + "Thanks! Here's your " + str(offered_disks) + " Disks!" + color.END)
            player.disks = player.disks = offered_disks
            player.encounter = False
            valid = True
            player.townsfolk_helped = player.townsfolk_helped + 1
            achievements.add_achievement("Helper: Helped a townsperson!")
            if player.reputation < 10:
                player.reputation = player.reputation + 1
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            town()
      elif option == "2" or option == "no":
         print(color.CYAN + "No?.. Well, okay then." + color.END)
         achievements.add_achievement("Denier: Denied a townsperson their request!")
         player.reputation = player.reputation - 2
         valid = True
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         town()
      else:
         print("Not a valid answer.")
         errand()


def burn_stake():
    os.system("cls")
    print(color.RED+r"""

                (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         """+color.END)
    print(color.RED + "WE ARE HERE." + color.END)
    print(color.RED + "WE, THE GOOD TOWNSFOLK, KNOW WHAT YOU'VE DONE." + color.END)
    print(color.RED + "WITCHCRAFT. SORCERY. EVILS." + color.END)
    print(color.RED + "SPEAKING WITH SPIRITS IS SORCERY." + color.END)
    print(color.RED + "WHAT SAY YOU IN YOUR DEFENSE?" + color.END)
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    print(color.RED + "....." + color.END)
    print(color.RED + "NOTHING?" + color.END)
    print(color.RED + "BURN. BURN. BURN." + color.END)
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    if player.immune == False:
        achievements.add_achievement("Witch: Burnt at stake!")
        game_over("Witchcraft accusations, burned to death by the townsfolk.")
    elif player.immune == True:
        true_ending()

def true_ending2():
    os.system("cls")
    pygame.mixer.init()
    curpath = os.path.dirname(os.path.abspath(__file__))
    rel_path = "game-data"
    target = "theme.wav"
    path = os.path.join(curpath, rel_path,target)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(3)
    print(color.RED + "YOU HAVE GREATLY OFFENDED US, THE FOREST SPIRITS." + color.END)
    print(color.RED + "NO LONGER SHALL YOU LIVE HERE IN OUR FOREST." + color.END)
    print(color.RED + "NO LONGER SHALL YOU TRANSGRESS US." + color.END)
    print(color.RED + "YOU...WILL DIE." + color.END)
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    os.system("cls")
    if player.spirit_immune == False:
        game_over("The forest spirit's wrath.")
    elif player.spirit_immune == True:
        print("No.")
        print(r"""
   
  //^\\\   ,;;;,                       
 ((-_-))) (-_- ;                      
  )))(((   >..'.    .:.     .--.      
 ((_._ )  /.   .|  :-_-;   /-_-))
 _))  ((_//|   ||  ,`-'.   ))-((
 `(    )`' |___|),;,   \\_/,`  ))
   \  /    | | |`' |___(/-'|___()  
    )(     | | |   | | |   | | |  
   /__\    |_|_|   |_|_|   |_|_|  
   `''     `-'-'   `-'-'   `-'-'
               """)
        print("We, the townspeople, have noticed your kindess and willingness to abide by our laws.")
        print("We will keep you safe..")
        print("The spirits cannot claim you if you are not one of the forest.")
        print("We invite you to join us, in our town.")
        print("Come. We are here.")
        achievements.add_achievement("Community: Saved by the town!")
        pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
        os.system("cls")
        pygame.mixer.music.stop()
        print("")
        print(color.BOLD + "Thanks for playing!" + color.END)
        print(color.PURPLE + " Game Ended" + color.END)
        print(color.BOLD + "Find your ACHIEVEMENTS in the View Achievements menu" + color.END)
        generate_achievements()
        pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
        start_game()

        
def true_ending():
    os.system("cls")
    pygame.mixer.init()
    curpath = os.path.dirname(os.path.abspath(__file__))
    rel_path = "game-data"
    target = "theme.wav"
    path = os.path.join(curpath, rel_path,target)
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(3)
    print(r"""

            '                                  `:.
         ::'                                    `::
        :: :.                                  .: ::
         `:. `:.             .             .:'  .:'
           `::. `::          !           ::' .::'
              `::.`::.    .' ! `.    .::'.::'
                `:.  `::::'':!:``::::'   ::'
                :'*:::.  .:' ! `:.  .:::*`:
               :: HHH::.   ` ! '   .::HHH ::
              ::: `H TH::.  `!'  .::HT H' :::
              ::..  `THHH:`:   :':HHHT'  ..::
              `::      `T: `. .' :T'      ::'
                `:. .   :         :   . .:'
                  `::'               `::'
                    :'  .`.  .  .'.  `:
                    :' ::.       .:: `:
                    :' `:::     :::' `:
                     `.  ``     ''  .'
                      :`...........':
                      ` :`.     .': '
                       `:  `''''  :'
          """)
    print(color.GREEN + "...NO." + color.END)
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    print(color.GREEN + "WE ARE THE SPIRITS OF THE FOREST." + color.END)
    print(color.GREEN + "WE HAVE GRANTED THEM IMMUNITY." + color.END)
    print(color.GREEN + "COME. FLY WITH US." + color.END)
    print(color.GREEN + "LIVE AND HAVE SOVEREIGNTY." + color.END)
    achievements.add_achievement("Animist: Saved by the spirits!")
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    pygame.mixer.music.stop()
    os.system("cls")
    print("")
    print(color.BOLD + "Thanks for playing!" + color.END)
    print(color.PURPLE + " Game Ended" + color.END)
    print(color.BOLD + "Find your ACHIEVEMENTS in the View Achievements menu" + color.END)
    generate_achievements()
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    start_game()


def murder_ending():
   os.system("cls")
   pygame.mixer.init()
   curpath = os.path.dirname(os.path.abspath(__file__))
   rel_path = "game-data"
   target = "theme.wav"
   path = os.path.join(curpath, rel_path,target)
   pygame.mixer.music.load(path)
   pygame.mixer.music.play(3)
   print(r"""

         .AMMMMMMMMMMA.          
       .AV. :::.:.:.::MA.        
      A' :..        : .:`A       
     A'..              . `A.     
    A' :.    :::::::::  : :`A    
    M  .    :::.:.:.:::  . .M    
    M  :   ::.:.....::.:   .M    
    V : :.::.:........:.:  :V    
   A  A:    ..:...:...:.   A A   
  .V  MA:.....:M.::.::. .:AM.M   
 A'  .VMMMMMMMMM:.:AMMMMMMMV: A  
:M .  .`VMMMMMMV.:A `VMMMMV .:M: 
 V.:.  ..`VMMMV.:AM..`VMV' .: V  
  V.  .:. .....:AMMA. . .:. .V   
   VMM...: ...:.MMMM.: .: MMV    
       `VM: . ..M.:M..:::M'      
         `M::. .:.... .::M       
          M:.  :. .... ..M       
          V:  M:. M. :M .V       
          `V.:M.. M. :M.V'
                         """)
   print(color.RED + "FOOLISH WITCH." + color.END)
   print(color.RED + "DON'T YOU KNOW..." + color.END)
   print(color.RED + "THE DEAD ARE SPIRITS TOO?" + color.END)
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   print(color.RED + "YOU WILL NOT JOIN US WHEN YOU DIE." + color.END)
   print(color.RED + "YOU WILL BURN..." + color.END)
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   pygame.mixer.music.stop()
   achievements.add_achievement("Karma: Got what you deserved!")
   game_over("Karma getting you. You killed the whole town!")

def game_over(death):
    os.system("cls")
    print(color.BOLD + "You died...." + color.END)
    print(color.BOLD + "Of.. " + death + color.END)
    print("Maybe the forest life isn't for you!")
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    print("You can always try again, though.")
    print(color.BOLD + "Find your ACHIEVEMENTS in the View Achievements menu" + color.END)
    generate_achievements()
    print(color.BOLD + "Thanks for playing!" + color.END)
    print(color.PURPLE + " Game Ended" + color.END)
    pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
    start_game()


def end_game():
   os.system("cls")
   print(color.BOLD + "That's the end of the game so far!" + color.END)
   print(color.BOLD + "I hope you enjoyed it!" + color.END)
   print("But if you're seeing this, you didn't get to the TRUE ending.")
   print("Keep trying!")
   print(color.BOLD + "Find your ACHIEVEMENTS in the View Achievements menu" + color.END)
   generate_achievements()
   print(color.BOLD + "Thanks for playing!" + color.END)
   print(color.PURPLE + " Game Ended" + color.END)
   start_game()

def save_game():
   curpath = os.path.dirname(os.path.abspath(__file__))
   rel_path = "game-data"
   target = "Save File"
   path = os.path.join(curpath, rel_path,target)
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
         try:
             with open(path,"wb") as file:
                pickle.dump(Data_Save,file)
             print("Game Saved!")
             pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
             house()
         except IOError:
            print("This is weird. A save file could not be found or created.")
            print("If you're seeing this message, perhaps contact the dev.")
            print("In the meantime, you can still play the game..")
            print("You just can't save until this gets fixed!")
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
   curpath = os.path.dirname(os.path.abspath(__file__))
   rel_path = "game-data"
   target = "Save File"
   path = os.path.join(curpath, rel_path,target)
   try:
      if os.path.getsize(path) > 0:
          with open(path,"rb") as file:
              savedata = pickle.load(file)
              player = savedata[0]
              C = savedata[1]
              pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
              house()
      else:
         print("There is nothing to load. Exiting...")
         pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
         start_game()
   except IOError:
       print("Your Save File was either moved or deleted, and could not be found!")
       sys.exit()

def generate_achievements():
   curpath = os.path.dirname(os.path.abspath(__file__))
   rel_path = "game-data"
   target = "Achievements.txt"
   path = os.path.join(curpath, rel_path,target)
   with open(path,"w") as a_file:
      for item in achievements.a_list:
         a_file.write("%s\n" % item)
   
def opening_game():
   os.system("cls")
   global player
   global C
   achievements.a_list.clear()
   achievements.add_achievement("      ")
   generate_achievements()
   set_prices()
   print("")
   print("")
   print("-------------------------------------------------------------------------------")
   print("Hello! This is actually a testing version of FORAGING SIMULATOR!")
   print("Though it is hopefully still fun, the purpose of this release is to TEST gameplay!")
   print("Please report any bugs or obvious issues to...alexneely8@gmail.com")
   print("Unless you know me, the creator, already. In which case..you can just tell me.")
   print("If the game crashes for any reason, you can find the bug report in the exceptions.log file!")
   print("-------------------------------------------------------------------------------")
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   os.system("cls")
   print(color.PURPLE + "..Hey! Your house is finally built." + color.END)
   print(color.PURPLE + "Don't know why you wanted it all the way out here in the forest." + color.END)
   print(color.PURPLE + "Maybe you just like fresh air." + color.END)
   print(color.PURPLE + "..." + color.END)
   print(color.PURPLE + "What's that? You like FORAGING and CRAFTING?" + color.END)
   print(color.PURPLE + "Seems like a good enough reason. I'm sure it'll be fine, it's not too far from the town." + color.END)
   print(color.PURPLE + "Few things you should know first." + color.END)
   print(color.PURPLE + "Sorcery and witchcraft is illegal in these parts!" + color.END)
   print(color.PURPLE + "Though if you don't care about all that, just know it's always best to be in good standing with others." + color.END)
   print(color.PURPLE + "You know. Have a good reputation and all that. Save your back in case things go wrong." + color.END)
   print(color.PURPLE + "Well, that's enough from me! I'll go back to my own town now." + color.END)
   print(color.PURPLE + "Enjoy your new house!" + color.END)
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   os.system("cls")
   player = Player(20,[],[],8,10,1,420,6,6,0,False,False,False,False,[],False,False,"regular",0)
   C = cat(" ",2,10,False,10,False)
   house()

def start_game():
   os.system("cls")
   pygame.mixer.init()
   curpath = os.path.dirname(os.path.abspath(__file__))
   rel_path = "game-data"
   target = "theme.wav"
   path = os.path.join(curpath, rel_path, target)
   pygame.mixer.music.load(path)
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
      print(color.PURPLE + "[3] " + color.END + "View Achievements")
      print(color.PURPLE + "[4] " + color.END + "Exit")
      option = input(color.PURPLE + ">>> " + color.END).lower()
      if option == "1" or option == "new game":
         choice = True
         opening_game()
      elif option == "2" or option == "load game":
         choice = True
         load_game()
      elif option == "4" or option == "exit":
         print(color.PURPLE + "Entering reality...." + color.END)
         choice = True
         sys.exit()
      elif option == "3" or option == "view achievements":
          view_achievements()
      else:
         print("That is not an acceptable answer.")

def view_achievements():
    curpath = os.path.dirname(os.path.abspath(__file__))
    rel_path = "game-data"
    target = "Achievements.txt"
    path = os.path.join(curpath, rel_path, target)
    try:
        with open(path,"r") as file:
           if not file.read(1):
              print("No achievements yet!")
           else:
              aa = file.readlines()
              for line in aa:
                 print(" " + line)
           pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
           start_game()
    except IOError:
            print("Looks like your Achivements file is missing.")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            start_game()
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
   
