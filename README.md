# Proyecto Integrador: Generador Seguro de Contraseñas

**Nombre del Proyecto:** El impacto de las nuevas tecnologías en la sociedad: Solución de Ciberseguridad
**Nmobre y apellido** Fabian Gonzalez
**Fecha:** 28 de Junio de 2026

## Objetivo del Sistema

Desarrollar una herramienta de software que automatice la creación de contraseñas seguras mediante cadenas de caracteres aleatorias, respondiendo a la necesidad actual de proteger la información personal frente a las crecientes amenazas tecnológicas.

## Descripción de Funcionalidades

1. **Configuración de Parámetros:** Permitir al usuario definir la longitud de la contraseña (validando que sea un mínimo de 8 caracteres por seguridad).

2. **Filtros Personalizados:** Integración de opciones lógicas para incluir letras mayúsculas, números y símbolos especiales.

3. **Generación Aleatoria:** Utilizar estructuras iterativas (bucles) para compilar una cadena segura basada en las elecciones del usuario.

4. **Validación de Errores:** El sistema detecta entradas inválidas (como ingresar letras en lugar de números) y vuelve a preguntar sin cerrarse.

## Diagramas del Sistema

### 1. Diagrama de Flujo (Lógica Funcional)

```mermaid
graph TD
    A([Inicio]) --> B[/Ingresar longitud de contraseña/]
    B --> C{¿Longitud < 8?}
    C -- Sí --> D[/Mostrar Error/]
    D --> B
    C -- No --> E[/Preguntar por: Mayúsculas, Números, Símbolos/]
    E --> F[Construir lista de caracteres válidos]
    F --> G[Generar contraseña aleatoria iterando con bucle FOR]
    G --> H[/Mostrar contraseña en pantalla/]
    H --> I([Fin])
graph TD
    UI[Capa de Presentación / Interfaz UI] -->|Envía Parámetros| LN(Capa de Lógica de Negocio)
    LN -->|Valida y Genera| LN
    LN -->|Envía Cadena Generada| OUT[Capa de Servicios y Salida Output]
    
    style UI fill:#d4e6f1,stroke:#2874a6,stroke-width:2px
    style LN fill:#f9e79f,stroke:#b7950b,stroke-width:2px
    style OUT fill:#d5f5e3,stroke:#1d8348,stroke-width:2px
