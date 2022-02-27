
import datetime



# file_name='a_an_example'
# file_name='b_basic'
file_name='c_coarse'
# file_name='d_difficult'
# file_name='e_elaborate'

file_name_in = f'{file_name}.in.txt'
file_name_out=f'output/{file_name}.out.txt'


















start = datetime.datetime.now()




end = datetime.datetime.now()
# print(f'Ended {end}')

timetaken=end-start

print(f'Time Taken {timetaken}')

