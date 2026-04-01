import numpy as np
taxi = np.genfromtxt('nyc_taxis.csv', delimiter=',', skip_header = True)
 

# 1. What is the mean speed of the Cab rides

# speed = trip distance / trip length

speed = taxi[:, 7]/ taxi[:, 8]/3600
meanspeed = speed.mean()
print(meanspeed)


# calculate the number of rides taken in the month of february. 

rides_feb = taxi[taxi[:, 1]  == 2, 1]
print(rides_feb.shape[0])


# calculate number of rides with a trip greater than $50

print(taxi[taxi[:, -3] > 50, -3].shape[0])


# calculate number of rides where drop was jfk airport

print(taxi[taxi[:, 6] == 2, 6].shape[0])