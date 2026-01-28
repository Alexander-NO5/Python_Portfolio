# terminal_game
# World of Might and Magic

import random

# welcome message
print("Welcome to the world of Might and Magic! 🌍⚔️🪄")
print("Or for short WMM! 🌍⚔️🪄")

# ask user if they want to be reborn
answer = input("Are you ready to be reborn? (Yes/No) ")

while answer != "Yes" and answer != "No":
  answer = input("Please respond with Yes or No! No need to chit chat for now! ")

# if user wants to be reborn proceed with character creation
if answer == "Yes":
  print("Congratulations! You are now reborn in the world of Might and Magic! 🎉")
  print("Welcome to your new life adventurer! 🏰🗡️🪄")
  print("----------------------------------------------------------------------")
  print("Before we begin, let's set up your character! 🧙‍♂️")
  print("First, let the system know your name! 📝")

# get adventurer name
  adventurer_name = input("Enter your name: ")
  print("----------------------------------------------------------------------")
  print(f"Welcome {adventurer_name}! Your adventure awaits! 🏰🗡️🪄")
  print("----------------------------------------------------------------------")      

# choose character class
  print("Now, let's choose your class! 🛡️⚔️🪄")
  print("1) Warrior 🛡️ - Strong and brave fighters.")
  print("2) Mage 🪄 - Masters of magical arts.")
  print("3) Rogue ⚔️ - Stealthy and cunning adventurers.")
  print("----------------------------------------------------------------------")
  print("Each class has its own unique abilities and playstyle. Choose wisely! 🤔")

# offer more info about each class
  class_info_response = input("Would you like to know more about each class? (Yes/No) ")
  while class_info_response != "Yes" and class_info_response != "No":
    class_info_response = input("Please respond with Yes or No! No need to chit chat for now! ")
  if class_info_response == "Yes":
    print("Warrior 🛡️: Warriors are the frontline fighters, excelling in melee combat and defense. They have high strength and constitution, making them durable in battle. 💪")
    print("As a Warrior, your starting skills are: Slash, Multy Strike & Shield Block.")
    print("Mage 🪄: Mages wield powerful spells to attack enemies and support allies. They have high intelligence and mana, allowing them to cast devastating magic. 🔮")
    print("As a Mage, your starting skills are: Fireball, Ice Spikes & Heal.")
    print("Rogue ⚔️: Rogues are masters of stealth and agility. They excel in sneaking, lockpicking, and dealing critical damage from the shadows. 🗡️")
    print("As a Rogue, your starting skills are: Backstab, Multi Shot & Evasion.")
    print("----------------------------------------------------------------------")
  else:
    print("No worries! You can always learn more about your class as you play. 😊")
    print("----------------------------------------------------------------------")

# choose class
  class_choice = input("Choose your class (1-3): ")
  while class_choice != "1" and class_choice != "2" and class_choice != "3":
    class_choice = input("Please choose a valid class (1-3): ")
  if class_choice == "1":
    character_class = "Warrior"
    print("You have chosen the Warrior class! 🛡️💪")
    print("Get ready to wield your sword and shield in epic battles! ⚔️🛡️")
    print("📜 Your starting attributes are:")
    print("    Strength: 15")
    print("    Dexterity: 5")
    print("    Intelligence: 5")
    print("    Constitution: 15")
    print("    Charisma: 8")
    print("    Luck: 7")
    print("----------------------------------------------------------------------")
    Strength = 15
    Dexterity = 5
    Intelligence = 5
    Constitution = 15
    Charisma = 8
    Luck = 7
  elif class_choice == "2":
    character_class = "Mage"
    print("You have chosen the Mage class! 🪄🔮")
    print("Prepare to unleash powerful spells and magical abilities! ✨🪄")
    print("📜 Your starting attributes are:")
    print("    Strength: 5")
    print("    Dexterity: 7")
    print("    Intelligence: 15")
    print("    Constitution: 8")
    print("    Charisma: 10")
    print("    Luck: 10")
    print("----------------------------------------------------------------------")
    Strength = 5
    Dexterity = 7
    Intelligence = 15
    Constitution = 8
    Charisma = 10
    Luck = 10
  elif class_choice == "3":
    character_class = "Rogue"
    print("You have chosen the Rogue class! ⚔️🗡️")
    print("Get ready to sneak through shadows and strike from the darkness! 🕵️‍♂️🗡️")
    print("📜 Your starting attributes are:")
    print("    Strength: 8")
    print("    Dexterity: 15")
    print("    Intelligence: 5")
    print("    Constitution: 10")
    print("    Charisma: 12")
    print("    Luck: 10")
    print("----------------------------------------------------------------------")
    Strength = 8
    Dexterity = 15
    Intelligence = 5
    Constitution = 10
    Charisma = 12
    Luck = 10

