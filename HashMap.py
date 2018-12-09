import copy
class MapItem:
	def __init__(self, key, value):
		self.key = key
		self.value = value

class HashMap:
	def __init__(self):
		self.map = [None] * 8
		self.filled = 0
		
		
	def insert(self, key, value, resizing=False):
		if not resizing:
			self.filled += 1

		
			
		h = hash(key)

		idx = h % (len(self.map) - 1)
		map_item = MapItem(key, value)
		
		if not self.map[idx]:
			self.map[idx] = [map_item]
		else:
			self._append_to_map(self.map[idx], idx, map_item)
		
		#2/3 rule
		if self.filled > len(self.map) * (2 / 3):
			self._resize()
			
	def _append_to_map(self, arr, idx, to_add):
		added = False
		for i, item in enumerate(arr):
			if item.key == to_add.key:
				added = True
				self.map[idx][i] = to_add
				break
		if not added:
			arr = self.map[idx]
			self.map[idx] = arr + [to_add]
			

	def get(self, key):
		idx = hash(key) % (len(self.map) - 1)
		if self.map[idx]:
			arr = self.map[idx] 
			for item in arr:
				if item.key == key:
					return item.value
			return None
		else:
			return None
		
		
	def _resize(self):
		new_size = len(self.map) * 2
		print("Resizing to: ", new_size)
		table_copy = copy.deepcopy(self.map) 
		
		self.map = [None] * new_size
		
		for l in table_copy:
			if l:
				for item in l:
					self.insert(item.key, item.value, True)
			
		
	def print_map(self):
		for l in self.map:
			if l:
				for item in l:
					print(item.key, item.value)

m = HashMap()
m.insert("a", 1)
m.insert("aa", 2)
m.insert("aaa", 3)
m.insert("aaaa", 4)
m.insert("aaaaa", 5)
m.insert("aaaaaa", 6)
m.insert("aaaaaaa", 7)
m.insert("aaaaaaaa", 8)
m.insert("aaaaaaaaa", 9)
m.insert("aaaaaaaaaa", 10)
m.insert("aaaaaaaaaaa", 11)
m.insert("aaaaaaaaaaaa", 12)

m.insert(None, 13)
print(m.get(None))

	

