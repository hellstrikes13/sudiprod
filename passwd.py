import random
import string
s = string.lowercase+string.digits+string.punctuation+string.uppercase
print ''.join(random.sample(s,8))
