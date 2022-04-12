#!/usr/bin/env python3

import os
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Pokemon RPG
========
Commands:
  go [direction]
  catch [pokemon]
''')

def showMap():

  north = ""
  east = ""
  south = ""
  west = "\t"

  if 'north' in rooms[currentRoom]:
    north = rooms[currentRoom]['north']

  if 'east' in rooms[currentRoom]:
    east = rooms[currentRoom]['east']

  if 'south' in rooms[currentRoom]:
    south = rooms[currentRoom]['south']
  
  if 'west' in rooms[currentRoom]:
    west = rooms[currentRoom]['west']

  print(f"\t\t{north}")
  print(f"\n\t\t  ↑")
  print(f"{west}\t← + →\t{east}")
  print(f"\t\t  ↓\n")
  print(f"\t\t{south}")

def showStatus():
  showMap()
  #print the player's current status
  print('---------------------------')
  print('You are in ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "pokemon" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['pokemon'])
  print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Pallet Town' : {
                  'north' : 'Route 1',
                  'pokemon': 'pikachu'
                },
            'Route 1'     :{
                  'south' : 'Pallet Town',
                  'north' : 'Viridian City'
            },
            'Viridian City': {
                  'north' : 'Viridian Forest',
                  'south' : 'Route 1',
                  'west'  : 'Route 22',
                },
            'Route 22'    : {
                  'east'  : 'Viridian City',
                  'north' : 'Route 23',
               },
            'Route 23'    : {
                  'north' : 'Victory Road',
                  'south' : 'Route 22',
                  'pokemon': 'seadra'
               },
            'Victory Road': {
                  'north' : 'Indigo Plateau',
                  'south' : 'Route 23',
            },
            'Indigo Plateau': {
                  'south' : 'Victory Road',
        
            },
            'Viridian Forest': {
                  'north' : 'Pewter City',
                  'south' : 'Viridian City',
                  'pokemon': 'metapod'
            },
            'Pewter City' : {
                  'east'  : 'Route 3',
                  'south' : 'Viridian Forest',
            },
            'Route 3'     : {
                  'east'  : 'MT. Moon',
                  'west'  : 'Pewter City',
                  'pokemon'  : 'pidgey',
            },
            'MT. Moon'    : {
                  'west'  : 'Route 3',
                  'pokemon'  : 'onix',
            }
         }

#start the player in the Hall
currentRoom = 'Pallet Town'

showInstructions()

#loop forever
while True:
  # os.system("clear")
  
  showStatus()

  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)
  print(move[0])
  print(move[1])

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'catch' first
  if move[0] == 'catch' :
    #if the room contains an item, and the item is the one they want to get
    if "pokemon" in rooms[currentRoom] and move[1] in rooms[currentRoom]['pokemon']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' Caught!')
      #delete the item from the room
      del rooms[currentRoom]['pokemon']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
  
  ## Define how a player can win
  if currentRoom == 'Indigo Plateau' and 'pikachu' in inventory and 'seadra' in inventory and 'pidgey' in inventory and 'metapod' in inventory and 'onix' in inventory:
    print('You faced the Elite Four and the Current Champion and defeated them!')
    print('!!! CONFRATULATIONS YOU WON !!!')
    break

  ## If a player enters the final room without all pokemon
  elif currentRoom == "Indigo Plateau":
    print("*** You were not ready to face the Elite Four or the current champion ***")
    print('*** YOU LOST... GAME OVER! ***')
    break
