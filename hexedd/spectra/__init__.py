import os

import numpy as np

from praxes.physref import elam


class _ResourceManager(object):

    _root = os.path.join(os.path.split(__file__)[0], 'data')

    def __getitem__(self, key):
        temp = os.path.join(self._root, '%s.dat'%key)
        if os.path.isfile(temp):
            return temp
        raise KeyError(
            "'%s' is not a valid key. Try one of %s" % (key, self.keys())
            )

    def keys(self):
        return [
            i.rstrip('.dat') for i in os.listdir(self._root)
            if i.endswith('.dat')
        ]

resources = _ResourceManager()


class Spectrum(object):

    def __init__(self, key):
        fn = resources[key]
        e, i = np.loadtxt(fn, delimiter=',', skiprows=1, unpack=True)
        self.energy = e
        self.intensity = i

    def __call__(self, energy):
        return np.interp(energy, self.energy, self.intensity)


def load(key, composition, energy, thickness, by_mass=True, mass_density=None):
    """
    import numpy as np
    import quantities as pq
    from hexedd import spectra

    energy = np.linspace(1,300,300)*pq.keV # energy must be non-zero!
    # calculate the white beam spectrum for an A2 white beam through
    # an inch of iron:
    intensity = spectra.load('chess_a2', 'Fe', energy, 1.0*pq.inch)
    """
    t = elam.transmission_coefficient(
        composition, energy, thickness,
        by_mass=by_mass, mass_density=mass_density
        )
    return t * Spectrum(key)(energy)


def keys():
    return resources.keys()
