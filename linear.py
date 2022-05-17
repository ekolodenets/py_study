# !python -m pip install --upgrade --user -q ortools
'''
Unit	      🌾Food	🪵Wood	🪙Gold	💪Power
🗡️Swordsman	    60	      20	  0	      70
🏹Bowman	    80	      10	  40	  95
🐎Horseman	    140	      0	      100	  230
'''
ratiosword = sum([60, 20, 0]), 70
ratiobow = sum([80, 10, 40]), 95
ratiohorse = sum([140, 0, 100]), 230
# Import OR-Tools' wrapper for linear solvers
from ortools.linear_solver import pywraplp
import math

# Create a linear solver using the GLOP backend
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

# Create the variables we want to optimize
swordsmen = solver.IntVar(0, solver.infinity(), 'swordsmen')
bowmen = solver.IntVar(0, solver.infinity(), 'bowmen')
horsemen = solver.IntVar(0, solver.infinity(), 'horsemen')

food = 2741
wood = 1000
gold = 1041


# Add constraints for each resource
solver.Add(swordsmen*60 + bowmen*80 + horsemen*140 <= food) # Food
solver.Add(swordsmen*20 + bowmen*10 + horsemen*0 <= wood)                 # Wood
solver.Add(swordsmen*0 +bowmen*40 + horsemen*100 <= gold)                 # Gold


# Maximize the objective function
power_s = 70
power_b = 95
power_h = 230

solver.Maximize(swordsmen*power_s + bowmen*power_b + horsemen*power_h)
# ratio_sword = round(sum([60, 20, 0])/power_s,2)
# ratio_bow = round(sum([80, 10, 40])/power_b,2)
# ratio_horse = round(sum([140, 0, 100])/power_h,2)
# print(f'{ratio_sword=}, {ratio_bow=}, {ratio_horse=}')

# Solve problem
status = solver.Solve()

# If an optimal solution has been found, print results
if status == pywraplp.Solver.OPTIMAL:
  print('================= Solution =================')
  print(f'Solved in {solver.wall_time():.2f} milliseconds in {solver.iterations()} iterations')
  print()
  print(f'Optimal power = {solver.Objective().Value()} 💪power')
  print('Army:')
  print(f' - 🗡️Swordsmen = {math.floor(swordsmen.solution_value())}')
  print(f' - 🏹Bowmen = {math.floor(bowmen.solution_value())}')
  print(f' - 🐎Horsemen = {math.floor(horsemen.solution_value())}')
  print(f'Food left: {food - math.floor(swordsmen.solution_value())*60 - math.floor(bowmen.solution_value())*80 - math.floor(horsemen.solution_value())*140}')
  print(f'Wood left: {wood - math.floor(swordsmen.solution_value())*20 - math.floor(bowmen.solution_value())*10}')
  print(f'Gold left: {gold - math.floor(bowmen.solution_value())*40 - math.floor(horsemen.solution_value())*100}')
else:
  print('The solver could not find an optimal solution.')