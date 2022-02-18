



import datetime



# file_name='a_an_example'
# file_name='b_basic'
file_name='c_coarse'
# file_name='d_difficult'
# file_name='e_elaborate'

file_name_in = f'{file_name}.in.txt'
file_name_out=f'{file_name}.out.txt'


start = datetime.datetime.now()
# print(f'Started {start}')


Ingredients=[]
# Pizzas=[]
Clients=[]

# class Ingredient:
#     def __init__(self) -> None:
#         pass


# class Pizza:
#     def __init__(self) -> None:
#         pass

# class Client:
#     def __init__(self) -> None:
#         pass






Lines=[]




with open(file_name_in, "r") as f:
    Lines = f.readlines()

# print(Lines)
# for line in Lines:
#     print(line)

num_of_clients=int(Lines[0])
print(f'num_of_clients: {num_of_clients}')



def create_ingredient(liked_ingredients):
    for i in range(len(liked_ingredients)):
        if liked_ingredients[i]  not in Ingredients:
            Ingredients.append(liked_ingredients[i])

    
#create ingredients
for i in range(1,len(Lines),2):

    liked_ingredients=Lines[i].split()[1:]
    disliked_ingredients=Lines[i+1].split()[1:]

    # print(liked_ingredients)
    # print(disliked_ingredients)

    create_ingredient(liked_ingredients)




print(f'Ingredients: {len(Ingredients)}')
print((Ingredients))

from itertools import combinations

pizza_combinations = list()
for n in range(1,len(Ingredients) + 1):
    # list_combinations += list(combinations(Ingredients, n))
    pizza_combinations += list(combinations(range(len(Ingredients)), n))
    


# print(len(pizza_combinations))
# print(pizza_combinations)




list_potential_clients_for_combinations=[0] * len(pizza_combinations)

# print(len(list_potential_clients_for_combinations))

# print(list_potential_clients_for_combinations)




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


def create_client(liked_ingredients,disliked_ingredients):

    
    clientobj={
        0:[],
        1:[],
    }


    # print(liked_ingredients)
    # print(disliked_ingredients)



    for liked_ingredient in liked_ingredients:
        # print(liked_ingredient)
        ingredient_index=get_ingredient_index_from_name(liked_ingredient)
        # print(ingredient_index)
        if ingredient_index is not None:
            clientobj[0].append(ingredient_index)

    for disliked_ingredient in disliked_ingredients:
        ingredient_index= get_ingredient_index_from_name(disliked_ingredient)
        if ingredient_index is not None:
            clientobj[1].append(ingredient_index)



    # print(f"liked_ingredients: {get_pizza_ingredient_name(clientobj[0])}")
    # print(f"disliked_ingredients: {get_pizza_ingredient_name(clientobj[1])}")



    Clients.append(clientobj)



    #create Clients
for i in range(1,len(Lines),2):

    liked_ingredients=Lines[i].split()[1:]
    disliked_ingredients=Lines[i+1].split()[1:]



    # print(liked_ingredients)
    # print(disliked_ingredients)

    # create_ingredient(liked_ingredients)
    create_client(liked_ingredients,disliked_ingredients)


# print(Clients)



def will_buy_pizza(client, pizza):

    # print(f'Pizza: {get_pizza_ingredient_name(pizza)}')

    

    for liked_ingredient in client[0]:
        # print(f'liked: {get_ingredient_name(liked_ingredient)}')
        if liked_ingredient not in pizza:
            # print('not in pizza')
            return False

    for disliked_ingredient in client[1]:
        # print(f'disliked: {get_ingredient_name(disliked_ingredient)}')
        if disliked_ingredient in pizza:
            # print('in pizza')
            return False

    return True



# will_buy_pizza(Clients[0], pizza_combinations[0])

for client in Clients:
    # print(client)
    for i, pizza in enumerate(pizza_combinations):

        if will_buy_pizza(client, pizza):
            list_potential_clients_for_combinations[i]+=1





# print(list_potential_clients_for_combinations)

max_value = max(list_potential_clients_for_combinations)
max_index = list_potential_clients_for_combinations.index(max_value)


# print(max_index)

max_pizza=pizza_combinations[max_index]

# print(max_pizza)

def make_pizza(pizza):
    return get_pizza_ingredient_name(pizza)



output_pizza=make_pizza(max_pizza)


def save_pizza(pizza):
    
     with open(file_name_out,"w") as f:
        # L = ["This is Delhi \n","This is Paris \n","This is London"] 
        output=f'{len(pizza)}'
        f.write(output)

        for ingredient in pizza:
            output=f' {ingredient}'
            f.write(output)

        # f.writelines(output)

save_pizza(output_pizza)

end = datetime.datetime.now()
# print(f'Ended {end}')

timetaken=end-start

print(f'Time Taken {timetaken}')


