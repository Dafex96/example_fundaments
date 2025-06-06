
while True:
    try:
        cant = int(input("Ingrese la cantidad de empleados a registrar: "))
        break
    except ValueError:
        print("Debe ingresar un numero entero, intente nuevamente.")

mas_de_10 = 0
menor_o_ig_10 = 0

for _ in range(cant):
    
    nombre = input("Ingrese el nombre del empleado: ")
    
    while True:
        try:
            years = int(input("Ingrese los años de antigüedad del empleado: "))
            break
        except ValueError:
            print("Debe ingresar un numero entero, intente nuevamente.")
    
    if years > 10:
        print("Mas de 10 años de antigüedad")
        mas_de_10 += 1
    else:
        print("Menos de 10 años de antigüedad")
        menor_o_ig_10 += 1

print(f"Se registraron {mas_de_10} empleados con mas de 10 años de antiguedad")
print(f"Se registraron {menor_o_ig_10} empleados con 10 años o menos de antiguedad")