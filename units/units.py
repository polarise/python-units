#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
"""
units.units
Copyright (C) 2017  Paul K. Korir
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Paul K. Korir, PhD"
__email__ = "paul.korir@gmail.com"
__date__ = "2017-06-02"


from __init__ import SIUnit, DerivedUnit

# SI units
ampere = SIUnit.define('A')
candela = SIUnit.define('cd')
kelvin = SIUnit.define('K')
kilogram = SIUnit.define('kg')
metre = SIUnit.define('m')
mole = SIUnit.define('mol')
second = SIUnit.define('s')

# derived units
radian = DerivedUnit.define('rad', metre / metre)
steradian = DerivedUnit.define('sr', metre * metre / metre / metre)
hertz = DerivedUnit.define('Hz', SIUnit() / second)
newton = DerivedUnit.define('N', kilogram * metre / second / second)
pascal = DerivedUnit.define('Pa', newton / metre / metre)
joule = DerivedUnit.define('J', newton * metre)
watt = DerivedUnit.define('W', joule / second)
coulomb = DerivedUnit.define('C', second * ampere)
volt = DerivedUnit.define('V', watt / ampere)
farad = DerivedUnit.define('F', coulomb / volt)
ohm = DerivedUnit.define('Ω', volt / ampere)
siemens = DerivedUnit.define('S', ampere / volt)
weber = DerivedUnit.define('Wb', volt * second)
tesla = DerivedUnit.define('T', weber / metre / metre)
henry = DerivedUnit.define('H', weber / ampere)
degree_celcius = DerivedUnit.define('°C', kelvin)
lumen = DerivedUnit.define('lm', candela * steradian)
lux = DerivedUnit.define('lx', lumen / metre / metre)
becquerel = DerivedUnit.define('Bq', SIUnit() / second)
gray = DerivedUnit.define('Gy', joule / kilogram)
sievert = DerivedUnit.define('Sv', joule / kilogram)
katal = DerivedUnit.define('kat', mole / second)