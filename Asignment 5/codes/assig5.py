
import random

#clearly, any other correct sequence will give the same result. The value of correct is arbitrary.
correct = (9, 8, 7, 6) 
count = 0
#tried with 10 ** 5, too much variation
#loop is slow, but no alternative found
for i in range(10 ** 6):
    select = tuple(random.sample(range(10), 4))
    if select == correct:
        count += 1

print(count / 10 ** 6)
    

