def extraer_e_imprimir_lineas(ruta_archivo_md, numeros_de_linea=None, rango_lineas=None):
    """
    Extrae e imprime líneas específicas de un archivo Markdown.

    Args:
        ruta_archivo_md (str): La ruta al archivo Markdown.
        numeros_de_linea (list, optional): Una lista de números de línea (base 1)
                                          a extraer. Ej: [2, 5, 10].
        rango_lineas (tuple, optional): Una tupla (inicio, fin) de números de línea (base 1)
                                        para extraer un rango inclusivo. Ej: (3, 7).
    """
    try:
        with open(ruta_archivo_md, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines() # Lee todas las líneas en una lista
            total_lineas = len(lineas)

            lineas_a_imprimir = []

            if numeros_de_linea:
                print(f"\n--- Extrayendo líneas específicas: {numeros_de_linea} ---")
                for num in numeros_de_linea:
                    if 1 <= num <= total_lineas:
                        # Los índices de Python son base 0, por eso restamos 1
                        lineas_a_imprimir.append(f"Línea {num}: {lineas[num - 1].strip()}")
                    else:
                        print(f"Advertencia: La línea {num} está fuera del rango ({total_lineas} líneas).")

            if rango_lineas:
                inicio, fin = rango_lineas
                print(f"\n--- Extrayendo rango de líneas: {inicio} a {fin} ---")
                # Asegurarse de que el rango sea válido
                inicio_idx = max(0, inicio - 1)
                fin_idx = min(total_lineas, fin) # El slice de Python es exclusivo en el final

                for i in range(inicio_idx, fin_idx):
                    lineas_a_imprimir.append(f"Línea {i + 1}: {lineas[i].strip()}")

            # Imprimir las líneas recolectadas
            if lineas_a_imprimir:
                for linea in lineas_a_imprimir:
                    print(linea)
            else:
                print("No se encontraron líneas para imprimir con los criterios dados.")

    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo_md}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")



def opcion_1():
    print("\n--- Tema / Problema / Solucion ---")
    extraer_e_imprimir_lineas("/workspaces/IA_Entregable1/README.md", rango_lineas=(2, 13))


def opcion_2():
    print("\n--- Informacion de los Dataset ---")
    extraer_e_imprimir_lineas("/workspaces/IA_Entregable1/README.md", rango_lineas=(17, 137))    

def opcion_3():
    print("\n--- Pseudocodigo ---")
    #config = input("Ingresa el nuevo valor de configuración: ")
    #print(f"Configuración actualizada a: {config}")
    #input("\nPresiona Enter para continuar...")

def opcion_4():
    import subprocess
    import os

    print("\n--- Diagrama de Flujo ---")
    # Intentar abrir el PNG generado (prioriza pseudocodigo_diagrama.png)
    ruta_png = os.path.join(os.path.dirname(__file__), "pseudocodigo_diagrama.png")
    if not os.path.exists(ruta_png):
        ruta_png = os.path.join(os.path.dirname(__file__), "diagrama.png")
    ruta_mmd = os.path.join(os.path.dirname(__file__), "diagrama_clean.mmd")

    try:
        if os.path.exists(ruta_png):
            nombre = os.path.basename(ruta_png)
            print(f"Abriendo diagrama: {nombre}")
            # En entornos Linux, xdg-open abre el archivo con la aplicación por defecto
            subprocess.run(["xdg-open", ruta_png], check=False)
        elif os.path.exists(ruta_mmd):
            print("No se encontró PNG. Puedes visualizar el archivo .mmd con un renderizador Mermaid (ej: https://mermaid.live)")
            print(f"Ruta del archivo .mmd: {ruta_mmd}")
            # Intentar abrir el .mmd en el navegador por defecto del host si está configurado
            browser_cmd = os.environ.get("BROWSER")
            if browser_cmd:
                try:
                    print(f"Abriendo en navegador: {browser_cmd} -> {os.path.basename(ruta_mmd)}")
                    subprocess.run([browser_cmd, f"file://{ruta_mmd}"], check=False)
                except Exception:
                    pass
        else:
            print("No se encontró ningún diagrama en el proyecto. Genera 'diagrama.png' o 'diagrama_clean.mmd' primero.")

    except Exception as e:
        print(f"Error al intentar abrir el diagrama: {e}")