# battlecry input
  print("Now, let's give your character some personality! 🗣️")
  print("What is your battlecry? 🗡️🪄")
  battlecry = input("Write something that your character will say at the beginning of every battle! ")
  print("----------------------------------------------------------------------")
    
# bonus attributes distribution flags and info
  print(f"Great! You are a {character_class} named {adventurer_name}! 🏰🗡️🪄")
  print(f"And your battlecry is: '{battlecry}'! 🗣️")
  print("----------------------------------------------------------------------")
  print("Now, let's determine your bonus attributes! 🎲📜")
  print("What are bonus attributes? 🤔")
  print("Bonus attributes are additional points that enhance your character's abilities beyond the starting attributes. They can give you an edge in combat, magic, stealth, and more! 💪🪄🗡️")
  print("You can distribute these bonus attributes to further customize your character and make them truly unique! 🌟")
  print("----------------------------------------------------------------------")
  print("You will roll 6d5 to determine your bonus attributes. 🎲")
  print("Keep in mind, higher the roll, better the attribute! 💪")
  print("The system likes you! You get a re-roll if you get less than 10! 🔄")
  print("----------------------------------------------------------------------")
  answer = input("Are you ready to roll for your bonus attributes? (Roll) ")
  while answer != "Roll":
    answer = input("Please Roll the dice! No need to chit chat for now!")
  print("Rolling your bonus attributes now... 🎲🎲🎲🎲🎲🎲")

  stat1 = 0
  stat2 = 0
  stat3 = 0
  stat4 = 0
  stat5 = 0
  stat6 = 0

  lowstat = 0

  TotalStats = stat1 + stat2 + stat3 + stat4 + stat5 + stat6 
  
  while TotalStats < 10:

    lowstat = lowstat + 1

    stat1 = random.randint(1, 5)
    stat2 = random.randint(1, 5)
    stat3 = random.randint(1, 5)
    stat4 = random.randint(1, 5)
    stat5 = random.randint(1, 5)
    stat6 = random.randint(1, 5)

    TotalStats = stat1 + stat2 + stat3 + stat4 + stat5 + stat6  
    
  if lowstat == 1:
    print("You are very lucky! You got good stats first try! 🍀")
  elif lowstat < 3:
    lowstat = lowstat - 1
    print(f"You are quite lucky you got good bonus attributes in {lowstat} re-rolls! 🍀")
  elif lowstat <= 5:
    lowstat = lowstat - 1
    print(f"You are a bit unlucky you got good bonus attributes in {lowstat} re-rolls! 🍀")
  elif lowstat < 10:
    lowstat = lowstat - 1
    print(f"You are unlucky you got good bonus attributes in {lowstat} re-rolls! 🍀")
  elif lowstat >= 10:
    lowstat = lowstat - 1
    print(f"You are very unlucky you got good bonus sattributes in {lowstat} re-rolls! 🍀")

  print("----------------------------------------------------------------------")
  print("Your bonus attributes rolls are: ")
  print(f"Roll 1: {stat1}") 
  print(f"Roll 2: {stat2}")
  print(f"Roll 3: {stat3}")
  print(f"Roll 4: {stat4}")   
  print(f"Roll 5: {stat5}")
  print(f"Roll 6: {stat6}")
  print("----------------------------------------------------------------------")

  print("Let's add these bonus attributes to your starting attributes! 📜➕📜")
  print("Where do you want to assign these bonus attributes? 🤔")

  stat1_distribution = input("Where do you want to assign Roll 1? ")
  while stat1_distribution != "Strength" and stat1_distribution != "Dexterity" and stat1_distribution != "Intelligence" and stat1_distribution != "Constitution" and stat1_distribution != "Charisma" and stat1_distribution != "Luck":
    stat1_distribution = input("Please choose a valid attribute (Strength, Dexterity, Intelligence, Constitution, Charisma, Luck): ")
  if stat1_distribution == "Strength":
    Strength = Strength + stat1
    used_strength = True
  elif stat1_distribution == "Dexterity":
    Dexterity = Dexterity + stat1
    used_dexterity = True
  elif stat1_distribution == "Intelligence":
    Intelligence = Intelligence + stat1
    used_intelligence = True
  elif stat1_distribution == "Constitution":
    Constitution = Constitution + stat1
    used_constitution = True
  elif stat1_distribution == "Charisma":
    Charisma = Charisma + stat1
    used_charisma = True
  elif stat1_distribution == "Luck":
    Luck = Luck + stat1
    used_luck = True

  stat2_distribution = input("Where do you want to assign Roll 2? ")
  while stat2_distribution != "Strength" and stat2_distribution != "Dexterity" and stat2_distribution != "Intelligence" and stat2_distribution != "Constitution" and stat2_distribution != "Charisma" and stat2_distribution != "Luck":
    stat2_distribution = input("Please choose a valid attribute (Strength, Dexterity, Intelligence, Constitution, Charisma, Luck): ")
  while stat2_distribution == stat1_distribution:
    stat2_distribution = input("You have already assigned a roll to that attribute. Please choose a different attribute: ")
  if stat2_distribution == "Strength":
    Strength = Strength + stat2
  elif stat2_distribution == "Dexterity":
    Dexterity = Dexterity + stat2
  elif stat2_distribution == "Intelligence":
    Intelligence = Intelligence + stat2
  elif stat2_distribution == "Constitution":
    Constitution = Constitution + stat2
  elif stat2_distribution == "Charisma":
    Charisma = Charisma + stat2
  elif stat2_distribution == "Luck":
    Luck = Luck + stat2

  stat3_distribution = input("Where do you want to assign Roll 3? ")
  while stat3_distribution != "Strength" and stat3_distribution != "Dexterity" and stat3_distribution != "Intelligence" and stat3_distribution != "Constitution" and stat3_distribution != "Charisma" and stat3_distribution != "Luck":
    stat3_distribution = input("Please choose a valid attribute (Strength, Dexterity, Intelligence, Constitution, Charisma, Luck): ")
  while stat3_distribution == stat1_distribution or stat3_distribution == stat2_distribution:
    stat3_distribution = input("You have already assigned a roll to that attribute. Please choose a different attribute: ")
  if stat3_distribution == "Strength":
    Strength = Strength + stat3
  elif stat3_distribution == "Dexterity":
    Dexterity = Dexterity + stat3
  elif stat3_distribution == "Intelligence":
    Intelligence = Intelligence + stat3
  elif stat3_distribution == "Constitution":
    Constitution = Constitution + stat3
  elif stat3_distribution == "Charisma":
    Charisma = Charisma + stat3
  elif stat3_distribution == "Luck":
    Luck = Luck + stat3

  stat4_distribution = input("Where do you want to assign Roll 4? ")
  while stat4_distribution != "Strength" and stat4_distribution != "Dexterity" and stat4_distribution != "Intelligence" and stat4_distribution != "Constitution" and stat4_distribution != "Charisma" and stat4_distribution != "Luck":
    stat4_distribution = input("Please choose a valid attribute (Strength, Dexterity, Intelligence, Constitution, Charisma, Luck): ")
  while stat4_distribution == stat1_distribution or stat4_distribution == stat2_distribution or stat4_distribution == stat3_distribution:
    stat4_distribution = input("You have already assigned a roll to that attribute. Please choose a different attribute: ")
  if stat4_distribution == "Strength":
    Strength = Strength + stat4
  elif stat4_distribution == "Dexterity":
    Dexterity = Dexterity + stat4
  elif stat4_distribution == "Intelligence":
    Intelligence = Intelligence + stat4
  elif stat4_distribution == "Constitution":
    Constitution = Constitution + stat4
  elif stat4_distribution == "Charisma":
    Charisma = Charisma + stat4
  elif stat4_distribution == "Luck":
    Luck = Luck + stat4

  stat5_distribution = input("Where do you want to assign Roll 5? ")
  while stat5_distribution != "Strength" and stat5_distribution != "Dexterity" and stat5_distribution != "Intelligence" and stat5_distribution != "Constitution" and stat5_distribution != "Charisma" and stat5_distribution != "Luck":
    stat5_distribution = input("Please choose a valid attribute (Strength, Dexterity, Intelligence, Constitution, Charisma, Luck): ")
  while stat5_distribution == stat1_distribution or stat5_distribution == stat2_distribution or stat5_distribution == stat3_distribution or stat5_distribution == stat4_distribution:
    stat5_distribution = input("You have already assigned a roll to that attribute. Please choose a different attribute: ")
  if stat5_distribution == "Strength":
    Strength = Strength + stat5
  elif stat5_distribution == "Dexterity":
    Dexterity = Dexterity + stat5
  elif stat5_distribution == "Intelligence":
    Intelligence = Intelligence + stat5
  elif stat5_distribution == "Constitution":
    Constitution = Constitution + stat5
  elif stat5_distribution == "Charisma":
    Charisma = Charisma + stat5
  elif stat5_distribution == "Luck":
    Luck = Luck + stat5

  stat6_distribution = input("Where do you want to assign Roll 6? ")
  while stat6_distribution != "Strength" and stat6_distribution != "Dexterity" and stat6_distribution != "Intelligence" and stat6_distribution != "Constitution" and stat6_distribution != "Charisma" and stat6_distribution != "Luck":
    stat6_distribution = input("Please choose a valid attribute (Strength, Dexterity, Intelligence, Constitution, Charisma, Luck): ")
  while stat6_distribution == stat1_distribution or stat6_distribution == stat2_distribution or stat6_distribution == stat3_distribution or stat6_distribution == stat4_distribution or stat6_distribution == stat5_distribution:
    stat6_distribution = input("You have already assigned a roll to that attribute. Please choose a different attribute: ")
  if stat6_distribution == "Strength":
    Strength = Strength + stat6
  elif stat6_distribution == "Dexterity":
    Dexterity = Dexterity + stat6
  elif stat6_distribution == "Intelligence":
    Intelligence = Intelligence + stat6
  elif stat6_distribution == "Constitution":
    Constitution = Constitution + stat6
  elif stat6_distribution == "Charisma":
    Charisma = Charisma + stat6
  elif stat6_distribution == "Luck":
    Luck = Luck + stat6

  if class_choice == "1":
    Health = 100 + (Constitution * 5)
    # Mana = 30 + (Intelligence * 2)
  elif class_choice == "2":
    Health = 70 + (Constitution * 3)
    # Mana = 100 + (Intelligence * 5)
  elif class_choice == "3":
    Health = 80 + (Constitution * 4)
    # Mana = 50 + (Intelligence * 3)

