#import test_matrices.py
#make a file of test matrices so not always checking 

class Matrix(object): 
	
	def init_empty(self, y, x):
		self.m = y
		self.n = x
		self.L = [[0 for i in range(self.n)] for i in range(self.m)]
		self.is_jagged = 0
		self.is_square = (self.m == self.n)

	def init_full(self, matrix): #have to fix empty matrix
		self.L = matrix
		self.m = len(self.L)
		self.n = len(self.L[0])
		self.is_jagged = 0

		for x in range(0, len(matrix) - 1):
			if(len(matrix[x]) != len(matrix[x + 1])):
				self.is_jagged = 1
				self.n = "variable"

		self.is_square = (self.m == self.n)
		#make this a function eventually, doesn't update statically when add/subtract called
		#make syntax of error checking more intutive on the whole

	def __init__(self, *args):
		if len(args) == 1: # have to fix for a length of 1 which doesn't give a matrix
			self.init_full(args[0]);
		elif len(args) == 2:
			self.init_empty(args[0], args[1])
		else:
			print("This is not a valid initialization, either pass the x and y parameter or a full matrix.");
	

	#def increase_size(self, addition, position):
		

	def display(self):
		if(self.is_jagged == 0):
			print("This is a", self.m, "by", self.n, "matrix which is not jagged.");
			if(self.is_square):
				print("It is square, so the determinant operation is defined.")
			else:
				print("It is not square, so the determinant is not defined.")
			for x in range(0, self.m):
				for y in range(0, self.n):
					print(self.L[x][y], end = ' ')
				print();
		else:
			print("This is a non-square, jagged matrix. No operations are defined.")
			for x in range(0,self.m):
				for y in range(0,len(self.L[x])):
					print(self.L[x][y], end = ' ')
				print()
	

	#is this exactly a cofactor or is it a slightly different definition
	def get_cofactor_i_j(self, index1, index2):
		#error check the indicies if this is publicly accessible


		if(not(self.is_square)):
			print("Can't compute cofactors of a nonsquare matrix.")

		else:
			sub_matrix = Matrix(self.m-1, self.m-1)

			for x in range(0, index2-1):
				for i in range(0, index1-1):
					sub_matrix.L[x][i] = self.L[x][i]
				
				for j in range(index1, self.m):
					sub_matrix.L[x][j-1] = self.L[x][j]
			for y in range(index2, self.m):
				for i in range(0, index1-1):
					sub_matrix.L[y-1][i] = self.L[y][i]
			
				for j in range(index1, self.m):
					sub_matrix.L[y-1][j-1] = self.L[y][j]


		
			#use list operations more efficiently		
			return sub_matrix

	def get_cofactor_matrix(self):
		if(not(self.is_square)):
			print("Can't generate cofactor matrix of a nonsquare matrix.")
		
		else:
			cofactor_matrix = Matrix(self.m,self.n)
			
			for i in range(1,self.m+1):
				for j in range(1,self.n+1):
					positive_or_negative = (-1)**((i+j)%2)
					value = self.get_cofactor_i_j(i,j).determinant()
					cofactor_matrix.L[i-1][j-1] = positive_or_negative*value
			
			return cofactor_matrix

	def determinant(self):
		if(not(self.is_square) or self.is_jagged):
			return "Determinant must be of a square matrix."
		elif(self.m == 0):
			return "Cannot compute determinant of empty matrix."
		elif(self.m == 1):
			return self.L[0]
		elif(self.m == 2):
			return self.L[0][0]*self.L[1][1]-self.L[1][0]*self.L[0][1]
		else:
			current_sum = 0
			for index in range(1, self.m+1):
				current_sum += (-1)**(index-1)*self.L[0][index-1]*(self.get_cofactor_i_j(index,1)).determinant()
			return current_sum
	
	def add_or_subtract(self,type, *args):
		val = 0
		for i in range (0, len(args)):
			val += (self.m != args[i].m or self.n != args[i].n)
		return val

	def add_or_subtract(self, type, *args):
		if(self.is_jagged):
			return "Matrices are jagged or do not have the same size, operation not permitted."
		for i in range(0, len(args)):
			if(self.m != args[i].m or self.n != args[i].n):
				return "Matrices are jagged or do not have the same size, operation not permitted."
		#error check
		result = self.L;
		for i in range(0, len(args)):
			for x in range(0, self.m):
				for y in range(0, self.n):
					if(type == 1):
						result[x][y] += args[i].L[x][y]
					else:
						result[x][y] -= args[i].L[x][y]
		return Matrix(result)

	#error: adds two matrices of different sizes

	def add(self, *args):
		return self.add_or_subtract(1, *args)

	def subtract(self, *args):
		return self.add_or_subtract(0, *args)

	def transpose(self):
		if(self.is_jagged or not(self.is_square)):
			return "Non-square matrices cannot be transposed."
		else:
			transposed = self.L
			for i in range(1, self.m):
				for j in range(0, i):
					temp = transposed[i][j]
					transposed[i][j] = transposed[j][i]
					transposed[j][i] = temp
			return Matrix(transposed)
				
	#fix all the bad error checking
	def invert(self):
		if(not(self.is_square)):
			print("The determinant of a non-square matrix is undefined.")
			return
		elif(self.determinant() == 0):
			print( "The determinant of the matrix is 0; it is uninvertible.")
			return
		else:
			inverse = self.get_cofactor_matrix().transpose()
			factor = 1/self.determinant()
			for i in range(0,self.m):
				for j in range(0,self.n):
					inverse.L[i][j] *= factor
			return inverse



a = Matrix([[1,2],[3,4]])
test = Matrix([[1,2,3,4,5],[6,7,8,-9,10.2],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
test1 = Matrix([[4,6,90],[11,-32,33],[2.798,128,257]])

#test.transpose().display()

test1.get_cofactor_matrix().display()

b = Matrix([[1,2,3],[4,5,6],[7,8,9]])
#test1.invert().display()