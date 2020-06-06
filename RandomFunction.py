'''
wapp to generate a random movie
'''
import random
marvel_movies=["ironman","antman","dr.strange","avengers","capt.america","civil war","thor","endgame","inifinity war"]

r1=random.randrange(len(marvel_movies))
print(marvel_movies[r1])


r2=random.randint(0,len(marvel_movies)-1)
print(marvel_movies[r2])