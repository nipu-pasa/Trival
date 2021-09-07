from Spaces.Planet import Planet
from Spaces.calc import planet_mass, planet_vol
naboo = Planet('Naboo', 3000000, 8, 'Naboo System')
naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)
print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')
