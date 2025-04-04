from NumericalMethods import NumericalMethods


# f = input("Introduce la ecuación diferencial: ")
# y0 = float(input("Introduce el valor inicial y0: "))
# x0 = float(input("Introduce el valor inicial x0: "))
# xf = float(input("Introduce el valor final xf: "))
# h = float(input("Introduce el tamaño del paso h: "))


# x_valores, y_valores = NumericalMethods.euler_method(f, y0, x0, xf, h)



# print("    ")
# print("Solución usando el método de Euler con h =", h)
# print("-" * 40)
# print("   x   |    y    ")
# print("-" * 40)
# for i in range(len(x_valores)):
#     print(f"{x_valores[i]:.1f}   |  {y_valores[i]:.6f}")
# print("-" * 40)
# print(f"El valor de y(1) es aproximadamente: {y_valores[-1]:.6f}")

# x_valores, y_valores = NumericalMethods.runge_kutta(f, y0, x0, xf, h)
# print("    ")
# print("Solución usando el método de Runge-Kutta con h =", h)
# print("-" * 40)
# print("   x   |    y    ")
# print("-" * 40)
# for i in range(len(x_valores)):
#     print(f"{x_valores[i]:.1f}   |  {y_valores[i]:.6f}")
# print("-" * 40)
# print(f"El valor de y(1) es aproximadamente: {y_valores[-1]:.6f}")









x_valores = NumericalMethods.newton_raphson("x**4 - 4", 10)
print("    ")
print("Solución usando el método de Newton-Raphson")
print("-" * 40)
print(x_valores)
# print("Solución usando el método de Newton-Raphson con h =", h)
# print("-" * 40)
# print("   x   |    y    ")
# print("-" * 40)
# for i in range(len(x_valores)):
#     print(f"{x_valores[i]:.1f}   |  {y_valores[i]:.6f}")
# print("-" * 40)
# print(f"El valor de y(1) es aproximadamente: {y_valores[-1]:.6f}")
# print("    ")
# print("Fin del programa")
# print("-" * 40)