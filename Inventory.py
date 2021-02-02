class Inventory:
	def __init__(self, sizeInItems = 10):
		self.__items = []
		self.__sizeInItems = sizeInItems
		self.__maxCarryWeight = 30
		self.__weight = 0
	def AddItemIfCan(self, item):
		if (len(self.__items) < self.sizeInItems):
			self.__items.Append(item)
			self.__weight += item.weight
			return True
		return False
	def RemoveItemByIndex(self, index):
		if (index > 0 and index < len(self.__items)):
			self.__weight -= self.__items[index].weight
			self.__items.pop(index)
			return True
		return False
	def AddRemoveMaxCarryWeight(self, carryWeight):
		newValue = self.__maxCarryWeight + carryWeight
		self.__maxCarryWeight = max(0, newValue)
		return True
	def GetItems(self):
		return self.__items
	def GetItem(self, index):
		if (index > len(self.__items) and index < len(self.__items)):
			return self.__items[index]
		raise Exception("Index out of range in items")
	def GetWeight(self):
		return self.__weight
	def GetMaxWeight(self):
		return self.__maxCarryWeight
	def GetSizeInItems(self):
		return self.__sizeInItems
	def AddRemoveSizeInItems(self, itemsSize):
		newValue = self.__sizeInItems + itemsSize
		self.__sizeInItems = max(0, newValue)
		return True
