import csv

data = [
    ["id","name","type1","type2","hp","attack","defense","sp_attack","sp_defense","speed","legendary"],
    [1,"Bulbasaur","Grass","Poison",45,49,49,65,65,45,False],
    [2,"Ivysaur","Grass","Poison",60,62,63,80,80,60,False],
    [3,"Venusaur","Grass","Poison",80,82,83,100,100,80,False],
    [4,"Charmander","Fire","",39,52,43,60,50,65,False],
    [5,"Charmeleon","Fire","",58,64,58,80,65,80,False],
    [6,"Charizard","Fire","Flying",78,84,78,109,85,100,False],
    [7,"Squirtle","Water","",44,48,65,50,64,43,False],
    [8,"Wartortle","Water","",59,63,80,65,80,58,False],
    [9,"Blastoise","Water","",79,83,100,85,105,78,False],
    [25,"Pikachu","Electric","",35,55,40,50,50,90,False],
    [26,"Raichu","Electric","",60,90,55,90,80,110,False],
    [94,"Gengar","Ghost","Poison",60,65,60,130,75,110,False],
    [130,"Gyarados","Water","Flying",95,125,79,60,100,81,False],
    [143,"Snorlax","Normal","",160,110,65,65,110,30,False],
    [150,"Mewtwo","Psychic","",106,110,90,154,90,130,True],
    [151,"Mew","Psychic","",100,100,100,100,100,100,True],
]

with open("pokemon.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("pokemon.csv created!")