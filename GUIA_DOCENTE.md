# Guia docente — Practica CI/CD con Jira, GitHub y version

## Objetivo de aprendizaje
Que el estudiante comprenda el flujo real de entrega de software:

Ticket Jira → Rama → Cambio en codigo → Prueba → Commit → Pull Request → Pipeline → Version → Release.

## Duracion sugerida
60 a 90 minutos.

## Antes de clase
1. Crear un repositorio en GitHub.
2. Subir el contenido de esta carpeta.
3. Activar GitHub Actions.
4. Compartir el enlace del repositorio a los estudiantes.
5. Pedir que trabajen en grupos.

## Desarrollo de clase

### Momento 1 — Lectura del ticket
Pregunte:
- ¿Que solicita negocio?
- ¿Que modulo se afecta?
- ¿Que riesgo tiene el cambio?
- ¿Que evidencia se requiere para aceptar el cambio?

### Momento 2 — Cambio en codigo
Los estudiantes deben corregir `app/descuentos.py`.

### Momento 3 — Pruebas
Deben ejecutar `pytest -q`.
La prueba `test_descuento_cliente_frecuente` debe pasar despues del cambio.

### Momento 4 — CI/CD
Deben crear Pull Request y validar el pipeline.

### Momento 5 — Release
Deben proponer version `v1.0.1`, nota de release y plan de rollback.

## Pregunta de cierre
¿El cambio termina cuando el codigo funciona o cuando queda trazado, probado, versionado y desplegable?

## Respuesta esperada
El cambio termina cuando queda trazado, probado, versionado, revisado y listo para desplegarse de forma controlada.
