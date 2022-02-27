
import datetime

from utils import create_map, simulate, calculate_score



# file_name='a'
# file_name='b'
# file_name='c'
# file_name='d'
# file_name='e'
file_name='f'

file_name_in = f'{file_name}.txt'
file_name_out=f'output/{file_name}.txt.out'



create_map(file_name_in)



start = datetime.datetime.now()


simulate()

score=calculate_score()

print(f'Final Score: {score}')



end = datetime.datetime.now()
# print(f'Ended {end}')

timetaken=end-start

print(f'Time Taken {timetaken}')

