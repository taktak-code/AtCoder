import math

a, b, x = map(int,input().split())
#xが0.5*Vを超えるか超えないかで場合分け
if x > 0.5*a*a*b:
    y = 2*x/a/a - b
    tan = (b-y)/a
    ans = math.atan(tan)
    print(math.degrees(ans))

elif x < 0.5*a*a*b:
    y = 2*x/a/b
    tan = b/y
    ans = math.atan(tan)
    print(math.degrees(ans))

else:
    print("45.0000000000")