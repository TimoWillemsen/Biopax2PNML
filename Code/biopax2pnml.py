import biopax
import pnml
from models import *

class Convertor:
	def __init__(self, inputfile, outputfile):
		reader = biopax.Reader()
		net = reader.read(inputfile)
		writer = pnml.Writer(net)
		writer.write(outputfile)