# Practica CI/CD: Del ticket Jira al cambio en codigo

## Contexto
La empresa tiene un sistema de tienda digital. El equipo de negocio reporto un error en el calculo de descuentos para clientes frecuentes.

## Ticket Jira simulado

**Codigo:** SI-104  
**Tipo:** Bug / Change Request  
**Prioridad:** Media  
**Modulo afectado:** Descuentos  

**Descripcion:**  
El sistema aplica 5% de descuento a todos los clientes. Negocio solicita que los clientes con mas de 5 compras reciban 10%.

## Regla esperada

- Si `compras_cliente > 5`, descuento = `0.10`
- Si `compras_cliente <= 5`, descuento = `0.05`

## Actividad del estudiante

1. Crear una rama:
   ```bash
   git checkout -b feature/SI-104-ajuste-descuento
   ```

2. Corregir el archivo:
   ```text
   app/descuentos.py
   ```

3. Ejecutar pruebas:
   ```bash
   pip install -r requirements.txt
   pytest -q
   ```

4. Hacer commit:
   ```bash
   git add .
   git commit -m "SI-104 Ajusta regla de descuento para clientes frecuentes"
   ```

5. Subir cambios y crear Pull Request.

6. Validar que el pipeline de GitHub Actions pase correctamente.

## Evidencia que deben entregar

- Captura del ticket Jira simulado.
- Nombre de la rama.
- Codigo corregido.
- Captura de pruebas exitosas.
- Captura del Pull Request.
- Captura del pipeline exitoso.
- Version propuesta: `v1.0.1`.
- Nota de release.
- Riesgo del cambio.
- Plan de rollback.

## Nota de release sugerida

**Version:** v1.0.1  
**Cambio:** SI-104 Ajuste de regla de descuento para clientes frecuentes.  
**Impacto:** Corrige calculo comercial para clientes con mas de 5 compras.  
**Riesgo:** Bajo.  
**Rollback:** Revertir a version v1.0.0 o revertir el commit asociado al ticket SI-104.
