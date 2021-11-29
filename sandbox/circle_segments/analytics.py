import sympy as sy

y0, y1, g0, g1, x = sy.symbols("y_0 y_1 g_0 g_1 x")
theta = sy.symbols("theta")
pi = sy.pi
R, w, h, H = sy.symbols("R w h H")

r = 1

theta0 = 2*sy.acos(h/r)
theta1 = 2*sy.acos((h-w)/r)
A0 = r**2 * (theta0 - sy.sin(theta0))/2
A1 = pi*r**2 - r**2 * (theta1 - sy.sin(theta1))/2

eq1 = sy.Eq(sy.simplify(A0/(A0+A1)), sy.simplify(y0/(y0+y1)))
print(eq1)
#print(sy.solve(eq1, h))

phi0 = 2*sy.acos(H/R)
phi1 = 2*sy.acos((H-w)/R)

beta0 = sy.asin(H/R)
beta1 = sy.asin((H-w)/R)

xup0 = -R*sy.sin(beta0)
xdown0 = -R*sy.sin(beta1)
#
#B00 = sy.integrate(sy.sqrt(R**2-x**2)-H,(x, -R*sy.sin(beta0), x0) )
#print(sy.simplify(B00))
