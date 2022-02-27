
import datetime
file_name='example'
# file_name='charleston_road'
# file_name='lets_go_higher'
# file_name='opera'
# file_name='rue_de_londres'

file_name_in = f'{file_name}.in'
file_name_out=f'output/{file_name}.out'

from utils import read_input, read_ouput,draw,draw_signals,calculate_score





start = datetime.datetime.now()


# score=simulate()

read_input(file_name_in)

read_ouput(file_name_out)

score=calculate_score()




print(f'Final Score: {score}')

# draw()
draw_signals()



end = datetime.datetime.now()
# print(f'Ended {end}')

timetaken=end-start

print(f'Time Taken {timetaken}')
