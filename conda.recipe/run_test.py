import os
import sys
import unittest

suite = unittest.TestLoader().discover('hexedd')
unittest.TextTestRunner(verbosity=1).run(suite)
