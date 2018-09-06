#Project 3

#Name: Emily O'Neal
#Instructor: Mike Ryu
#Section: 13
from solverFuncs import *
import sys

#helper functions

def box_to_row(x):
	
	r = x // 5
	
	return r

def box_to_column(y):
	
	c = y % 5
		
	return c


def main():

	count = 0 
	backtrack = 0
	cages = get_cages()
	puzzle = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0] ]
	box = 0

#loop through the whole grid
	while box < 25:
		

		if puzzle[box_to_row(box)][box_to_column(box)] == 5:
			puzzle[box_to_row(box)][box_to_column(box)] = 0
			backtrack = backtrack + 1 #what even is a backtrack

			box = box -1

			#num = 6
		else:
			num = puzzle[box_to_row(box)][box_to_column(box)] + 1	

			while num <= 5:
				
				puzzle[box_to_row(box)][box_to_column(box)] = num
				count = count + 1
				#print(puzzle)
				if  check_valid(puzzle, cages) == False:

					if num < 5:
						num = num+ 1
					else:
						#print("back:\n", puzzle)
						puzzle[box_to_row(box)][box_to_column(box)] = 0
						num = num + 1
						
						box = box - 1
						backtrack = backtrack + 1
						

				else:
					
					num = 6
					box = box + 1
		#print(puzzle)

	print("\n---Solution---\n")
	
	for part in puzzle:
		print(part[0], part[1],part[2],part[3],part[4],' ')



	#rint (puzzle)
	print ("\nchecks:", count, "backtracks:", backtrack)
	

if __name__ == '__main__':
   main()