'''

Given a infinite stream, pick k numbers. Each number should have equal probablity of being picked


pick the first k numbers from the stream  and store them in a chosenset

now for every other number in the stream, generate a random number R (0 to N)

if R lies in the range of 0 to k, then hold that value in the stream as "Val"
and,
	chosenset[R] = Val , swap that value out



'''