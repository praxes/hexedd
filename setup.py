from setuptools import find_packages, setup

import versioneer

setup(
    name='hexedd',
    packages=find_packages(),
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    )
