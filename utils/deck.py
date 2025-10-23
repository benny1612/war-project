def create_card(rank:str,suite:str):
    vel_num=["2","3","4","5","6","7","8","9","10"]
    vel_letaer={"J":11,"Q":12,"K":13,"A":14}
    card_dict={"rank":rank,"suite":suite}
    if rank in vel_num:
        card_dict["velue"]=(rank)
    elif rank in vel_letaer:
        card_dict["velue"]=(vel_letaer[rank])
    return card_dict

# def compare_card(p1_card:dict, p2_card:dict):
#     if p1_card["velue"] > p2_card['velue']:
#         return'p1'
#     elif p1_card["velue"] < p2_card['velue']:
#         return 'p2'
#     elif p1_card["velue"] == p2_card['velue']:
#         return "WAR"


def create_deck():
    vel_num=["2","3","4","5","6","7","8","9","10"]
    vel_letaer={"J":11,"Q":12,"K":13,"A":14}
    suits_list=["H",'C','D','S']
    list_of_cards=[]

    for num in vel_num:
        for l in suits_list:
            list_of_cards.append(create_card(num,l))
    for vl in vel_letaer:
        for l in suits_list:
            list_of_cards.append(create_card(vl,l))
    return list_of_cards
    





list_of_cards=create_deck()
    




def shuffle(deck:list[dict]):
    list_of_cards=create_deck()
    shuffle_list=[]



    import random
    for i in range(random.randrange(1,1001)):
        list_of_cards[random.randint(1,51)]=list_of_cards[random.randint(1,51)]
        
        shuffle_list=list_of_cards
        
        
                
    return shuffle_list


