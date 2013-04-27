class PetriNet:
	def __init__(self, description):
		self.description = description;
		self.places = []
		self.transitions = []
		self.arcs = []

	def newPlace(self, place):
		for exisitingplace in self.places:
			if exisitingplace.id == place.id:
				print('Found duplicate place')
				return

		self.places.append(place)
	def newTransition(self, transition):
		self.transitions.append(transition)
	def newArc(self, arc):
		self.arcs.append(arc)

class Place:
	def __init__(self, uid, description):
		self.id = uid.rsplit('/',1)[1]
		self.description = description

class Arc:
	def __init__(self, source, target):
		self.source = source
		self.target = target

class Transition:
	def __init__(self):
		return