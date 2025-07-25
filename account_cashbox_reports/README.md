# Account Cashbox Reports

Este módulo contiene todos los reportes para el sistema de Account Cashbox.

## Características

- Reporte de sesiones de caja con filtrado por fechas
- Detalle completo de cheques emitidos y recibidos
- Integración con l10n_latam_check para mostrar:
  - Número de cheque
  - Banco
  - CUIT del emisor
  - Fecha de pago
  - Importe
- Diseño profesional de PDF
- Control de caja por diario
- Resumen de movimientos por tipo

## Dependencias

- account_cashbox
- l10n_latam_check

## Instalación

Este módulo se instala automáticamente cuando account_cashbox está presente en el sistema y l10n_latam_check está disponible.

## Uso

1. Vaya a Facturación > Reportes > Reportes de Caja > Reporte de Sesiones
2. Seleccione el rango de fechas
3. Genere el reporte

## Funcionalidades del Reporte

- **Información de sesión**: Nombre, caja, estado, fechas, usuarios
- **Control de caja**: Saldos iniciales, movimientos, diferencias
- **Detalle de pagos**: Por diario, con tipos y métodos de pago
- **Detalle de cheques**: Separados en recibidos y emitidos
- **Resúmenes**: Totales por categoría
