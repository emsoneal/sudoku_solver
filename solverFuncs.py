
#Project 3

#Name: Emily O'Neal
#Instructor: Mike Ryu
#Section: 13
def check_valid(puzzle, cages):
	
	if check_rows_valid(puzzle) == True and check_columns_valid(puzzle) == True and check_cages_valid(puzzle, cages):
		return True
	else: 
		return False
	
	check_cages_valid(puzzle, cages)


def check_rows_valid(puzzle):
	#use nested for loops
		#first loop gives you the correct list (which row)
	for row in puzzle:

			#second loop goes through each index in the list 
		for indx in range(len(row)):
			next1 = indx + 1
			
				
			 #check to see if each index is the same as the last
			while next1 < 5:
				
			 	if row[indx] == row[next1] and row[next1] != 0:
			 		return False
			 	else:
			 		next1 = next1 + 1
	return True
			 #if it is, change the number and check again


def check_columns_valid(puzzle):

	
	for cndx in range(5):
		for rndx in range(4):
			next1 = rndx + 1
			
			while next1 < 5:

				if puzzle[rndx][cndx]== puzzle[next1][cndx] and puzzle[next1][cndx] != 0:
					return False
				else:
					next1 = next1 + 1 

	return True

def check_cages_valid(puzzle, cages):

	for c in cages:
		most = c[0]
		num = c[1]
		sumCages = 0
		small = []
		zero = False
		
		for indx in range(num):
			# if there is a zero, it can still be less
			
			# if c[indx+2] <= 4:
			# 	sumCages = sumCages + puzzle[0][c[indx+2]]
			# 	small.append(puzzle[0][c[indx+2]])
			# else:
			sumCages = sumCages + puzzle[c[indx+2] // 5][c[indx+2] % 5]
			small.append(puzzle[c[indx+2] // 5][c[indx+2] % 5])

			if sumCages > most :
				return False
			


		for n in small:
			if n == 0:
				zero = True
				#numZero = numZero + 1
		if sumCages >= most and zero == True :
				return False

		#if sumCages + 5 * numZero < most:
			#return False
		if sumCages < most and zero == False :
			return False
	
	return True
			
def get_cages():

	cage = []
	part = []
	num = input('Number of cages: ')
	for i in range(int(num)):
		part = input("Cage number " + str(i) + ": ").split()
		part = [int(j) for j in part]
		cage.append(part)



	return cage 

