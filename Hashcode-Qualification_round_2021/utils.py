
import uuid


simulation_time=0
num_of_intersections=0
num_of_streets=0
num_of_cars=0
car_points=0


Traffic_Lights=[]

Intersections=[]



Streets=[]
Streets_Dict={}


Cars=[]


class Intersection:
    def __init__(self) -> None:
        
        self.intersection_in_street=[]
        self.cars_at_in_street=[]

        self.traffic_light=None

        self.car_passed=False


        self.intersection_out_street=[]


    def append_intersection_in_street(self,street):
        self.intersection_in_street.append(street)

    def append_intersection_out_street(self,street):
        self.intersection_out_street.append(street)

    def append_car_at_in_street(self,car):
        self.cars_at_in_street.append(car)


    def loop(self):
        self.car_passed=False



    def get_car_turn(self,car):
        
        if not self.car_passed:
            self.car_passed=True
            if self.cars_at_in_street[0] == car:
                
                self.cars_at_in_street[0].move_to_next_street()
                self.cars_at_in_street.pop()




class Street:
    def __init__(self,street_name,street_time,street_start_intersection,street_end_intersection) -> None:
        self.street_name=street_name
        self.street_time=street_time
        self.street_start_intersection=street_start_intersection
        self.street_end_intersection=street_end_intersection


    def add_car_at_end_of_street_intersection_in(self,car):
        self.street_end_intersection.append_car_at_in_street(car)


    def get_car_turn(self,car):
        self.street_end_intersection.get_car_turn(car)





class Car:
    def __init__(self,car_path) -> None:

        self.uuid=uuid.uuid4().hex
        self.car_path=car_path
        # print(self.car_path)

        self.moving=True
        self.time_passed=0
        self.countdown=0

        self.path_street_index=0
        self.path_street=self.car_path[0]

        self.path_street_end=True
        self.add_car_at_end_of_street_intersection_in()


    def add_car_at_end_of_street_intersection_in(self):
        self.path_street_end=True
        self.path_street.add_car_at_end_of_street_intersection_in(self)

    def move(self):


        if self.moving:

            


            if self.countdown:
                self.countdown -=1
            
            if not self.countdown:

                if self.path_street_index == len(self.car_path)-1:
                    self.end_journey()
                    return

                if self.path_street_end:
                    self.path_street.get_car_turn(self)
                else:
                    self.add_car_at_end_of_street_intersection_in()
                    self.path_street.get_car_turn(self)

            self.time_passed+=1
                    


        
        
        # print(f'{self.uuid} {self.path_street.street_name} {self.countdown} {self.moving}')
        # print(f'{self.uuid} {self.time_passed}')

                    

    def end_journey(self):
        self.moving=False
        # print(f'End Journey')


            
                





    def move_to_next_street(self):

        if self.path_street_index < len(self.car_path)-1:


            # print(self.path_street.street_name)

            self.path_street_index+=1
            self.path_street=self.car_path[self.path_street_index]
            self.path_street_end=False
            self.countdown= self.path_street.street_time



            

            








class Traffic_Light:
    def __init__(self) -> None:
        pass






def create_map(file_name_in):

    global Intersections

    Lines=[]


    with open(file_name_in, "r") as f:
        Lines = f.readlines()


    first_line=Lines[0].split()

    global simulation_time
    global num_of_intersections
    global num_of_streets
    global num_of_cars
    global car_points

    simulation_time=int(first_line[0])
    num_of_intersections=int(first_line[1])
    num_of_streets=int(first_line[2])
    num_of_cars=int(first_line[3])
    car_points=int(first_line[4])

    print(f'Simulation Time: {simulation_time}')
    print(f'Num of Intersections: {num_of_intersections}')
    print(f'Num of Streets: {num_of_streets}')
    print(f'Num of Cars: {num_of_cars}')
    print(f'Car Points: {car_points}')
    
    # Intersections=[[[],[]] for _ in range(num_of_intersections)]

    for _ in range(num_of_intersections):
        Intersections.append(Intersection())

    create_street_intersections(Lines,num_of_streets)
    create_cars(Lines,num_of_streets,num_of_cars)


    # print(Intersections)

    # print(Streets)

    # print(Streets_Dict)

    # print(Cars)




def create_street_intersections(Lines,num_of_streets):

    # print('Street Loop')



    #Street Loop
    for i in range(1,num_of_streets+1):
        # print(i)
        street_index=i-1
        street_line=Lines[i].split()
        # print(street_line)
        street_name=street_line[2]
        street_time=int(street_line[3])
        street_start=int(street_line[0])
        street_end=int(street_line[1])
        





        global Streets
        global Streets_Dict

        global Intersections

        street=Street(
            street_name,street_time,Intersections[street_start],Intersections[street_end]
        )
        Streets.append(street)
        Streets_Dict[street_name]=street_index


        

        # #Intersections IN
        # Intersections[street_end][0].append(street_index)
        Intersections[street_end].append_intersection_in_street(street)

        # #Intersections OUT
        # Intersections[street_start][1].append(street_index)
        Intersections[street_start].append_intersection_out_street(street)
        





def create_cars(Lines,num_of_streets,num_of_cars):

    global Cars
    # print('Car Loop')

    #Car Loop
    for i in range(num_of_streets+1,num_of_streets+1+num_of_cars):
        # print(i)
        car_line=Lines[i].split()[1:]
        # print(car_line)
        car=Car([Streets[Streets_Dict[car_path]] for car_path in car_line])
        Cars.append(car)


def calculate_score():

    global car_points
    score=0

    for car in Cars:
        if not car.moving:
            # print(car.time_passed)
            points=car_points + (simulation_time-car.time_passed)
            score+=points


    return score


def simulate():


    simulation_timer=0


    while(True):
        if simulation_timer >= simulation_time:
            break


        for intersection in Intersections:
            intersection.loop()

        for car in Cars:
            car.move()



        simulation_timer+=1

    

