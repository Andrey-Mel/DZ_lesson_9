# написать простейшую игру дурак
import random
#--------------------------------------------------------------------
# list_coloda = [(6, 'c'), (7, 'c'), (8, 'c'), (9, 'c'), (10, 'c'), (11, 'c'), (12, 'c'), (13, 'c'), (14, 'c'),
#                        (6, 'b'), (7, 'b'), (8, 'b'), (9, 'b'), (10, 'b'), (11, 'b'), (12, 'b'), (13, 'b'), (14, 'b'),
#                        (6, 'k'), (7, 'k'), (8, 'k'), (9, 'k'), (10, 'k'), (11, 'k'), (12, 'k'), (13, 'k'), (14, 'k'),
#                        (6, 'p'), (7, 'p'), (8, 'p'), (9, 'p'), (10, 'p'), (11, 'p'), (12, 'p'), (13, 'p'), (14, 'p')]
# for i in range(len(list_coloda)):
#     print(list_coloda[i][1])
#Списки: Карты, Колода, список_игрок_1, игрок_комп_2
#----------------------------------------------------------------------------------------
# list_shablon_kart = [(6, 1), (7, 2), (8, 3), (9, 4), (10, 5), ('V', 6), ('D', 7), ('K', 8), ('T', 9)]
#
# for i in range(len(list_shablon_kart)):
#     print(list_shablon_kart[i][0])
#     print(list_shablon_kart[i][1])
#------------------------------------------------------------------------
bubna = [('6_b', 1), ('7_b', 2), ('8_b', 3), ('9_b', 4), ('10_b', 5), ('V_b', 6), ('D_b', 7), ('K_b', 8), ('T_b', 9)]
cherva = [('6_ch', 1), ('7_ch', 2), ('8_ch', 3), ('9_ch', 4), ('10_ch', 5), ('V_ch', 6), ('D_ch', 7), ('K_ch', 8), ('T_ch', 9)]
pika = [('6_p', 1), ('7_p', 2), ('8_', 3), ('9_p', 4), ('10_', 5), ('V_p', 6), ('D_p', 7), ('K_p', 8), ('T_p', 9)]
kresti = [('6_k', 1), ('7_k', 2), ('8_k', 3), ('9_k', 4), ('10_k', 5), ('V_k', 6), ('D_k', 7), ('K_k', 8), ('T_k', 9)]

koloda = [bubna,  cherva, pika, kresti]

#Отдельная масть
for mast in koloda[1]:
    #print(mast)
    pass

#Автоматизировать масть
# for i in range(4):
#     print(koloda[i])
x= 1
mast_kosir = random.choice(koloda)
#print(kosir)

#Перемешать колоду
# random.shuffle(koloda) #перемешивает только мастями а не картами
# print(koloda)
for sh_koloda in koloda:
    random.shuffle(sh_koloda)
    #print(sh_koloda) # мешает только внутри списков мастей

#раздача карт игроку
player_1 = []
# for i in range(6):
#     #player_1 = random.choice(sh_koloda[1])#выводит не то что-то одно из одного какого-то списка мастей
#     print(player_1)
player_1 = random.choices(sh_koloda,k=6)# не получается так тоже одной масти мешает и дает
print(player_1)
