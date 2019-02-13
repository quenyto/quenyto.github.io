import hashlib, getpass, time, gc, Tkinter, base64

Q = 'WydFbmRpbmcgY2hlY2tpbmcgYmFsYW5jZSBvbiA1LzE4IHN0YXRlb'
Q += 'WVudCAoJFhYWFhYLlhYKTogJywgJ0ZpcnN0IGxldHRlcnMgb2Ygd'
Q += 'GhlIGxhc3QgbmFtZXMgb2YgdGVhY2hlcnMsIGdyYWRlcyAxIHRoc'
Q += 'm91Z2ggNSAobG93ZXJjYXNlKTogJywgJ0RhdGUgb2Ygc2Vjb25kI'
Q += 'HZhcmljZWxsYSB2YWNjaW5hdGlvbiAoTU0vREQvWVlZWSk6ICdd'
U = 'WydoYXNobGliLnNoYTI1NicsICdnZXRwYXNzLmdldHBhc3MnLCAna'
U += 'C5oZXhkaWdlc3QnXQ=='
I = 'WzMyLCAyMCwgMTMyNDQwMDksIDgxMjc5MTAxLCAzMzMzMywgMjYsI'
I += 'DQzOSwgMTZd'
E = 'WyJlZShZLDEpKGYoQykgJSAoMjYgKiogMjApKS5yanVzdCgxMiwgJ'
E += '3onKSIsICcocFswXS51cHBlcigpICsgcFsxOihMIC0gMildICsgI'
E += 'i4iICsgc3RyKE4pKVswOkxdJ10='
T = 'WydJbnNlcnQga2V5OiAnLCAnUGFzc3dvcmQgaGFzIGJlZW4gY29wa'
T += 'WVkIHRvIHRoZSBjbGlwYm9hcmQuLi5cblByZXNzIEVOVEVSIHdoZ'
T += 'W4gZmluaXNoZWQuJ10='
L = 'bGFtYmRhIGFycjogc3VtKFt4ICUgZShJKVszXSBmb3IgeCBpbiBhc'
L += 'nJdKSAlIGUoSSlbNl0='
Y = 'WydsYW1iZGEgaDogaW50KGguaGV4ZGlnZXN0KCksIGUoSSlbN10pJ'
Y += 'ywgImxhbWJkYSBuOiAnJy5qb2luKGNocihvcmQoJ2EnKSArIHApI'
Y += 'GZvciBwIGluIGQobikpWzo6LTFdIiwgJ2xhbWJkYSBzOiBlZShVL'
Y += 'DApKHMpJywgJ2xhbWJkYSBzOiBlZShZLDApKGVlKFksMikocykpJ'
Y += 'ywgJ2xhbWJkYSBpOiBlZShZLDMpKHN0cihpKSknLCAnbGFtYmRhI'
Y += 'GFycjogcmVkdWNlKGxhbWJkYSBhLCBiOiBhIF4gYiwgYXJyLCAwK'
Y += 'Sdd'

e = lambda q: eval(eval('base64.b64dec' + 'ode')(q))
ee = lambda q, i: eval(e(q)[i])

ec = False
try:
  import sums as _
except ImportError:
  ec = False
else:
  ec = True

def d(n):
    while n:
        n, r = divmod(n - 1, e(I)[5])
        yield r

def f(arr):
  r = 0
  s = ''
  for i in range(e(I)[0]):
    for x in arr:
      s += hex(x)[i % len(hex(x))]
  h = ee(Y,2)('')
  v = ee(Y,0)
  for i in range(e(I)[4]):
    h.update(s + str(i))
    r = max(r, v(h))
  return ee(Y,4)(r)

def rct(C, xs, cs, iter=[-1]):
  if ee(Y,5)(C) == xs:
    return C
  for i in iter:
    zan = C[:]
    zan[i] = xs
    zan[i] = ee(Y,5)(zan)
    if e(L)(zan) == cs:
      return zan
  return C

k = ee(Y,3)(ee(U,1)(e(T)[0]))
l = len(e(Q))
C = [0] * l

for i in range(l):
  k = ee(Y,4)(k)
  x = ee(Y,3)(ee(U,1)(e(Q)[i]))
  C[i] = f([k, x])
  if i == l - 2 and ec:
    C = rct(C, _.xs, _.cs)
    if ee(Y,5)(C) == _.xs:
      break
  gc.collect()

if ec:
  C = rct(C, _.xs, _.cs, range(l))

#print 'xs = ', ee(Y,5)(C)
#print 'cs = ', e(L)(C)

L = e(I)[1]
N = (f(C) % e(I)[2]) % 10
p = ee(E,0)
p = ee(E,1)
gc.collect()

r = Tkinter.Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(p)
raw_input(e(T)[1])
r.clipboard_clear()
r.clipboard_append(" ")
r.update()
time.sleep(0.5)
r.destroy()


