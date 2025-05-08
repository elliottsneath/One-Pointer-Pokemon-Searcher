import json

list = [
		"Alolan Raticate", "Camerupt", "Barbaracle", "Alolan Golem", "Alolan Exeggutor", "Aurorus", "Crabominable", "Arbok", "Alolan Dugtrio", "Altaria", "Beheeyem", "Ariados", "Aggron", "Banette", "Alolan Exeggutor", "Absol", "Aggron", "Carbink", "Bibarel", "Flareon",
		"Bibarel", "Ampharos", "Bellossom", "Beartic", "Falinks", "Ariados", "Camerupt", "Beautifly", "Bruxish", "Armaldo", "Alolan Golem", "Cursola", "Altaria", "Alolan Raticate", "Alolan Dugtrio", "Dedenne", "Castform", "Heatmor", "Bruxish", "Dedenne", "Cacturne", "Crabominable",
		"Grapploct", "Beedrill", "Galarian Stunfisk", "Butterfree", "Calyrex", "Beautifly", "Armaldo", "Dusknoir", "Flapple", "Cacturne", "Bastiodon", "Galarian Rapidash", "Chatot", "Houndoom", "Carracosta", "Electivire", "Calyrex", "Delibird", "Medicham", "Dustox", "Golem", "Chatot",
		"Chimecho", "Beedrill", "Aurorus", "Shedinja", "Tatsugiri", "Honchkrow", "Galarian Stunfisk", "Mawile", "Delcatty", "Magcargo", "Corsola", "Electrode", "Carnivine", "Dewgong", "Poliwrath", "Seviper", "Marowak", "Cramorant", "Exeggutor", "Butterfree", "Barbaracle", "Spiritomb",
		"Turtonator", "Houndoom", "Klinklang", "Mr. Mime", "Dodrio", "Pyroar", "Cramorant", "Emolga", "Cherrim", "Eiscue", "Sawk", "Swalot", "Whiscash", "Delibird", "Galarian Rapidash", "Dustox", "Bastiodon", "Trevenant", "Liepard", "Mawile", "Shiinotic", "Dubwool", "Rapidash",
		"Dewgong", "Luxray", "Exeggutor", "Frosmoth", "Throh", "Victreebel", "Dodrio", "Grumpig", "Frosmoth", "Carbink", "Malamar", "Meltan", "Dunsparce", "Simisear", "Golduck", "Manectric", "Flapple", "Glalie", "Emolga", "Hypno", "Illumise", "Carracosta", "Mightyena", "Perrserker",
		"Exploud", "Turtonator", "Gorebyss", "Minun", "Gogoat", "Hisuian Avalugg", "Farfetch'd", "Jynx", "Kricketune", "Corsola", "Morpeko", "Probopass", "Farfetch'd", "Huntail", "Morpeko", "Jumpluff", "Jynx", "Fearow", "Lunatone", "Leavanny", "Golem", "Shiftry", "Togedemaru", "Fearow",
		"Kabutops", "Pachirisu", "Leafeon", "Lapras", "Honchkrow", "Malamar", "Ledian", "Hisuian Avalugg", "Spiritomb", "Furfrou", "Kingler", "Plusle", "Leavanny", "Mr. Rime", "Jumpluff", "Medicham", "Masquerain", "Kabutops", "Thievul", "Furret", "Lapras", "Togedemaru", "Lilligant",
		"Walrein", "Ledian", "Meowstic", "Mothim", "Klawf", "Greedent", "Lumineon", "Zebstrika", "Lurantis", "Masquerain", "Mr. Mime", "Ninjask", "Lunatone", "Gumshoos", "Luvdisc", "Maractus", "Mothim", "Mr. Rime", "Orbeetle", "Lycanrock Midnight", "Kecleon", "Octillery", "Meganium",
		"Ninjask", "Musharna", "Parasect", "Magcargo", "Linoone", "Phione", "Parasect", "Noctowl", "Oranguru", "Pinsir", "Probopass", "Lopunny", "Poliwrath", "Sawsbuck", "Pidgeot", "Orbeetle", "Rabsca", "Rampardos", "Noctowl", "Pyukumuku", "Shiftry", "Squawkabilly", "Rabsca", "Shedinja",
		"Relicanth", "Oinkologne", "Relicanth", "Shiinotic", "Swanna", "Solrock", "Shuckle", "Shuckle", "Oranguru", "Samurott", "Simisage", "Swoobat", "Swoobat", "Spidops", "Solrock", "Persian", "Seaking", "Sunflora", "Toucannon", "Unown", "Vespiquen", "Stonjourner", "Pidgeot",
		"Simipour", "Trevenant", "Tropius", "Veluza", "Vivillon", "Sudowoodo", "Purugly", "Swanna", "Tropius", "Unfezant", "Wobbuffet", "Volbeat", "Pyroar", "Tatsugiri", "Victreebel", "Vespiquen", "Wyrdeer", "Wormadam", "Raticate", "Veluza", "Wormadam", "Xatu", "Xatu", "Regigigas",
		"Wailord", "Sawsbuck", "Walrein", "Slaking", "Whiscash", "Spinda", "Wugtrio", "Squawkabilly", "Toucannon", "Unfezant", "Watchog", "Wyrdeer", "Zangoose", "Aipom", "Braixen", "Arrokuda", "Alolan Geodude", "Applin", "Alolan Sandshrew", "Clobbopus", "Alolan Grimer", "Alolan Diglett",
		"Archen", "Abra", "Anorith", "Alolan Geodude", "Bramblin", "Applin", "Alolan Grimer", "Alolan Diglett", "Azurill", "Alolan Rattata", "Carkol", "Barboach", "Alolan Graveler", "Bayleef", "Alolan Vulpix", "Combusken", "Bellsprout", "Baltoy", "Combee", "Baltoy", "Blipbug",
		"Alolan Graveler", "Drakloak", "Arctibax", "Alolan Meowth", "Alolan Sandshrew", "Clefairy", "Azurill", "Charcadet", "Binacle", "Blitzle", "Bellsprout", "Amaura", "Crabrawler", "Budew", "Barboach", "Corvisquire", "Beldum", "Burmy", "Amaura", "Dreepy", "Axew", "Alolan Rattata",
		"Aron", "Cleffa", "Bidoof", "Charmander", "Brionne", "Charjabug", "Bounsweet", "Arctibax", "Croagunk", "Bulbasaur", "Cubone", "Dartrix", "Bronzor", "Cascoon", "Anorith", "Drifloon", "Bagon", "Bunnelby", "Beldum", "Cottonee", "Buneary", "Charmeleon", "Buizel", "Chinchou",
		"Bramblin", "Bergmite", "Galarian Farfetch'd", "Croagunk", "Diglett", "Doduo", "Chingling", "Caterpie", "Archen", "Dusclops", "Deino", "Carvanha", "Bronzor", "Cutiefly", "Deerling", "Chimchar", "Bunnelby", "Eelektrik", "Budew", "Cetoddle", "Hakamo-o", "Ekans", "Drilbur",
		"Drifloon", "Cosmoem", "Charjabug", "Aron", "Duskull", "Dipplin", "Deino", "Cufant", "Fidough", "Doduo", "Combusken", "Carvanha", "Electabuzz", "Bulbasaur", "Cubchoo", "Hisuian Sneasel", "Foongus", "Fletchling", "Ducklett", "Cosmog", "Combee", "Binacle", "Frillish", "Dragonair",
		"Galarian Linoone", "Ferroseed", "Flabébé", "Dolliv", "Cyndaquil", "Chewtle", "Electrike", "Cacnea", "Frigibax", "Kubfu", "Gastly", "Gabite", "Fletchinder", "Dottler", "Cutiefly", "Boldore", "Galarian Yamask", "Drakloak", "Galarian Zigzagoon", "Galarian Meowth", "Floette",
		"Eevee", "Darumaka", "Chinchou", "Elekid", "Capsakid", "Galarian Darumaka", "Machoke", "Glimmet", "Galarian Yamask", "Hoothoot", "Drowzee", "Dewpider", "Bonsly", "Gastly", "Dratini", "Houndour", "Hisuian Sliggoo", "Igglybuff", "Fletchinder", "Fennekin", "Clamperl", "Flaaffy",
		"Cherubi", "Galarian Mr. Mime", "Machop", "Gloom", "Geodude", "Hoppip", "Duosion", "Dottler", "Carkol", "Gimmighoul", "Dreepy", "Impidimp", "Honedge", "Impidimp", "Fletchling", "Fuecoco", "Clauncher", "Helioptile", "Chespin", "Sealeo", "Makuhita", "Grimer", "Gible", "Ledyba",
		"Elgyem", "Dwebble", "Cranidos", "Golett", "Fraxure", "Inkay", "Klang", "Jigglypuff", "Galarian Linoone", "Growlithe", "Corphish", "Hisuian Voltorb", "Chikorita", "Smoochum", "Mankey", "Gulpin", "Golett", "Mantyke", "Espurr", "Grubbin", "Dwebble", "Greavard", "Frigibax",
		"Krokorok", "Klink", "Kirlia", "Galarian Zigzagoon", "Hisuian Growlithe", "Croconaw", "Joltik", "Cottonee", "Snom", "Meditite", "Haunter", "Graveler", "Murkrow", "Exeggcute", "Joltik", "Geodude", "Haunter", "Gabite", "Maschiff", "Lairon", "Marill", "Girafarig", "Houndour",
		"Dewott", "Luxio", "Dartrix", "Snorunt", "Mienfoo", "Hisuian Sneasel", "Hippopotas", "Natu", "Flittle", "Kakuna", "Glimmet", "Hisuian Zorua", "Gible", "Morgrem", "Magnemite", "Milcery", "Glameow", "Lampent", "Dewpider", "Magnemite", "Deerling", "Snover", "Monferno", "Ivysaur",
		"Krokorok", "Noibat", "Galarian Mr. Mime", "Karrablast", "Graveler", "Honedge", "Goomy", "Murkrow", "Metang", "Mime Jr.", "Happiny", "Larvesta", "Drizzile", "Mareep", "Dipplin", "Spheal", "Pancham", "Kakuna", "Larvitar", "Pidgeotto", "Galarian Ponyta", "Kricketot",
		"Hisuian Growlithe", "Lampent", "Hakamo-o", "Nickit", "Pawniard", "Morelull", "Helioptile", "Litleo", "Ducklett", "Pawmi", "Dolliv", "Swinub", "Pawmo", "Koffing", "Marshtomp", "Pidgey", "Galarian Slowpoke", "Larvesta", "Kabuto", "Litwick", "Hisuian Sliggoo", "Nuzleaf",
		"Shieldon", "Morgrem", "Herdier", "Litten", "Feebas", "Pawmo", "Exeggcute", "Vanillish", "Pignite", "Mareanie", "Mudbray", "Pidove", "Girafarig", "Ledyba", "Lairon", "Misdreavus", "Jangmo-o", "Pawniard", "Tinkatink", "Ralts", "Hisuian Zorua", "Litwick", "Finizen", "Pichu",
		"Ferroseed", "Vanillite", "Riolu", "Nidoran♀", "Nincada", "Pikipek", "Gothita", "Metapod", "Larvitar", "Phantump", "Noibat", "Poochyena", "Tinkatuff", "Snubbull", "Hoothoot", "Magby", "Finneon", "Pikachu", "Floragato", "Scraggy", "Nidoran♂", "Numel", "Rookidee", "Gothorita",
		"Nincada", "Lileep", "Poltchageist", "Shelgon", "Purrloin", "Varoom", "Spritzee", "Igglybuff", "Magmar", "Frillish", "Shinx", "Fomantis", "Stufful", "Nidorina", "Onix", "Rowlet", "Hatenna", "Nymble", "Nacli", "Pumpkaboo", "Sliggoo", "Sandile", "Swirlix", "Jigglypuff", "Monferno",
		"Froakie", "Tadbulb", "Foongus", "Timburr", "Nidorino", "Paldean Wooper", "Rufflet", "Hattrem", "Paras", "Nosepass", "Sandygast", "Tyrunt", "Scraggy", "Tinkatink", "Lechonk", "Numel", "Frogadier", "Toxel", "Gloom", "Tyrogue", "Oddish", "Palpitoad", "Scatterbug", "Inkay",
		"Pineco", "Omanyte", "Shuppet", "Vibrava", "Stunky", "Tinkatuff", "Lickitung", "Pansear", "Goldeen", "Tynamo", "Gossifleur", "Paldean Wooper", "Phanpy", "Skiploom", "Kadabra", "Rellor", "Onix", "Sinistea", "Zweilous", "Vullaby", "Togepi", "Lillipup", "Pignite", "Horsea",
		"Voltorb", "Grookey", "Poipole", "Pupitar", "Spearow", "Kirlia", "Sewaddle", "Pupitar", "Yamask", "Zorua", "Togetic", "Litleo", "Ponyta", "Kabuto", "Wattrel", "Grotle", "Roselia", "Rhyhorn", "Staravia", "Meditite", "Shelmet", "Rhyhorn", "Zweilous", "Loudred", "Quilava", "Krabby",
		"Yamper", "Grovyle", "Salandit", "Sandile", "Starly", "Metang", "Silcoon", "Rockruff", "Meowth", "Raboot", "Lombre", "Hisuian Voltorb", "Shroodle", "Sandshrew", "Swablu", "Mime Jr.", "Sizzlipede", "Roggenrola", "Minccino", "Salandit", "Lotad", "Hoppip", "Skorupi", "Sandygast",
		"Taillow", "Munna", "Skorupi", "Rolycoly", "Munchlax", "Scatterbug", "Magikarp", "Ivysaur", "Skrelp", "Silicobra", "Togetic", "Natu", "Snom", "Shieldon", "Patrat", "Scorbunny", "Mantyke", "Lileep", "Spinarak", "Swinub", "Tranquill", "Ralts", "Spewpa", "Tirtouga", "Pidgeotto",
		"Sizzlipede", "Mareanie", "Lombre", "Stunky", "Toedscool", "Trumbeak", "Slowpoke", "Spinarak", "Tyrunt", "Pidgey", "Slugma", "Marill", "Lotad", "Tentacool", "Trapinch", "Vullaby", "Smoochum", "Surskit", "Pidove", "Tepig", "Marshtomp", "Morelull", "Toxel", "Vibrava", "Wattrel",
		"Solosis", "Swadloon", "Pikipek", "Torchic", "Mudkip", "Nuzleaf", "Trubbish", "Wooper", "Wingull", "Spoink", "Tarountula", "Porygon", "Torracat", "Omanyte", "Oddish", "Varoom", "Woobat", "Woobat", "Venipede", "Rattata", "Vulpix", "Oshawott", "Pansage", "Venipede", "Yanma",
		"Wynaut", "Venonat", "Rufflet", "Palpitoad", "Paras", "Venonat", "Zubat", "Weedle", "Sentret", "Panpour", "Petilil", "Weedle", "Whirlipede", "Shroodle", "Piplup", "Phantump", "Weepinbell", "Wimpod", "Skitty", "Poliwag", "Poltchageist", "Whirlipede", "Wurmple", "Skwovet",
		"Poliwhirl", "Pumpkaboo", "Zubat", "Yanma", "Slakoth", "Popplio", "Quilladin", "Smoliv", "Prinplup", "Roselia", "Spearow", "Psyduck", "Rowlet", "Stantler", "Quaxly", "Seedot", "Staravia", "Quaxwell", "Servine", "Starly", "Remoraid", "Sewaddle", "Stufful", "Seadra", "Shroomish",
		"Swablu", "Sealeo", "Skiddo", "Taillow", "Seel", "Skiploom", "Tandemaus", "Shellder", "Smoliv", "Teddiursa", "Shellos", "Snivy", "Tranquill", "Skrelp", "Snover", "Trumbeak", "Slowpoke", "Sprigatito", "Vigoroth", "Sobble", "Steenee", "Whismur", "Spheal", "Sunkern", "Wooloo",
		"Squirtle", "Swadloon", "Yungoos", "Staryu", "Toedscool", "Zigzagoon", "Surskit", "Treecko", "Tentacool", "Turtwig", "Tirtouga", "Weepinbell", "Totodile", "Tympole", "Wailmer", "Wartortle", "Wiglett", "Wimpod", "Wingull", "Wooper"
]

list_lower = set(k.lower() for k in list)

input_file = r'C:\Code Folder\One Pointer Pokemon Searcher\learnset.json'
output_file = r'C:\Code Folder\One Pointer Pokemon Searcher\filtered_learnset.json'

with open(input_file, 'r') as f:
    data = json.load(f)

filtered_data = {key: value for key, value in data.items() if key in list_lower}

with open(output_file, 'w') as f:
    json.dump(filtered_data, f, indent=4)

print(f"Filtered JSON saved to {output_file}")
