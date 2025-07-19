from django.core.management.base import BaseCommand
from todos.services import TodoAPIService

class Command(BaseCommand):
    help = 'Sincroniza TODOs desde la API externa de JSONPlaceholder'

    def add_arguments(self, parser):
        parser.add_argument(
            '--force',
            action='store_true',
            help='Fuerza la sincronización incluso si hay datos existentes',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🔄 Iniciando sincronización con la API...')
        )
        
        try:
            synced_count, total_count = TodoAPIService.sync_todos()
            
            if synced_count == 0:
                self.stdout.write(
                    self.style.WARNING(
                        f'✅ No se encontraron nuevos TODOs. Total en base de datos: {total_count}'
                    )
                )
            else:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✅ Sincronización exitosa! {synced_count} nuevos TODOs de {total_count} total.'
                    )
                )
                
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error durante la sincronización: {str(e)}')
            )
