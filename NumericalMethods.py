class NumericalMethods:
  @staticmethod
  def newton_raphson(f, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
      fx = eval(f, {"x": x})
      h = 1e-6
      dfx = (eval(f, {"x": x + h}) - fx) / h

      if abs(dfx) < tol:
        raise ValueError("La derivada es cero. No se puede aplicar el método de Newton-Raphson.")
          
      x_new = x - fx / dfx
      # print(f"Iteración {i+1}: x = {x_new}, f(x) = {fx}")    
      print(f"Iteración {i+1}: x = {x_new}")      
      if abs(x_new - x) < tol:
        return x_new
      x = x_new
    raise ValueError("No se encontró una solución en el número máximo de iteraciones.")


  @staticmethod
  def runge_kutta(f, y0, x0, xf, h):
    n_steps = NumericalMethods.__calculate_steps(xf,x0,h)
    
    x = [0]*(n_steps + 1)
    y = [0 for _ in range(n_steps + 1)]

    x[0] = x0
    y[0] = y0

    for i in range(n_steps):
        k1 = h * eval(f, {"x": x[i], "y": y[i]})
        k2 = h * eval(f, {"x": x[i] + h/2, "y": y[i] + k1/2})
        k3 = h * eval(f, {"x": x[i] + h/2, "y": y[i] + k2/2})
        k4 = h * eval(f, {"x": x[i] + h, "y": y[i] + k3})

        x[i+1] = x[i] + h
        y[i+1] = y[i] + (k1 + 2*k2 + 2*k3 + k4) / 6
    
    return x, y

  @staticmethod
  def euler_method(f, y0, x0, xf, h):
    n_steps = NumericalMethods.__calculate_steps(xf,x0,h)
    
    x = [0]*(n_steps + 1)
    y = [0 for _ in range(n_steps + 1)]

    x[0] = x0
    y[0] = y0

    for i in range(n_steps):
        x[i+1] = x[i] + h
        y[i+1] = y[i] + h * eval(f, {"x": x[i], "y": y[i]})
    
    return x, y

  def __calculate_steps(xf,x0,h):
    return int((xf - x0) / h)