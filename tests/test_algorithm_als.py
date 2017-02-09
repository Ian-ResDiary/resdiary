import unittest
import sys, os
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql.dataframe import DataFrame
from stubs import stub_algorithm
from test_superclass import *

# Append the source directory to the system path
# so that we can import the files for testing
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src/recommenders'))
import ALS as algorithm

class ALSAlgorithmTest(BaseTestCase):

	@classmethod
	def setUpClass(self):
		self.data = SQLContext(self.sc).read.csv(
	        os.path.dirname(__file__)+'/stubs/StubBookings.txt',
	        header=True,
	        inferSchema=True,
	        nullValue='NULL'
                )
                self.model = algorithm.ALS(self.sc)

	def test_main(self):
		# Check for detection of empty RDD
		self.assertRaises(ValueError, self.model.predict,
                                  self.sc.parallelize([]))

		# Check that an exception is thrown if wrong argument provided
		self.assertRaises(TypeError, self.model.train, ['foo', 'bar'])


	@classmethod
	def tearDownClass(self):
		del self.data
