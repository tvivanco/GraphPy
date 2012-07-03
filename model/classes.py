import copy	# Para hacer copias superficiales (shallow copies)

class Matrix:
	"""Clase que maneja la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self, dim):
		self.__dimMatrix = dim
		self.__matrix = self.__set_matrix(dim)
	
	#
	#  PRIVATE METHODS
	#
	
	def __set_matrix(self, dim):
		"""Para una dimension "dim":
		Crea una nueva matriz. Todos sus elementos tienen el valor '0'
		Retorna la nueva matriz"""
		matrix = []
		for i in range(dim):
			matrix.append([])
			for j in range(dim):
				matrix[i].append(0)
		return matrix
	
	#
	#  PUBLIC METHODS
	#
	
	def get_dim(self):
		"""Retorna una copia 'superficial' (por valor) de la dimension"""
		dim = copy.copy(self.__dimMatrix)
		return dim
	
	def get_matrix(self):
		"""Retorna una copia 'superficial' (por valor) de la matriz"""
		matrix = copy.copy(self.__matrix)
		return matrix
	
	def add_entry(self):
		"""Agrega los datos de un nodo (nueva fila y columna)
		Retorna la nueva dimension de la matriz"""
		try:
			new = []
			dim = self.__dimMatrix
			for i in range(dim):
				new.append(0)
			self.__matrix.append(new)
			dim += 1
			self._Matrix__dimMatrix += 1
			for i in range(dim):
				self.__matrix[i].append(0)
		except:
			return False
		return True
	
	def del_entry(self, target):
		"""Para un indice "target":
		Elimina los datos de un nodo (fila & columna respectiva)
		Retorna la nueva dimension de la matriz"""
		try:
			self.__matrix.pop(target)
			for i in self.__matrix:
				self.__matrix[i].pop(target)
			self._Matrix__dimMatrix -= 1
		except:
			return False
		return True
	
	def symmetry(self):
		"""Determina si la matriz es simetrica o no
		Retorna 'True' si es simetrica, 'False' si no lo es"""
		dim = self.__dimMatrix
		for i in dim:
			for j in dim:
				if j <= i:
					continue
				if self.__matrix[i][j] != self.__matrix[j][i]:
					return False
		return True
	
	def set_entry(row, col, value):
		"""Inserta un valor en el elemento (row, col) de la matriz"""
		self.__matrix[row][col] = value
	
	def num_relations(self, entry):
		dim = self.__dimMatrix
		relations = 0
		for i in dim:
			if self.__matrix[node][i] != 0:
				relations += 1
		return relations


class Graph:
	"""Clase que representa un grafo en un determinado momento
	Utiliza la Matriz de Adyacencia/Incidencia"""
	
	def __init__(self):
		self.__matrix = Matrix(0)
		self.__nodes = 0
	
	#
	#  PRIVATE METHODS
	#
	
	def __validate_target(self, target):
		dim = self.__matrix.get_dim()
		if target >= 0 and target < dim
			return True
		print "Invalid Target!"
		return False
	
	#
	#  PUBLIC METHODS
	#
	
	def add_node(self):
		return self.__matrix.add_entry()
	
	def del_node(self, node):
		if self.__validate_target(node):
			return self.__matrix.del_entry(node)
		return False
	
	def change_relation(self, orig, dest, weight):
		"""Para dos indices 'orig' y 'dest', y un peso de camino 'Weight':
		Modifica (o setea) una relacion entre dos nodos
		Retorna 'False' si los indices no son validos, 'True' en otro caso"""
		if self.__validate_target(orig) and self.__validate_target(dest):
			self.__matrix.set_entry(orig, dest, weight)
			return True
		return False
	
	def get_matrix(self):
		"""Retorna una copia de la Matriz de Incidencia/Adyacencia"""
		return self.__matrix.get_matrix()
	
	def directed(self):
		"""Determina si el grafo es dirigido o no dirigido"""
		return self.__matrix.symmetry()
	
	def connected(self):
		pass
	
	def complete(self):
		"""Determina si el grafo es completo o no
		Retorna 'True' si es completa, 'False' si no lo es"""
		cantNodos = self.__nodes
		for i in cantNodos:
			if self.degree(i) != (cantNodos - 1):
				return False
		return True
	
	def bipartite(self):
		color1 = 1
		color2 = 2
		matrix = self.__matrix.get_matrix()
		dim = self.__matrix.get_dim()
		colored = []
		for i in dim:
			colored.append(0)
		
		for i in dim:
			for j in dim:
				if colored[i] == 0:
					colored[i] = 1
				if matrix[i][j] != 0:
					if colored[j] == 0 and colored[i] == 1
						colored[j] == 2
					if colored[j] == 0 and colored[i] == 2
						colored[j] == 1
					if colored[j] != 0 and colored[i] == colored[j]
						return False
		return True
	
	def degree(self, node):
		"""Para un nodo 'node':
		Retorna el grado del nodo"""
		if self.__validate_target(node):
			return self.__matrix.num_relations()
		return None
