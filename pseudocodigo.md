# Pseudocódigo de `main_menu.py`

Descripción: Pseudocódigo en español que representa el flujo y las funciones principales del programa.

Inicio
1. Definir función extraer_e_imprimir_lineas(ruta_archivo_md, numeros_de_linea=None, rango_lineas=None):
   1.1. Intentar abrir el archivo en modo lectura (utf-8).
   1.2. Leer todas las líneas en una lista `lineas`.
   1.3. Si `numeros_de_linea` está definido:
       - Para cada `num` en `numeros_de_linea`:
           - Si 1 <= num <= total_lineas:
               - Añadir "Línea num: contenido" a la lista de salida.
           - Si no: imprimir advertencia.
   1.4. Si `rango_lineas` está definido (inicio, fin):
       - Ajustar índices para slicing.
       - Para i desde inicio_idx hasta fin_idx-1:
           - Añadir "Línea i+1: contenido" a la lista de salida.
   1.5. Si hay líneas para imprimir, imprimirlas.
   1.6. Capturar FileNotFoundError -> imprimir mensaje de error.
   1.7. Capturar otras excepciones -> imprimir mensaje de error.
   1.8. Fin función.

2. Definir funciones de opción (opcion_1 .. opcion_7):
   - opcion_1: imprimir encabezado; llamar extraer_e_imprimir_lineas(README.md, rango 2-13).
   - opcion_2: imprimir encabezado; llamar extraer_e_imprimir_lineas(README.md, rango 17-137).
   - opcion_3..opcion_7: imprimir encabezado correspondiente (placeholders).

3. Definir mostrar_menu():
   - Imprimir el menú con opciones 1..8 y mensajes decorativos.

4. Definir main():
   - Mientras True:
       - llamar mostrar_menu()
       - leer entrada del usuario como `eleccion`
       - Si eleccion == '1' -> llamar opcion_1()
       - Elif eleccion == '2' -> llamar opcion_2()
       - Elif eleccion == '3' -> llamar opcion_3()
       - Elif eleccion == '4' -> llamar opcion_4()
       - Elif eleccion == '5' -> llamar opcion_5()
       - Elif eleccion == '6' -> llamar opcion_6()
       - Elif eleccion == '7' -> llamar opcion_7()
       - Elif eleccion == '8' -> imprimir mensaje de salida; break
       - Else: imprimir "Opción no válida"; esperar Enter para continuar
   - Fin while

5. Si se ejecuta como script principal: llamar main()

Fin
