import sympy as sp

def derivar_por_limite():
    print("==================================================")
    print("  MOTOR DE DERIVADAS POR DEFINICIÓN DE LÍMITE")
    print("==================================================\n")
    
    # 1. Definimos las variables: 'x' (nuestra variable) y 'h' (el incremento)
    x, h = sp.symbols('x h', real=True)
    
    # 2. Pedimos al usuario que ingrese una función
    print("Ejemplos válidos: x**2, sin(x), cos(x), exp(x), x**3 + 2*x")
    entrada_usuario = input("Ingresa la función f(x) a derivar: ")
    
    try:
        # Convertimos el texto del usuario a una expresión matemática de SymPy
        # CORRECCIÓN: 'locals' fuerza a SymPy a usar nuestras variables estrictas 'x' y 'h'
        f = sp.sympify(entrada_usuario, locals={'x': x, 'h': h})
    except sp.SympifyError:
        print("Error: La función ingresada no es válida.")
        return

    print(f"\n--- Analizando: f(x) = {f} ---")
    
    # p1: Evaluar f(x+h)
    # Reemplazamos todas las 'x' por 'x+h'
    f_xh = f.subs(x, x + h)
    print(f"\n[Paso 1] Evaluamos f(x+h):")
    print(f"f(x+h) = {f_xh}")
    
    # p1.5: Expansión (Polinomios y Trigonometría)
    # sp.expand(trig=True) fuerza a expandir sumas de ángulos como sin(x+h) o binomios como (x+h)^2
    f_xh_expandido = sp.expand(f_xh, trig=True)
    
    if f_xh != f_xh_expandido:
        print(f"\n[Paso 1.5] Expandimos los términos (Polinomios o Ángulos Trigonométricos):")
        print(f"f(x+h) = {f_xh_expandido}")
        f_xh = f_xh_expandido # Actualizamos con la versión expandida
        
    # p2: Restar f(x)
    numerador = f_xh - f
    print(f"\n[Paso 2] Construimos el numerador f(x+h) - f(x):")
    print(f"Numerador = {numerador}")
    
    # Simplificamos el numerador (cancela términos semejantes)
    numerador_simplificado = sp.simplify(numerador)
    if numerador != numerador_simplificado:
        print(f"Simplificando el numerador obtenemos:")
        print(f"Numerador = {numerador_simplificado}")
        
    # p3: Armar el cociente de Newton (dividir por h)
    cociente = numerador_simplificado / h
    print(f"\n[Paso 3] Armamos el cociente de diferencias (dividiendo por h):")
    print(f"Cociente = {cociente}")
    
    # p4: Aplicar el límite cuando h tiende a 0
    print(f"\n[Paso 4] Aplicamos el límite: lim(h->0) del cociente...")
    derivada = sp.limit(cociente, h, 0)
    
    print("\n==================================================")
    print(f" RESULTADO FINAL: f'(x) = {derivada}")
    print("==================================================\n")

if __name__ == "__main__":
    derivar_por_limite()