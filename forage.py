
import sys
import random
import os
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

class player:
    health = 20
    max_health = 20
    storage = []
    basket = []
    basketsize = 5
    disks = 5
    day = 1
    time = 420 #420 mins = 7 AM, 1320 mins = 12 AM
    suspicion = 0
    danger = 0
    townsfolk_helped = 0
    cansleep = False
    passed_out = False
    def disp_stats():
       hhmm = '{:02d}:{:02d}'.format(*divmod(player.time, 60))
       print("Health: " + str(player.health) + "/20"," Disks: " + str(player.disks)," Day: " + str(player.day)," Time: " + str(hhmm))
    def disp_storage():
       for letter in Counter(player.storage):
          print(letter+":",Counter(player.storage)[letter])
       #print(type(Counter(player.storage)))
       #print(*player.storage, sep = "\n")
    def disp_basket():
       for letter in Counter(player.basket):
          print(letter+":",Counter(player.basket)[letter])
    def inc_time(mins):
       player.time = player.time + mins
       if player.time >= 840:
          player.cansleep = True
       if player.time == 1140:
          print(color.RED + "You are running low on time." + color.END)
          print(color.RED + "You have 3 hours to get to bed before your health suffers." + color.END)
       if player.time >= 1320:
          print(color.RED + "You didn't go to bed, did you?" + color.END)
          print(color.RED + "You are reminded of your own morrtality as you collapse on the ground." + color.END)
          print(color.RED + "The forest spirits may take care of you this time, but there will be consequences tomorrow." + color.END)
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          player.passed_out = True
          next_day()
    def item_info():
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
          if itemname in items.askables:
             itemtype = "Creatable Item"
          elif itemname in items.buyables:
             itemtype = "Buyable Item"
          else:
             itemtype = "Foraged Item"
          print("Rarity: " + rarity + " --- "+ " Type: " + itemtype)
       else:
          player.arrange_storage()
    def arrange_storage():
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
                for i in player.basket:
                   player.storage.append(i)
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
                player.storage.remove(moveditem)
                arrange_storage()
          elif option == "4" or option == "toss basket item":
             player.disp_basket()
             print("Type the name of the item you wish to toss.")
             moveditem = str(input(">>> ")).lower()
             if moveditem not in player.basket:
                print("Not a valid item.")
                pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
                player.arrange_storage()
             else:
                player.basket.remove(moveditem)
                arrange_storage()
          elif option == "5" or option == "view storage":
             player.disp_storage()
             player.item_info()
             pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
             player.arrange_storage()
          elif option == "6" or option == "view basket":
             player.disp_basket
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
                     "large basket"]
   
   askables = ["love potion","curse talisman","money charm",
                      "health potion","sweet tea","deadly poison",
                      "vegetable soup","bread loaf","sweet perfume",
                      "candle","strong incense","luck charm",
                      "protection amulet","berry juice","berry pie",
                      "bitter tea","mild poison","mushroom soup","wreath"]
   
   offerables = ["bread loaf","strong incense","berry pie","berry juice",
                 "sweet perfume","vegetable soup","mushroom soup"]


   common_tree_items = ["stick","pine needles","oak bark","acorns","cedar resin"]
   uncommon_tree_items = ["honey","beeswax","morel","laetiporus"]
   rare_tree_items = ["fly agaric"]


   common_path_items = ["clovers","dandelion","rosemary","green sage","lemonbalm",
                        "lavender","blackberries","raspberries"]
   uncommon_path_items = ["rose petals","hemlock","chamomile","ginger","wild carrot",
                          "wild onion","wild garlic"]
   rare_path_items = ["belladonna berries"]
   

   common_creek_items = ["stick","pebbles","morel","oak bark"]
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
    ["stick","stick","stick","stick","stick","stick","string","cloth","oak bark"] #large basket
      
    ]

    
def house():
    os.system('cls')
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
                    pc.health = pc.health + 1
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
       else:
          print("That is not an acceptable answer.")
          pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
          house()
       

