from thefuzz import fuzz
from thefuzz import process

import particle

fuzzyargs = ["I think your mom is nice", "I think your mommy's nice"]

print(particle.similarity(fuzzyargs[0],fuzzyargs[1]))
print(fuzz.ratio(fuzzyargs[0],fuzzyargs[1]))