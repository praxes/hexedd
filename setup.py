from setuptools import Command, find_packages, setup

import versioneer


cmdclass = versioneer.get_cmdclass()


class test(Command):

    """Run the test suite."""

    description = "Run the test suite"

    user_options = [('verbosity', 'v', 'set test report verbosity')]

    def initialize_options(self):
        self.verbosity = 0

    def finalize_options(self):
        try:
            self.verbosity = int(self.verbosity)
        except ValueError:
            raise ValueError('Verbosity must be an integer.')

    def run(self):
        import unittest
        suite = unittest.TestLoader().discover('hexedd')
        unittest.TextTestRunner(verbosity=self.verbosity+1).run(suite)

cmdclass['test'] = test


package_data = {
    'hexedd': [
        'spectra/data/*.dat'
        ]
    }


setup(
    name = 'hexedd',
    packages = find_packages(),
    version = versioneer.get_version(),
    package_data = package_data,
    cmdclass = cmdclass,
    )
