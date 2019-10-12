from timeit import default_timer as timer
from GCD import GCD_alg
import sys

#print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
r = GCD_alg(21, 49)
#r= GCD_alg( 18446744073709551615 ,  4294967295 )
#r = GCD_alg(26213124689646513002165056522,3194548592524452535451541165465565)
#f = open('text.txt', 'w')
#f.write(str(r.gcd)+"GCD\n")
#f.write(str(r.B)+"D\n")
#f.write(str(r.times[0])+"Time\n")
#f.write(str(r.op1)+" "+str(r.op2))
#f.close()

print(str(r.op1)+" "+str(r.op2))
print("GCD: "+str(r.gcd))
print("Num of dec signs: "+str(r.B))
print("Time: "+str(r.times))

