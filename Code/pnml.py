import xml.etree.cElementTree as ET
ET.register_namespace('pnml','http://www.pnml.org/version-2009/grammar/pnml')

class Writer:
	def __init__(self, net):
		self.elementcount = 0
		self.net = net

	#Return a new identifier
	def uniqueId(self, prefix='id'):
		self.elementcount += 1
		return prefix + str(self.elementcount)

	def writeName(self, parent, nameValue):
		name = ET.SubElement(parent, 'name')
		nameText = ET.SubElement(name, 'text')
		nameText.text = nameValue

	def writePlace(self, parent, place):
		if not place.id:
			place.id = self.uniqueId('p') 
		placeElement = ET.SubElement(parent, 'place', {
			'id': place.id
			})
		self.writeName(placeElement, place.description)

	def writeTransition(self, parent, transition):
		uid = self.uniqueId('t')
		transitionElement = ET.SubElement(parent, 'transition', {
			'id': uid
			})
		transition.id = uid;

	def writeArc(self, parent, arc):
		uid = self.uniqueId('a')
		arcElement = ET.SubElement(parent, 'arc',{
			'id': uid,
			'source': arc.source.id,
			'target': arc.target.id
			})
		return uid

	def prepare(self):
		self.root = ET.Element('pnml');	
		net = ET.SubElement(self.root, 'net', {
			'type': 'http://www.pnml.org/version-2009/grammar/ptnet',
			'id': self.uniqueId('id-')
			})

		page = ET.SubElement(net, 'page', {
			'id': 'top-level'			
			})
		return page

	def write(self, location):
		page = self.prepare()

		self.writeName(page, self.net.description)

		for place in self.net.places:
			self.writePlace(page, place)

		for transition in self.net.transitions:
			self.writeTransition(page, transition)

		for arc in self.net.arcs:
			self.writeArc(page, arc)

		tree = ET.ElementTree(self.root)
		tree.write(location)