# final stats display & starting skills display
  print("----------------------------------------------------------------------")
  print("Here are your final stats: 📜")  
  print(f"Strength: {Strength}")
  print(f"Dexterity: {Dexterity}")
  print(f"Intelligence: {Intelligence}")
  print(f"Constitution: {Constitution}")
  print(f"Charisma: {Charisma}")
  print(f"Luck: {Luck}")
  print("----------------------------------------------------------------------")
  print(f"Health: {Health} ❤️") # | Mana: {Mana} 🔮")
  print("----------------------------------------------------------------------")
  if class_choice == "1":
    slash_damage = 10 + (Strength // 2)
    multy_strike_damage = 5 + (Strength // 3)
    shield_block_amount = 10 + (Constitution // 4) + (Dexterity // 4)
    print("Your starting skills are: ")
    print(f"Slash 🗡️ - Deals {slash_damage} damage to an enemy.")
    print(f"Multy Strike ⚔️ - Deals {multy_strike_damage} damage multiple times to an enemies.")
    print(f"Shield Block 🛡️ - Blocks {shield_block_amount} damage from the next attack.")
  elif class_choice == "2":
    fireball_damage = 12 + (Intelligence // 2)
    ice_spikes_damage = 8 + (Intelligence // 3)
    heal_amount = 10 + (Intelligence // 4) + (Constitution // 4)
    print("Your starting skills are: ")
    print(f"Fireball 🔥 - Deals {fireball_damage} damage to an enemy.")
    print(f"Ice Spikes ❄️ - Deals {ice_spikes_damage} damage multiple times to an enemies.")
    print(f"Heal ✨ - Restores {heal_amount} health to yourself.")
  elif class_choice == "3":
    backstab_damage = 15 + (Dexterity // 2)
    multi_shot_damage = 7 + (Dexterity // 3)
    evasion_chance = 10 + (Dexterity // 2) + (Luck // 2)
    print("Your starting skills are: ")
    print(f"Backstab 🗡️ - Deals {backstab_damage} damage to an enemy from behind.")
    print(f"Multi Shot 🎯 - Deals {multi_shot_damage} damage multiple times to an enemies.")
    print(f"Evasion 🌪️ - Increases your chance to dodge the next attack by {evasion_chance}%.")

# ready to begin adventure
  print("----------------------------------------------------------------------")
  answer = input("Are you ready to begin your adventure? (Yes) ")
  while answer != "Yes":
    answer = input("Please respond with Yes! No need to chit chat for now! ")
  print("Let the adventure begin!")
  print("----------------------------------------------------------------------")
  
  print(f"As you step into the world of Might and Magic, you feel a surge of excitement. Your journey as a {character_class} named {adventurer_name} is about to unfold! 🏰🗡️🪄")
  print("You wake up in a cave, the air is damp and the sound of dripping water echoes around you. You see a faint light coming from the entrance of the cave. 🌄")
  print("Still the exit is far away, you need to get there! 🏃‍♂️")
  print("As you make your way towards the light, you hear a growl coming from the shadows. Suddenly, a wild goblin jumps out in front of you! 🐉")
  print("What will you do? 🤔")
  answer = input("Type 'Fight' to engage the goblin in battle or 'Befriend' if you think you can get out without a fight: ")
  while answer != "Fight" and answer != "Befriend":
    answer = input("Please respond with Fight or Befriend! No need to chit chat for now! ")
  if answer == "Fight":
    print("You bravely draw your weapon and prepare to fight the goblin! ⚔️🛡️")
    print(battlecry)

    goblin_Strength = 8
    goblin_dexterity = 10
    goblin_intelligence = 4
    goblin_constitution = 6
    goblin_health = 50 + (goblin_constitution * 4)

    print("----------------------------------------------------------------------")
    print(f"Cave Goblin")
    print(f"Strength: {goblin_Strength}")
    print(f"Dexterity: {goblin_dexterity}")
    print(f"Intelligence: {goblin_intelligence}")
    print(f"Constitution: {goblin_constitution}")
    print(f"Health: {goblin_health} ❤️")
    print("----------------------------------------------------------------------")
    print(f"{adventurer_name} the {character_class}!")
    print(f"Strength: {Strength}")
    print(f"Dexterity: {Dexterity}")
    print(f"Intelligence: {Intelligence}")
    print(f"Constitution: {Constitution}")
    print(f"Charisma: {Charisma}")
    print(f"Luck: {Luck}")
    print(f"Health: {Health} ❤️") # | Mana: {Mana} 🔮")
    if class_choice == "1":
      print("Skills: Slash, Multy Strike & Shield Block.")
    elif class_choice == "2": 
      print("Skills: Fireball, Ice Spikes & Heal.")
    elif class_choice == "3":
      print("Skills: Backstab, Multi Shot & Evasion.")
    print("----------------------------------------------------------------------")

# Battle loop for Warrior
    if class_choice == "1":
      while Health > 0 and goblin_health > 0:
        player_move = input("Choose a skill to use: ")
        while player_move != "Slash" and player_move != "Multy Strike" and player_move != "Shield Block":
          player_move = input("Please choose a valid skill! ")
        print(f"You used {player_move}!")
        if player_move == "Slash":
          goblin_health = goblin_health - slash_damage
          print(f"You dealt {slash_damage} damage to the goblin! Goblin's remaining health: {goblin_health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")
        elif player_move == "Multy Strike":
          for strike in range(Luck // 3):
            goblin_health = goblin_health - multy_strike_damage
            print(f"You dealt {multy_strike_damage} damage to the goblin! Goblin's remaining health: {goblin_health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")
        elif player_move == "Shield Block":
          print("You brace yourself for the goblin's attack!")
          goblin_atack = 15 + (goblin_Strength // 2)
          blocked_amount = shield_block_amount
          damage_taken = goblin_atack - blocked_amount
          if damage_taken < 0:
            damage_taken = 0
          Health = Health - damage_taken
          print(f"The goblin attacks and deals {goblin_atack} damage, but you block {blocked_amount}! You take {damage_taken} damage. Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")

# Battle loop for Mage
    elif class_choice == "2":
      while Health > 0 and goblin_health > 0:
        player_move = input("Choose a skill to use: ")
        while player_move != "Fireball" and player_move != "Ice Spikes" and player_move != "Heal":
          player_move = input("Please choose a valid skill! ")
        print(f"You used {player_move}!")
        if player_move == "Fireball":
          goblin_health = goblin_health - fireball_damage
          print(f"You dealt {fireball_damage} damage to the goblin! Goblin's remaining health: {goblin_health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")
        elif player_move == "Ice Spikes":
          for spike in range(Luck // 3):
            goblin_health = goblin_health - ice_spikes_damage
            print(f"You dealt {ice_spikes_damage} damage to the goblin! Goblin's remaining health: {goblin_health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")
        elif player_move == "Heal":
          Health = Health + heal_amount
          print(f"You healed yourself for {heal_amount}! Your current health: {Health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")

# Battle loop for Rogue
    elif class_choice == "3":
      while Health > 0 and goblin_health > 0:
        player_move = input("Choose a skill to use: ")
        while player_move != "Backstab" and player_move != "Multi Shot" and player_move != "Evasion":
          player_move = input("Please choose a valid skill! ")
        print(f"You used {player_move}!")
        if player_move == "Backstab":
          goblin_health = goblin_health - backstab_damage
          print(f"You dealt {backstab_damage} damage to the goblin! Goblin's remaining health: {goblin_health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")
        elif player_move == "Multi Shot":
          for shot in range(Luck // 3):
            goblin_health = goblin_health - multi_shot_damage
            print(f"You dealt {multi_shot_damage} damage to the goblin! Goblin's remaining health: {goblin_health} ❤️")
          goblin_atack = 15 + (goblin_Strength // 2)
          Health = Health - goblin_atack
          print(f"The goblin attacks back and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
          print("----------------------------------------------------------------------")
        elif player_move == "Evasion":
          print("You prepare to dodge the goblin's next attack!")
          goblin_atack = 15 + (goblin_Strength // 2)
          dodge_roll = random.randint(1, 100)
          if dodge_roll <= evasion_chance:
            print("You successfully dodged the goblin's attack! No damage taken!")
          else:
            Health = Health - goblin_atack
            print(f"The goblin attacks and deals {goblin_atack} damage to you! Your remaining health: {Health} ❤️")
            print("----------------------------------------------------------------------")

  elif answer == "Befriend":
    answer = input("Write a friendly message to the goblin to try and befriend it: ")
    print("You attempt to befriend the goblin! 🐉🤝")
    print(f'You say to the goblin: "{answer}"')
    charisma_check = Charisma + random.randint(1, 20)
    if charisma_check > 15:
      print("Your charm works! The goblin decides to befriend you instead of fighting! 🎉")
      print("The goblin joins your party as a companion! 🐉👫")
    else:
      print("The goblin is not convinced by your attempt to befriend it. It attacks you instead! ⚔️")
      print("You were unprepared so you died... ☠️")
      # Here will implement a battle sequence similar to the one above.

  if Health > 0 and answer == "Fight":
    print("🎉 You have defeated the goblin! Congratulations on your first victory! 🎉")
    print("You gain 20 experience points and find a small pouch of gold on the goblin. 💰")
    print("Good luck on your adventure ahead! 🏰🗡️🪄")
    print("----------------------------------------------------------------------")
  elif answer == "Befriend" and charisma_check >15:
    print("🎉 You have successfully befriended the goblin! Congratulations on making a new ally! 🎉")
    print("The goblin shares some of its knowledge about the cave and gives you a small pouch of gold. 💰")
    print("Good luck on your adventure ahead with your new companion! 🏰🗡️🪄")
    print("----------------------------------------------------------------------")
  elif answer == "Befriend" and charisma_check <= 15:
    print("✨ Rest in peace dear soul! ✨")
    print("☠️  Game Over! ☠️")
    print("----------------------------------------------------------------------")
  elif Health <= 0:
    print("✨ Rest in peace dear soul! ✨")
    print("☠️  Game Over! ☠️")
    print("----------------------------------------------------------------------")

elif answer == "No":
  print("✨ Rest in peace dear soul! ✨")
  print("☠️  Game Over! ☠️")
  print("----------------------------------------------------------------------")
