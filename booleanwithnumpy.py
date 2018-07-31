# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
np.logical_or(my_house>18, my_house <10)

# Both my_house and your_house smaller than 11
np.logical_and(your_house<11, my_house <11)