def opcion_5():
    print("\n--- Sugerencias por COPILOT ---")
    #config = input("Ingresa el nuevo valor de configuración: ")
    #print(f"Configuración actualizada a: {config}")
    #input("\nPresiona Enter para continuar...")

def opcion_6():
    print("\n--- Programa ---")
    #config = input("Ingresa el nuevo valor de configuración: ")
    #print(f"Configuración actualizada a: {config}")
    #input("\nPresiona Enter para continuar...")

def opcion_7():
    print("\n--- Instrucciones ---")
    #config = input("Ingresa el nuevo valor de configuración: ")
    #print(f"Configuración actualizada a: {config}")
    #input("\nPresiona Enter para continuar...")

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\n" + "="*30)
    print("      MENÚ PRINCIPAL")
    print("="*30)
    print("1. Tema / Problema / Solucion")
    print("2. Informacion de los Dataset")
    print("3. Pseudocodigo")
    print("4. Diagrama de Flujo")
    print("5. Sugerencias por Copilot")
    print("6. Mostrar Programa")
    print("7. Mostrar Instrucciones")
    print("9. Regenerar diagrama (PNG & SVG)")
    print("8. Salir")
    print("="*30)

def main():
    """Función principal que ejecuta el bucle del menú."""
    while True:
        mostrar_menu()
        eleccion = input("Por favor, selecciona una opción (1-8): ")

        if eleccion == '1':
            opcion_1()
        elif eleccion == '2':
            opcion_2()
        elif eleccion == '3':
            opcion_3()
        elif eleccion == '4':
            opcion_4()
        elif eleccion == '5':
            opcion_5()
        elif eleccion == '6':
            opcion_6()
        elif eleccion == '7':
            opcion_7()
        elif eleccion == '9':
            # Submenú para regenerar PNG, SVG, ambos o volver
            import subprocess, os
            ruta_mmd = os.path.join(os.path.dirname(__file__), "diagrama_clean.mmd")
            ruta_png = os.path.join(os.path.dirname(__file__), "diagrama.png")
            ruta_svg = os.path.join(os.path.dirname(__file__), "diagrama.svg")

            if not os.path.exists(ruta_mmd):
                print("No se encontró 'diagrama_clean.mmd'. Asegúrate de tener el archivo .mmd en el directorio del proyecto.")
                continue

            while True:
                print("\n--- Regenerar diagrama ---")
                print("1. Regenerar solo PNG")
                print("2. Regenerar solo SVG")
                print("3. Regenerar ambos (PNG + SVG)")
                print("4. Volver al menú principal")
                sub = input("Selecciona una opción (1-4): ")

                try:
                    if sub == '1':
                        print("Regenerando PNG...")
                        subprocess.run(["npx", "mmdc", "-i", ruta_mmd, "-o", ruta_png], check=False)
                        print("PNG generado:", ruta_png)
                        break
                    elif sub == '2':
                        print("Regenerando SVG...")
                        subprocess.run(["npx", "mmdc", "-i", ruta_mmd, "-o", ruta_svg], check=False)
                        print("SVG generado:", ruta_svg)
                        break
                    elif sub == '3':
                        print("Regenerando PNG y SVG...")
                        subprocess.run(["npx", "mmdc", "-i", ruta_mmd, "-o", ruta_png], check=False)
                        subprocess.run(["npx", "mmdc", "-i", ruta_mmd, "-o", ruta_svg], check=False)
                        print("Ambos archivos generados:", ruta_png, ruta_svg)
                        break
                    elif sub == '4':
                        break
                    else:
                        print("Opción no válida en el submenú. Intenta de nuevo.")

                except FileNotFoundError:
                    print("npx no está disponible. Instala Node.js y @mermaid-js/mermaid-cli para usar esta opción.")
                    break
                except Exception as e:
                    print(f"Error al regenerar el diagrama: {e}")
                    break
        elif eleccion == '8':
            print("\nSaliendo del programa. ¡Hasta luego!")
            break # Sale del bucle while y termina el programa
        else:
            print("\nOpción no válida. Por favor, intenta de nuevo.")
            input("Presiona Enter para continuar...") # Pausa si la opción es inválida

if __name__ == "__main__":
    main()