import hashlib, getpass, time, base64, gc, Tkinter

def d(n):
    while n:
        n, r = divmod(n - 1, 26)
        yield r

def a(n):
  return ''.join(chr(ord('a') + p) for p in d(n))[::-1]

def b(q):
  return eval(base64.b64decode(q[::-1]))

Q = 'dZTNyEGaz5iYpxGazFGagwyJuQWZoNXaulmZg4WZodHISVEVOVEIzNXZyBlbc5iLuQmch9mYwlGbjBSZoRHIvRHIkVWaw92Yg4WZlJGIzFGagQmcvd3czFGUnACLnAiOpU2chNmcld3bshCI1ACanV3byhGdgEDIzVGZhJ3ZgwycyVGajFWZ0BiZvBycl1WYuBCdzFGbgUGa0BiZvBycyVGd0VGbgQ3cylmRnACLnAiOpgFWugFWYhFWkgCI05WZtVGdhR3cggTMvUDIu9GIlNmbhxWYiByZul2ajVGajByZulGZuV0JgwyJgoTKZlVWZ9CRE9STNhCIu9Wa0FmbpN2YhZHIhxGblNWayFmdgQmbvNWZzBiZvBSZ0FGRnACLnAiO5V2agQnclNnbJdyW'

k = getpass.getpass(b(Q)[0])
h = b(Q)[-1](k)

for i in range(len(b(Q)) - 3):
  h.update(getpass.getpass(b(Q)[i+1]))
  gc.collect()

N = T = B = long(h.hexdigest(), 16)
for i in range(9999):
  h.update(k + str(pow(6733, i, 7011023)))
  f = k + str(i) + h.hexdigest()
  g = long(b(Q)[-1](f).hexdigest(), 16) ^ B
  N = g % 10 if (i + g + N) % 10 == 0 else N
  T = max(g, T)
  B = min(g, B)

L = len(k) * 4 - 14 
pL = max(min(L, 22), 7)
p = a((T ^ B) % (26 ** 20)).rjust(12, 'z')
p = (p[0].upper() + p[1:(pL - 2)] + "." + str(N))[0:L]
h = L = pL = T = B = 0
gc.collect()

r = Tkinter.Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(p)
raw_input(b(Q)[-2])
r.clipboard_clear()
r.clipboard_append(" ")
r.update()
time.sleep(0.5)
r.destroy()
