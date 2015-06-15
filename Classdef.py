"""Various python classes planetary usage
Author: C. Grima (cyril.grima@gmail.com)
"""

from planetbody import spheroid
from planetbody import orbit


class Body:
	"""Planet class (name, adjective, acronym, parent)
	in respect with the ecliptic (Earth)
	"""
	def __init__(self, category, name, adjective, acronym, parent, mass, radius,
                 rotation, semimaj, apoapsis, periapsis,
                 axtilt, inclination, periarg, ascnode):
		self.category = category
		self.name = name
		self.adjective = adjective
		self.acronym = acronym
		self.parent = parent  # parent body
		self.mass = mass  # mass [kg]
		self.radius = radius  # equatorial radius {a, b, c} [m]
		self.rotation = rotation  # rotation [days]
		self.semimaj = semimaj  # semimajor axis [m]
		self.apoapsis = apoapsis  # apoapsis radius [m]
		self.periapsis = periapsis  # periaspsis radius [m]
		self.axtilt = axtilt  # rotation axis tilt [deg]
		self.inclination = inclination  # orbit plan inclination [deg]
		self.periarg = periarg  # longitude of the periapsis argument [deg]
		self.ascnode = ascnode  # Ascending node [deg]

		# Defined from above constants
		self.area = spheroid.area(self.radius['a'], self.radius['c'])
		self.density = spheroid.density(self.mass, self.radius['a'], self.radius['c'])
		self.ellipticity = spheroid.ellipticity(self.radius['a'], self.radius['c'])
		self.flattening = spheroid.flattening(self.radius['a'], self.radius['c'])
		self.volume = spheroid.volume(self.radius['a'], self.radius['c'])
		self.radius_mean = spheroid.radius_volumic(self.volume)
		self.gravity = spheroid.gravity(self.radius_mean, self.mass)