def create():
   os.system("cls")
   creatable_ints = []
   creatables = []
   os.system("cls")
   itemname = ""
   for c,i in enumerate(items.craftlist):
      can_create = all(elem in player.storage for elem in items.craftlist[c])
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
   choice = str(input(">>> "))
   valid = False
   while valid == False:
      if choice == "1" or choice == "Yes":
         valid = True
         player.inc_time(30)
         #remove materials from storage, put the created thing into storage
         for m,n in enumerate(creatables):
            if n == itemname:
               list_to_remove_from = m
         for p in items.craftlist[list_to_remove_from]:
            player.storage.remove(p)
         player.storage.append(itemname)
      elif choice == "2" or choice == "No":
         valid = True
         create()
      else:
         print("Not a valid answer")
      

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
         if place == 1: #fallen trees
            encounter = random.randint(0,100)
            if encounter <= 50:
               item_got = random.choice(items.common_tree_items)
            elif encounter > 50 and encounter < 90:
               item_got = random.choice(items.uncommon_tree_items)
            elif encounter >= 90:
               item_got = random.choice(items.rare_tree_items)
         elif place == 2: #path
            encounter = random.randint(0,100)
            if encounter <= 50:
               item_got = random.choice(items.common_path_items)
            elif encounter > 50 and encounter < 90:
               item_got = random.choice(items.uncommon_path_items)
            elif encounter >= 90:
               item_got = random.choice(items.rare_path_items)
         elif place == 3: #creek
            encounter = random.randint(0,100)
            if encounter <= 50:
               item_got = random.choice(items.common_creek_items)
            elif encounter > 50 and encounter < 90:
               item_got = random.choice(items.uncommon_creek_items)
            elif encounter >= 90:
               item_got = random.choice(items.rare_creek_items)
         print(color.BOLD + "You got: " + str(item_got) + "!" + color.END)
         if len(player.basket) < player.basketsize:
            player.basket.append(item_got)
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            forage(place)
         else:
            print("...There's no room in your basket! You discard the item.")
            pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
            forage(place)
      if option == "2" or option == "go back":
         choice = True
         look_forest()

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
            if sellitem in common_tree_items or sellitem in common_path_items or sellitem in common_creek_items:
               print("I can give you 2 Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + 2
                  player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.uncommon_tree_items or sellitem in items.uncommon_path_items or sellitem in items.uncommon_creek_items:
               print("I can give you 5 Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + 5
                  player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.rare_tree_items or sellitem in items.rare_path_items or sellitem in items.rare_creek_items:
               print("I can give you 10 Disks.")
               print(color.PURPLE + "[1]" + color.END + "Yes")
               print(color.PURPLE + "[2]" + color.END + "No")
               yn = input(color.PURPLE + ">>> " + color.END).lower()
               if yn == "1" or yn == "yes":
                  player.disks = player.disks + 10
                  player.basket.remove(sellitem)
               elif yn == "2" or yn == "no":
                  print("Okay then.")
               else:
                  print("Not a valid answer.")
            elif sellitem in items.all_creatables():
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
         randbuyprice = random.randint(5,20)
         print("Great! Take a look at what we have.")
         print(*items.buyables, sep = "\n")
         print("")
         print("Prices vary, today everything is " + str(randbuyprice) + " Disks.")
         print("Type the name of the item you want to buy, else X to go back.")
         buyitem = str(input(">>> ")).lower()
         if buyitem not in items.buyables:
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
   player.cansleep = False
   if player.day == 5:
      end_game()
   player.time = 420
   if player.passed_out == True:
      player.health = 15
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
         if randitem not in basket:
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


def start_game():
   os.system("cls")
   print(color.PURPLE + "Welcome to FORAGING SIMULATOR." + color.END)
   print(color.PURPLE + "A game where you live on the edge of a forest." + color.END)
   print(color.PURPLE + "Some call you wise, others call you a witch." + color.END)
   print(color.PURPLE + "But really, your passion is FORAGING items, as well as CRAFTING new ones." + color.END)
   print(color.PURPLE + "You can help people, or hurt them, the choice will be yours." + color.END)
   print(color.PURPLE + "But in the end, the fate of the small town is in your hands." + color.END)
   print("")
   print(color.PURPLE + "You have TWO WEEKS." + color.END)
   print(color.PURPLE + "Good luck." + color.END)
   print("")
   print("")
   print("-------------------------------------------------------------------------------")
   print("Hello! This is actually a testing version of FORAGING SIMULATOR!")
   print("You'll have 5 days in this one, and you won't get to see the main storyline or conflicts.")
   print("Though it is hopefully still somewhat fun, the purpose of this release is to TEST gameplay!")
   print("Please report any bugs or obvious issues to...alexneely8@gmail.com")
   print("Unless you know me, the creator, already. In which case..you can just tell me.")
   print("-------------------------------------------------------------------------------")
   pressenter = input(color.BLUE + "(PRESS ANY KEY TO CONTINUE)" + color.END)
   house()


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





   
