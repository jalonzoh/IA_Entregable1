# Instrucciones para usar `main_menu.py`

Este documento explica cómo ejecutar y usar `main_menu.py` dentro de este repositorio (incluye pasos para generar y visualizar los diagramas). Está pensado para entornos de desarrollo (GitHub Codespaces, devcontainers) o máquinas Linux/WSL.

## Requisitos
- Python 3.8+ (para ejecutar el script).
- Para regenerar diagramas desde el menú (opción 9): Node.js y `@mermaid-js/mermaid-cli` (o `npx` disponible).
  - Alternativa: usar Docker (se incluyeron pasos en el repositorio para ejecutarlo desde el contenedor Node si no quieres instalar Node globalmente).
- `xdg-open` para abrir imágenes en Linux (normalmente presente en distribuciones). En macOS usa `open` y en Windows `start` (el script usa `BROWSER` env var como fallback).

## Archivos relevantes
- `main_menu.py` - script principal con el menú.
- `diagrama_clean.mmd` - fuente Mermaid del diagrama.
- `diagrama.png`, `diagrama.svg` - diagramas generados.
- `pseudocodigo_diagrama.png` - diagrama generado específico para pseudocódigo.
- `pseudocodigo.md` - pseudocódigo en texto.
- `puppeteer-config.json` - configuración para Puppeteer (usa Chromium en contenedor).

## Cómo ejecutar el menú
1. Abre una terminal en la raíz del repo.
2. Ejecuta:

```bash
python main_menu.py
```

3. Verás el menú con opciones numeradas. Ejemplos de uso:
- `1` Mostrar Tema/Problema/Solución (extrae líneas del `README.md`).
- `2` Mostrar información de los datasets (extrae rango del `README.md`).
- `3` Mostrar pseudocódigo (placeholder).
- `4` Ver diagrama: intentará abrir `pseudocodigo_diagrama.png` si existe, sino `diagrama.png`. Usa `xdg-open` o la variable de entorno `BROWSER`.
- `9` Submenú para regenerar diagramas con `npx mmdc` (elige PNG, SVG o ambos).
- `8` Salir.

## Regenerar diagramas sin instalar nada en la máquina
Si no quieres instalar Node localmente, puedes regenerar los diagramas dentro de un contenedor Docker (el repo ya fue probado con esto). Ejemplo:

```bash
docker run --rm -v "$PWD":/data -w /data node:20 bash -lc "apt-get update -qq && apt-get install -y chromium --no-install-recommends >/dev/null 2>&1; npm init -y >/dev/null 2>&1 || true; npm install @mermaid-js/mermaid-cli puppeteer-core --no-audit --no-fund >/dev/null 2>&1; npx mmdc -i diagrama_clean.mmd -o diagrama.png --puppeteerConfigFile puppeteer-config.json"
```

Para generar SVG cambia `-o diagrama.png` por `-o diagrama.svg` (o genera ambos con dos comandos).

## Uso de la variable `BROWSER`
Si `xdg-open` no funciona en tu entorno, puedes exportar `BROWSER` con la ruta a tu navegador y el script intentará abrir el archivo `.mmd` con `file://`:

```bash
export BROWSER=/usr/bin/firefox
python main_menu.py
# seleccionar opción 4
```

## Notas y recomendaciones
- Para uso interactivo en Codespaces o entornos remotos, `xdg-open` puede no funcionar correctamente. En ese caso descarga el archivo `diagrama.png` desde el repositorio o abre `diagrama.svg` en el navegador.
- El submenú opción `9` invoca `npx mmdc`. Si `npx` no existe, el script mostrará un mensaje indicándolo.
- Si quieres que el script instale dependencias automáticamente, coméntamelo (es posible pero requiere `npm`/`apt` y privilegios).

---

Si quieres, puedo:
- Añadir estas instrucciones al README principal.
- Crear un `Makefile` o script `scripts/generate_diagrams.sh` para automatizar la regeneración.

