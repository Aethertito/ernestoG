from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse

class Command(BaseCommand):
    help = 'Prueba todas las URLs de la aplicación para verificar funcionalidades'

    def handle(self, *args, **options):
        client = Client()
        
        # URLs a probar
        urls_to_test = [
            ('todos:index', 'Página principal'),
            ('todos:todos_ids_only', 'Solo IDs'),
            ('todos:todos_ids_titles', 'IDs y Títulos'),
            ('todos:todos_pending_ids_titles', 'Pendientes IDs y Títulos'),
            ('todos:todos_completed_ids_titles', 'Completados IDs y Títulos'),
            ('todos:todos_ids_userids', 'IDs y UserIDs'),
            ('todos:todos_completed_ids_userids', 'Completados IDs y UserIDs'),
            ('todos:todos_pending_ids_userids', 'Pendientes IDs y UserIDs'),
            ('todos:todo_list_full', 'Lista completa'),
            ('todos:todo_create', 'Crear TODO'),
        ]
        
        self.stdout.write(
            self.style.SUCCESS('🔄 Probando todas las URLs...')
        )
        
        all_passed = True
        
        for url_name, description in urls_to_test:
            try:
                url = reverse(url_name)
                response = client.get(url)
                
                if response.status_code == 200:
                    self.stdout.write(
                        self.style.SUCCESS(f'✅ {description}: {url} - OK')
                    )
                else:
                    self.stdout.write(
                        self.style.ERROR(f'❌ {description}: {url} - Error {response.status_code}')
                    )
                    all_passed = False
                    
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f'❌ {description}: Error - {str(e)}')
                )
                all_passed = False
        
        if all_passed:
            self.stdout.write(
                self.style.SUCCESS('\n🎉 ¡Todas las funcionalidades están funcionando correctamente!')
            )
        else:
            self.stdout.write(
                self.style.ERROR('\n⚠️ Algunas funcionalidades tienen problemas.')
            )
