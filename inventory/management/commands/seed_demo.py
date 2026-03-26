from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from inventory.models import Product


class Command(BaseCommand):
    help = "Carga datos demo para EcoStock Sim"

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@ecostock.local", "admin123")
            self.stdout.write(self.style.SUCCESS("Usuario demo creado: admin / admin123"))

        demo_products = [
            {
                "name": "Sensor RFID UHF",
                "sku": "ECO-1001",
                "category": "RFID",
                "location": "A-01",
                "quantity": 18,
                "unit_price": 1450,
                "status": "Disponible",
                "description": "Sensor para lectura en portal logístico.",
            },
            {
                "name": "Etiqueta industrial",
                "sku": "ECO-1002",
                "category": "Consumibles",
                "location": "B-03",
                "quantity": 8,
                "unit_price": 22.5,
                "status": "Bajo stock",
                "description": "Etiqueta adhesiva para rastreo interno.",
            },
            {
                "name": "Lector móvil",
                "sku": "ECO-1003",
                "category": "Escáner",
                "location": "C-02",
                "quantity": 0,
                "unit_price": 9800,
                "status": "Agotado",
                "description": "Dispositivo tipo handheld para validación en piso.",
            },
            {
                "name": "Caja plástica 60x40",
                "sku": "ECO-1004",
                "category": "Contenedores",
                "location": "D-09",
                "quantity": 36,
                "unit_price": 215,
                "status": "Disponible",
                "description": "Caja retornable para surtido.",
            },
        ]

        for item in demo_products:
            Product.objects.update_or_create(sku=item["sku"], defaults=item)

        self.stdout.write(self.style.SUCCESS("Datos demo cargados correctamente."))
