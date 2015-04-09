import math

# Determine which topology of the four nodes is most likely
def quartet_query(x, a1, a2, a3):
	score1 = jukes_cantor_distance(x, a1) + jukes_cantor_distance(a2, a3)
	score2 = jukes_cantor_distance(x, a2) + jukes_cantor_distance(a1, a3)
	score3 = jukes_cantor_distance(x, a3) + jukes_cantor_distance(a1, a2)
	scores = [score1, score2, score3]
	print scores
	return scores.index(min(scores))
	
# Determine which subtree of internal node v we should add x to
def node_query(T, v, x):
	print "node query"
	
# Compute the jukes-cantor distance between two (aligned) sequences
def jukes_cantor_distance(x, y):
	# Compute the number of differences
	numDiffs = 0
	for index in range(0, len(x)):
		if (x[index] != y[index]):
			numDiffs += 1
    
	if (numDiffs == 0):
		distance = 0.0
	else:
		# TODO: Check what to do here
		if (float(numDiffs) / len(x)) > 0.75:
			distance = float("inf")
		else:
			distance = -0.75 * math.log(1 - (4.0 / 3.0) * (float(numDiffs) / len(x)), math.e)
	return distance