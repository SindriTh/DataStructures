import random
from Stopwatch import *

timer = Stopwatch()
timer2 = Stopwatch()
lis = []
for i in range(0,10000):
    lis.append(i)


timer.StartTimer()
s = f"{50}nano"
timer.StopTimer()

lis = []
for i in range(0,10000):
    lis.append(i)


timer2.StartTimer()
s = "{}nano".format(50)
timer2.StopTimer()

print(f"The first process took {timer.GetDuration()/1000}ns or {timer.GetDuration()/1000000}ms")
print(f"The second process took {timer2.GetDuration()/1000}ns or {timer2.GetDuration()/1000000}ms")

# Öll þessi test gerð með lista sem er 10.000 stök af lengd.
# insert er helmingi hægara en append. Alltaf að nota append ef það er hægt.
# það er miklu hægara að eyða indexi sem kemur fyrr á listanum (Supposedly af því það þarf að shifta öllum hinum.)
# pop er fljótt, tekur kannski 5-15ns
# reverse tekur svipað langan tíma og pop. count tekur langan tíma (150-300ns).
# clear tekur um 70-150ns
# fstrings nánast alltaf hraðari en format, en hægari en harðkóðað.