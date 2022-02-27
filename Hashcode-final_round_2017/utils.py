

import uuid

from matplotlib import pyplot

num_rows=0
num_cols=0
router_radius=0
backbone_cost=0
router_cost=0
budget=0


num_routers=0
num_backbones=0

initial_backbone=(0,0)

Map=[]


def create_map(num_rows,num_cols,initial_backbone,Lines):
    

    '''
        0 : Invalid Position
        1 : wall
        2 : Area
        3 : Initial Backbone
        4 : Backbone
        5 : Router 
        6 : Signal
    '''
    


    for line in Lines:
        map_row=[]
        for ch in line:
            if not ch == '\n':

                #invalid position
                if ch == '-':
                    map_row.append(0)
                    #wall
                elif ch == '#':

                    map_row.append(1)
                    #area coverage
                elif ch == '.':
                    map_row.append(2)


                # map_row.append(ch)
                # print(ch,end='')
        
        Map.append(map_row)

    #place backbone


    Map[initial_backbone[0]][initial_backbone[1]]=3
    



def read_input(file_name_in):


    Lines=[]


    with open(file_name_in, "r") as f:
        Lines = f.readlines()


    first_line=Lines[0].split()
    second_line=Lines[1].split()
    third_line=Lines[2].split()


    global num_rows
    global num_cols
    global router_radius
    global backbone_cost
    global router_cost
    global budget

    global initial_backbone

    num_rows=int(first_line[0])
    num_cols=int(first_line[1])
    router_radius=int(first_line[2])

    backbone_cost=int(second_line[0])
    router_cost=int(second_line[1])
    budget=int(second_line[2])


    initial_backbone=(int(third_line[0]),int(third_line[1]))
    print(f'Num Rows: {num_rows}')
    print(f'Num Columns: {num_cols}')
    print(f'Router Radius: {router_radius}')
    print(f'BAckbone Cost: {backbone_cost}')
    print(f'Router Cost: {router_cost}')
    print(f'Budget: {budget}')
    print(f'Backbone: {initial_backbone}')
    
    create_map(num_rows,num_cols,initial_backbone,Lines[3:])
    


backbone_poss=[]

def place_backbones(Lines):

    global Map
    global num_backbones

    for backbone in Lines:
        num_backbones+=1
        pos=backbone.split()
        row=int(pos[0])
        col=int(pos[1])
        # pos=(row,col)
        Map[row][col]=4


routers_poss=[]

def place_routers(Lines):

    global Map
    global num_routers
    global routers_poss



    for router in Lines:
        num_routers+=1
        pos=router.split()
        row=int(pos[0])
        col=int(pos[1])
        pos=(row,col)
        routers_poss.append(pos)
        Map[row][col]=5


def read_ouput(file_name_out):


    Lines=[]


    with open(file_name_out, "r") as f:
        Lines = f.readlines()


    num_backbone=int(Lines[0])

    num_routers=int(Lines[num_backbone+1])

    # print(num_backbone)
    # print(num_routers)


    place_backbones(Lines[1:num_backbone+1])

    place_routers(Lines[num_backbone+2:num_backbone+num_routers+2])


Signal_Map=[]

from copy import copy, deepcopy


def get_area_covered_by_routers():

    area=0


    global Map
    global Signal_Map
    Signal_Map=deepcopy(Map)


    global routers_poss
    global router_radius

    global num_rows
    global num_cols



    # print(routers_poss)


    Map_Signals=[[False for _ in range(num_cols)] for _ in range(num_rows)]

    for arouter in routers_poss:
        router_row = arouter[0]
        router_col = arouter[1]



        for i in range(-router_radius,router_radius+1):
            for j in range(-router_radius,router_radius+1):

                row=router_row+i
                col=router_col+j


                val = Map[row][col] 
                if not (val == 0 or val == 1):
                    # area+=1
                    Map_Signals[row][col] = True
                    Signal_Map[row][col] = 6

        



    for row in Map_Signals:
        area+=sum(row)


    # print(f'Area: {area}')


    return area

    
def calculate_score():

    global num_routers
    global num_backbones
    global backbone_cost
    global router_cost
    global budget
    
    score=0

    score += (budget-((num_routers*router_cost) + (num_backbones*backbone_cost)))

    area_covered_by_routers=get_area_covered_by_routers()

    score+= (1000*area_covered_by_routers)


    return score


def draw():

    global Map

    pyplot.figure(figsize=(5,5))
    pyplot.imshow(Map)
    pyplot.show()


def draw_signals():

    global Signal_Map

    pyplot.figure(figsize=(5,5))
    pyplot.imshow(Signal_Map)
    pyplot.show()