from django.db import models


class Product(models.Model):
    STATUS_CHOICES = [
        ("Disponible", "Disponible"),
        ("Bajo stock", "Bajo stock"),
        ("Agotado", "Agotado"),
    ]

    name = models.CharField("Nombre", max_length=120)
    sku = models.CharField("SKU", max_length=30, unique=True)
    category = models.CharField("Categoría", max_length=60)
    location = models.CharField("Ubicación", max_length=80)
    quantity = models.PositiveIntegerField("Cantidad", default=0)
    unit_price = models.DecimalField("Precio unitario", max_digits=10, decimal_places=2, default=0)
    status = models.CharField("Estado", max_length=20, choices=STATUS_CHOICES, default="Disponible")
    description = models.TextField("Descripción", blank=True)
    created_at = models.DateTimeField("Creado", auto_now_add=True)
    updated_at = models.DateTimeField("Actualizado", auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self) -> str:
        return f"{self.name} ({self.sku})"

    @property
    def stock_value(self):
        return self.quantity * self.unit_price
