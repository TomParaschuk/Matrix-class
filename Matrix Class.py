class Matrix(object):
	
	def init_empty(self, y, x):
		self.m = y;
		self.n = x;
		self.L = [[0 for i in range(self.n)] for i in range(self.m)];
		self.is_jagged = 0;
		self.is_square = (self.m == self.n);

	def init_full(self, matrix): #gotta fix empty matrix
		self.L = matrix;
		self.m = len(self.L);
		self.n = len(self.L[0]);
		self.is_jagged = 0;

		for x in range(0, len(matrix) - 1):
			if(len(matrix[x]) != len(matrix[x + 1])):
				self.is_jagged = 1;
				self.n = "variable";

		self.is_square = (self.m == self.n);

	def __init__(self, *args):
		if len(args) == 1: # have to fix for a length of 1 which doesn't give a matrix
			self.init_full(args[0]);
		elif len(args) == 2:
			self.init_empty(args[0], args[1]);
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
					print(self.L[x][y], end = ' ');
				print();
		else:
			print("This is a non-square, jagged matrix. No operations are defined.")
			for x in range(0,self.m):
				for y in range(0,len(self.L[x])):
					print(self.L[x][y], end = ' ');
				print();
	
	def get_sub_matrix(self, index):
		sub_matrix = Matrix(self.m-1, self.m-1);

		for x in range(1, self.m):
			for i in range(0, index-1):
				sub_matrix.L[x-1][i] = self.L[x][i];
				
			for j in range(index, self.m):
				sub_matrix.L[x-1][j-1] = self.L[x][j];
				
		return sub_matrix;

	def determinant(self):
		if(not(self.is_square) or self.is_jagged):
			return "Determinant must be of a square matrix."
		elif(self.m == 0):
			return "Cannot compute determinant of empty matrix."
		elif(self.m == 1):
			return self.L[0];
		elif(self.m == 2):
			return self.L[0][0]*self.L[1][1]-self.L[1][0]*self.L[0][1];
		else:
			current_sum = 0;
			for index in range(1, self.m+1):
				current_sum += (-1)**(index-1)*self.L[0][index-1]*(self.get_sub_matrix(index)).determinant();
			return current_sum;
	
	def add_or_subtract(self,type, *args):
		val = 0;
		for i in range (0, len(args)):
			val += (self.m != args[i].m or self.n != args[i].n);
		return val;

	# def add_or_subtract(self, type, *args):
	# 	if(self.is_jagged):
	# 		return "Matrices are jagged or do not have the same size, operation not permitted.";
	# 	for i in range(0, len(args)):
	# 		if(self.m != args[i].m or self.n != args[i].n):
	# 			return "Matrices are jagged or do not have the same size, operation not permitted.";
	# 	#error check
	# 	result = self.L;
	# 	for i in range(0, len(args)):
	# 		for x in range(0, self.m):
	# 			for y in range(0, self.n):
	# 				if(type == 1):
	# 					result[x][y] += args[i].L[x][y];
	# 				else:
	# 					result[x][y] -= args[i].L[x][y];
	# 	return Matrix(result);

	def add(self, *args):
		return self.add_or_subtract(1, *args);

	def subtract(self, *args):
		return self.add_or_subtract(0, *args);

	# def transpose(self):
	# 	if(self.is_jagged or not(self.is_square)):
	# 		return "Non-square matrices cannot be transposed."
	# 	else:
	# 		tranpose = self;
	# 		for i in range(1, transpose.m + 1):
	# 			for j in range(0, i):
	# 				temp = tranpose.L[i][j];
	# 				transpose.L[i][j] = transpose.L[j][i];
	# 				transpose.L[j][i];
	# 		return transpose;

	# def invert(self):
	# 	if(!self.is_square):
	# 		return "The determinant of a non-square matrix is undefined."
	# 	elif(self.determinant() == 0):
	# 		return "The determinant of the matrix is 0; it is uninvertible."
	# 	else:

a = Matrix([[1,2],[3,4]])
#a.transpose().display();
b = Matrix(3,3);
print(a.add(b));
b = a;
b.display();
