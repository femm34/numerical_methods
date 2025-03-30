class NumericalMethods:
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