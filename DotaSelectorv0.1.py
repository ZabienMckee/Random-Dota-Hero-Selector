import random
import time
hero = str(input('''What type of hero do you want to play?

[1] - Carry
[2] - Support
[3] - Ganker
[4] - Disabler
[5] - Durable
[6] - initiator
[7] - Pusher
[8] - Nuker
[9] - Any

[0] - Help/About
'''))
if hero == '1':
    herolist = ['Mars','AntiMage', 'Kunka', 'Storm Spirit', 'Alchemist', 'Bristleback', 'Chaos Knight', 'Dragon Knight', 'Huskar', 'Life Stealer', 'Lycan', 'Slardar', 'Sven', 'Tiny', 'Wraith King', 'Arc Warden', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Juggernaut', 'Lone Druid', ' Luna', 'Medusa', 'Meepo', 'Monkey King', 'Morphling', 'Naga Siren', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Razor', 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Weaver', 'Outworld Devourer']
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '2':
    herolist = ['Abaddon', 'IO', 'Omni Knight', 'Treant Protector', 'Vengeful Spirit', 'Venomancer', 'Ancient Apparition', 'Bane', 'Chen', 'Crystal Maiden', 'Dark Willow', 'Dazzle', 'Disruptor', 'Enchantress', ' Keeper of the Light', 'Lich', 'Lion', 'Ogre Magi', 'Oracle', 'Rubick', 'Shadow Demon', 'Shadow Shaman', 'Skywrath Mage', 'Winter Wyvern', 'Witch Doctor']
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '3':
    herolist = ['Alchemist', 'Batrider', 'Beastmaster', 'Bloodseeker', 'Bounty Hunter', 'Clockwerk', 'Chaos Knight', 'Clinkz', 'Doom', 'Ember Spirit', 'Enchantress', 'Invoker', 'Kunka', 'Mirana', 'Nature\'s Prophet', 'Necrophose', 'Night Stalker', 'Nyx Assassin', 'Pudge', 'Queen of Pain', 'Shadow Demon', 'Slark', 'Spirit Breaker', 'Storm Spirit', 'NULLPOINTEREXCEPTION hero "Techies" is too bullshit to be selected Error(21389) ', 'Tinker', 'Timbersaw']
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '4':
    herolist = ['Axe', 'Beastmaster', 'Brewmaster', 'Chaos Knight', 'Clockwerk', 'Doom' 'Dragon Knight', 'Earth Shaker', 'Kunka', 'Legion Commander', 'Magnus', 'Night Stalker', 'Pudge', 'Spirit Breaker', 'Sand King', 'Sven', 'Tide Hunter', 'Tusk', 'Wraith King', 'Faceless Void', 'Naga Siren', 'Nyx Assassin', 'Vengeful Spirit', 'Bane', 'batrider', 'Crystal Maiden ', 'Disruptor', 'Enigma', 'Grimstroke', 'Invoker', 'Lion', 'Ogre Magi', 'Puck', 'Shadow Demon', 'Silencer', 'Winter Wyvern' ]
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '5':
    herolist = ['Mars', 'Abaddon', 'Alchemist', 'Beastmaster', 'Bristleback', 'Centaur Warrunner', 'Chaos Knight', 'Doom', 'Dragon Knight', 'Huskar', 'Life Stealer', 'Night Stalker', 'Pudge', 'Slardar', 'Spirit Breaker', 'Sven', 'Tide Hunter', 'Timbersaw', 'Tiny', 'Undying', 'Wraith King', 'Razpr', 'Morphling', 'Viper']
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '6':
    herolist = ['Axe', 'beastmaster', 'Centuar Warrunner', 'Brew Master,' 'Clockwerk', 'Doom', 'Earth Shaker', 'Elder Titan', 'Kunka', 'Magnus', 'Night Stalker', 'Pheonix', 'Pudge', 'Sand King', 'Slardar', 'Spirit Breaker', 'Sven', 'Tide Hunter', 'Tiny', 'Treant Protector', 'Tusk', 'Faceless Void', 'Nyx Assassin', 'Pangolier', 'Vengeful Spirit', 'Batrider', 'Enigma', 'Lion', 'Puck', 'Silencer', 'Warlock']
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '7':
    herolist = ['Chaos Knight', 'Dragon Knight', 'Lycan', 'Tiny', 'Brood Mother', 'Lone Druid', 'Naga Siren', 'Terrorblade', 'Troll Warlord', 'Chen', 'Death Prophet', 'Enchantress', 'Enigma', 'Jakiro', 'Leshrac', 'Nature\'s Prophet', 'Pugna', 'Shadow Shaman', 'Tinker']
    print("~~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~")
    print (random.choice(herolist))
elif hero == '8':
    herolist = ['Earth Spirit', 'Pheonix', 'Sand King', 'Timbersaw', 'Tiny', 'Luna', 'Meepo', 'Nyx assassin', 'Pangolier', 'Shadow Demon', 'Crystal Maiden', 'Dark Willow', 'Grimstroke', 'Invoker', 'Jakiro', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Necrophos', 'Ogre Magi', 'Oracle', 'Outworld Devourer', ' Puck', 'Pugna', 'Queen of Pain', 'Shadow Shaman', 'Skywrath Mage', 'Storm Spirit', 'NULLPOINTEREXCEPTION hero Techies is too bullshit to be played Error(23490)', 'Tinker', 'Visage', 'Witch Doctor', 'Zues']
    print("~~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~")
    print (random.choice(herolist))
elif hero == '9':
    herolist = ['Abaddon', 'Alchemist', 'Axe', 'Beastmaster', 'Brewmaster', 'Bristleback', 'Centuar Warrunner', 'Chaos Knight', 'Clockwerk', 'Doom', 'Dragon Knight', 'Earth Spirit', 'Earth Shaker', 'Elder Titan', 'Huskar', 'IO', 'Kunka', 'Legion Commander', 'Life Stealer', 'Lycan', 'Magnus', 'Night Stalker', 'OmniKnight', 'Pheonix', 'Pudge', 'Sand King', 'Slardar', 'Spirit Breaker', 'Sven', 'TideHunter', 'Timbersaw', 'Tiny', 'Tusk', 'Treant Protector', 'Underlord', 'Undying', 'Wraith King', 'Antimage', 'Arc Wsarden', 'Blood Seeker', 'Bountry Huter', 'Brood Mother', 'Clinkz', 'Drow Ranger', 'Ember Spirit', 'Faceless Void', 'Gyrocopter', 'Juggermaut', 'Lone Druid', 'Luna', 'Medusa', 'Meepo', 'Mirana', 'Monkey King', 'Morphling', 'Naga Siren', 'Nyx Assassin', 'Pangolier', 'Phantom Assassin', 'Phantom Lancer', 'Razor,' 'Riki', 'Shadow Fiend', 'Slark', 'Sniper', 'Spectre', 'Templar Assassin', 'Terrorblade', 'Troll Warlord', 'Ursa', 'Vengeful Spirit', 'Venomancer', 'Viper', 'Weaver', 'Ancient Apparition', 'Bane', 'Batrider', 'Chen', 'Crystal Maiden', 'Dark Seer', 'Dark Willow', 'Dazzle', 'Death Prophet', 'Disruptor', 'Enchantress', 'Engima', 'Grimstroke', 'Invoker', 'Jakrio', 'Keeper of the Light', 'Leshrac', 'Lich', 'Lina', 'Lion', 'Nature\'s Prophet', 'Necrophose', 'Ogre Magi', 'Oracle', 'Outworld Devourer', 'Puck', 'Pugna', 'Queen of Pain', 'Rubick', 'Shadow Demon', 'Shadow Shaman', 'Silencer', 'Skywrath Mage', 'Storm Spirit', 'Techies', 'Tinker', 'Visage', 'Warlock', 'Wind Ranger', 'Winter Wyvern', 'Witch Doctor', ' Zues']
    selection = (random.choice(herolist))
    print("~~~~~~~~~ YOUR HERO IS ~~~~~~~~~~~~~")
    print(selection)
elif hero == '0':
	print('''		Random Dota Character Selector (RDCS) v0.1
				Program written on 3/1/2019
				powered by Python3''')
