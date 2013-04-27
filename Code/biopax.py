import rdflib
from models import *
from rdflib import plugin
rdflib.plugin.register('sparql', rdflib.query.Processor, 'rdfextras.sparql.processor', 'Processor')
rdflib.plugin.register('sparql', rdflib.query.Result, 'rdfextras.sparql.query', 'SPARQLQueryResult')

class Reader:
	def __init__(self):
		self.net = PetriNet('')
		return
		#self.net = PetriNet()
	def read(self, inputfile):
		graph = rdflib.Graph()
		result = graph.parse(inputfile)


		query = """
			PREFIX bp: <http://www.biopax.org/release/biopax-level3.owl#>
			SELECT  ?left ?displayNameLeft ?right ?displayNameRight
			WHERE {
			    ?BiochemicalReaction bp:left ?left . 
			    ?BiochemicalReaction bp:right ?right .
			    ?left bp:displayName ?displayNameLeft . 
			    ?right bp:displayName ?displayNameRight
			}
		"""

		for x in graph.query(query):
			placeLeft = Place(x[0], x[1])
			placeRight = Place(x[2], x[3])
			transition = Transition()
			arcleft = Arc(placeLeft, transition)
			arcRight = Arc(transition, placeRight)

			self.net.newPlace(placeLeft)
			self.net.newPlace(placeRight)
			self.net.newTransition(transition)
			self.net.newArc(arcleft)
			self.net.newArc(arcRight)
			#print("left: %s right: %s" % x)

		return self.net

		#print("graph has %s statements." % len(graph))
		#namespaces = {'bp': 'http://www.biopax.org/release/biopax-level3.owl'}
		#print(self.root.nsmap)
		#description = self.root.findall('bp:BiochemicalReaction',namespaces=self.root.nsmap)
		#print(description)

	def readPlaces(self):
		return self.net.places
	def readTransitions(self):
		return self.net.transitions
	def readArcs(self):
		return self.net.arcs