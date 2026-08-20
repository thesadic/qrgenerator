# Guía de contribución

Gracias por tu interés en contribuir a **QR Generator**. Este documento describe cómo reportar problemas, proponer mejoras y enviar cambios de forma que el proyecto se mantenga simple, usable y bajo control del maintainer.

Al participar, aceptás el [Código de Conducta](CODE_OF_CONDUCT.md).

## Antes de empezar

1. Revisá los [issues abiertos](https://github.com/thesadic/qrgenerator/issues) por si tu idea o bug ya está reportado.
2. Para errores, usá la plantilla de [bug report](.github/ISSUE_TEMPLATE/bug_report.md).
3. Para nuevas funciones, usá la plantilla de [feature request](.github/ISSUE_TEMPLATE/feature_request.md).
4. Si querés implementar un cambio sustancial, abrí primero un issue para alinearlo con el maintainer.

## Flujo de trabajo (Fork → Branch → PR)

1. **Fork** del repositorio en GitHub.
2. **Cloná** tu fork y añadí el remoto upstream:

   ```bash
   git clone https://github.com/<tu-usuario>/qrgenerator.git
   cd qrgenerator
   git remote add upstream https://github.com/thesadic/qrgenerator.git
   ```

3. **Creá una rama** desde `main` actualizado:

   ```bash
   git fetch upstream
   git checkout main
   git merge upstream/main
   git checkout -b feature/descripcion-corta
   # o: fix/descripcion-corta
   ```

4. **Hacé tus cambios**, con commits claros y enfocados (un tema por PR cuando sea posible).
5. **Probalo localmente** (ver [Pruebas locales](#pruebas-locales)).
6. **Push** a tu fork y abrí un **Pull Request** contra `main` del repositorio original, usando la [plantilla de PR](.github/PULL_REQUEST_TEMPLATE.md).
7. Esperá a que pase el **CI** de GitHub Actions (smoke test del CLI en varias versiones de Python). Un PR en rojo no se revisa para merge hasta que esté verde, salvo acuerdo explícito del maintainer.

## Regla de fusión (obligatoria)

**Ningún pull request se fusiona en `main` sin revisión y aprobación previa del maintainer.**

- Los PRs deben pasar por revisión humana.
- No se aceptan merges directos a `main` desde colaboradores sin aprobación.
- Si el maintainer pide cambios, actualizá la misma rama; no abras un PR nuevo salvo que se indique lo contrario.

## Estilo de código

El proyecto es un CLI mínimo. Mantené ese alcance.

- Mensajes al usuario en **español**, con prefijos `[INFO]`, `[WARN]`, `[SUCCESS]`, `[ERROR]`.
- Función principal: `generate_qr_pro(url, filename="qrcode_pro.png", logo_path=None)`.
- Con logo (o en general), usá corrección de errores **`ERROR_CORRECT_H`** (~30% de recuperación). No bajes el nivel si hay logo superpuesto.
- Logo centrado, máximo ~25% del ancho del QR (`qr_width // 4`).
- Docstrings en español para funciones públicas.
- Manejo de errores con `try/except` y mensaje claro; no hace falta un framework de logging.
- **No** añadir frameworks web, servicios online ni dependencias nuevas sin justificación clara y acuerdo en un issue.
- **No** commitear imágenes generadas, logos locales ni entornos virtuales/Conda.

## Pruebas locales

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# QR sin logo
python qrgenerator.py "https://ejemplo.com"

# QR con logo (reemplazá por una imagen local tuya)
python qrgenerator.py "https://ejemplo.com" /ruta/a/logo.png
```

Verificá que:

- Se imprime `[SUCCESS]` y se genera el PNG.
- Con logo, aparece `[INFO]` y el código sigue siendo escaneable.
- Con ruta de logo inexistente, aparece `[WARN]` y se genera un QR estándar.

En el PR, describí el comando usado y el resultado (ver plantilla).

## Mensajes de commit

Preferí mensajes concisos en imperativo, en español o inglés, por ejemplo:

- `fix: manejar logo RGBA sin canal alpha inválido`
- `docs: aclarar instalación con venv`

## Preguntas

Si algo no está claro, abrí un issue o comentá en el PR. Gracias por ayudar a mejorar el proyecto.
