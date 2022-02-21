import numba


import random
import math
import numpy as np
import time


import datetime



# file_name='a_an_example'
# file_name='b_basic'
file_name='c_coarse'
# file_name='d_difficult'
# file_name='e_elaborate'

file_name_in = f'{file_name}.in.txt'
file_name_out=f'output/{file_name}.out.txt'


Lines=[]




with open(file_name_in, "r") as f:
    Lines = f.readlines()

# print(Lines)
# for line in Lines:
#     print(line)

num_of_clients=int(Lines[0])
print(f'num_of_clients: {num_of_clients}')









Ingredients=np.array([])


def create_ingredient(liked_ingredients):
    global Ingredients
    for i in range(len(liked_ingredients)):
        if liked_ingredients[i]  not in Ingredients:
            Ingredients=np.append(Ingredients,liked_ingredients[i])

    
#create ingredients


def create_ingredients():
  for i in range(1,len(Lines),2):

      liked_ingredients=Lines[i].split()[1:]
      disliked_ingredients=Lines[i+1].split()[1:]

      # print(liked_ingredients)
      # print(disliked_ingredients)

      create_ingredient(liked_ingredients)

create_ingredients()


Ingredients_shape=Ingredients.shape
num_of_ingredients=Ingredients_shape[0]

# print(f'Ingredients: {len(Ingredients)}')
print(f'Ingredients: {num_of_ingredients}')
# print(f'All Ingredients {Ingredients}')






def get_ingredient_name(index):
    return Ingredients[index]


def get_pizza_ingredient_name(pizza):
    return [get_ingredient_name(index) for index in pizza]



def get_ingredient_index_from_name(ingredient_name):

    # try:
    #     return Ingredients.index(ingredient_name)
    # except:
    #     return False


    for i, ingredient in enumerate(Ingredients) :

        if ingredient == ingredient_name:
            return i








# Clients=np.array([])

Clients=[]



# Clients_Like=np.array([])
# Clients_Dislike=np.array([])

# client_count=0


def create_client(liked_ingredients,disliked_ingredients):
    # global client_count
    # client_count+=1
    global Clients
    # global Clients_Like
    # global Clients_Dislike

    
    

    # liked_ingredients_array=np.zeros(Ingredients_shape,dtype=np.int8)
    # disliked_ingredients_array=np.zeros(Ingredients_shape,dtype=np.int8)
    liked_ingredients_array=np.full(Ingredients_shape, False, dtype=bool)
    disliked_ingredients_array=np.full(Ingredients_shape, False, dtype=bool)

    # print(liked_ingredients)
    # print(disliked_ingredients)



    for liked_ingredient in liked_ingredients:
        # print(liked_ingredient)
        ingredient_index=get_ingredient_index_from_name(liked_ingredient)
        # print(ingredient_index)
        if ingredient_index is not None:
            # liked_ingredients_array=np.append(liked_ingredients_array,ingredient_index)
            liked_ingredients_array[ingredient_index]=True

    for disliked_ingredient in disliked_ingredients:
        ingredient_index= get_ingredient_index_from_name(disliked_ingredient)
        if ingredient_index is not None:
            # disliked_ingredients_array=np.append(disliked_ingredients_array,ingredient_index)
            disliked_ingredients_array[ingredient_index]=True


    # print(liked_ingredients_array)
    # print(f"liked_ingredients: {get_pizza_ingredient_name(clientobj[0])}")
    # print(f"disliked_ingredients: {get_pizza_ingredient_name(clientobj[1])}")

    # clientobj=np.array([])
    clientobj=np.array(np.array([liked_ingredients_array,disliked_ingredients_array]))
    # , dtype=object

    # clientobj_like=np.array(np.array([liked_ingredients_array,]))
    # clientobj_dislike=np.array(np.array([disliked_ingredients_array,]))

    

    # Clients_Like=np.append(Clients_Like,np.array([clientobj_like,]))
    # Clients_Dislike=np.append(Clients_Dislike,np.array([clientobj_dislike,]))
    # print(clientobj)
    # print(clientobj[0])
    # print(clientobj[1])

    # Clients=np.append(Clients,np.array([clientobj]))
    Clients.append(clientobj)


    # Clients=Clients+[clientobj]
    # Clients= np.append(Clients, [[clientobj]], axis=0)
    # Clients=np.vstack((Clients, clientobj))


    # print(clientobj)



    #create Clients


def create_clients():
  for i in range(1,len(Lines),2):

      liked_ingredients=Lines[i].split()[1:]
      disliked_ingredients=Lines[i+1].split()[1:]



      # print(liked_ingredients)
      # print(disliked_ingredients)

      # create_ingredient(liked_ingredients)
      create_client(liked_ingredients,disliked_ingredients)


create_clients()







ClientsArray = np.asarray([client for client in Clients])







score=0

with open(file_name_out, "r") as f:
    Line = f.readline()

pizza_lines=Line.split()[1:]

# print(f'Out Pizza: {pizza_lines}')
print(f'Out Pizza Ingredients: {len(pizza_lines)}')

# pizza=np.array([get_ingredient_index_from_name(pizza_ingredient) for pizza_ingredient in pizza_lines])
pizza=np.full(Ingredients_shape, False, dtype=bool)

for pizza_ingredient in pizza_lines:
  ingredient_index=get_ingredient_index_from_name(pizza_ingredient)
  pizza[ingredient_index]=True

# pizza




@numba.njit
def will_buy_pizza(client, pizza):

    # print(f'Pizza: {get_pizza_ingredient_name(pizza)}')

    liked_ingredients=client[0]
    disliked_ingredients=client[1]

    # for _, liked_ingredient in np.ndenumerate(liked_ingredients):
        # print(f'liked: {get_ingredient_name(liked_ingredient)}')
        # if liked_ingredient not in pizza:
        
            # print('not in pizza')
            # return False

    # for _, disliked_ingredient in np.ndenumerate(disliked_ingredients):
        # print(f'disliked: {get_ingredient_name(disliked_ingredient)}')
        # if disliked_ingredient in pizza:
            # print('in pizza')
            # return False

    liked_ingredients_indexes=np.where(liked_ingredients==True)
    disliked_ingredients_indexes=np.where(disliked_ingredients==True)
    # print(liked_ingredients_indexes)
    # print(disliked_ingredients_indexes)

    for liked_ingredients_index in liked_ingredients_indexes[0]:
      # print(liked_ingredients_index)
      if pizza[liked_ingredients_index] == False:
        return False

    for disliked_ingredients_index in disliked_ingredients_indexes[0]:
      if pizza[disliked_ingredients_index] == True:
        return False



    return True

# will_buy_pizza(ClientsArray[0], pizza)





@numba.njit
def return_score(pizza):
    score=0
    # print(ClientsArray.shape[0])

    for i in range(0,ClientsArray.shape[0]):
        # print()
        if will_buy_pizza(ClientsArray[i], pizza):
            score+=1

        
    # print(client)
    # for client_index in range(0,num_of_clients):
    #     client=np.array([Clients[2*client_index],Clients[2*client_index+1]])

        # if will_buy_pizza(ClientsArray[0], pizza):
        #     score+=1

    return score


start=datetime.datetime.now()


score=return_score(pizza)

end=datetime.datetime.now()

duration= end-start
print(f'Time taken: {duration}')


print(f'Filename: {file_name}')
print(f'Final Score: {score}')