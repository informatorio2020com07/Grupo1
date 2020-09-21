from django.core.management import BaseCommand
from Anuncio.models import Localidad, Transporte

from csv import DictReader


class Command(BaseCommand):

    def __cargar_bd(self):
        for fila in DictReader(open("static/csv/localidades.csv")):
            locali = Localidad()
            locali.localidad = fila["Nombre"]
            locali.save()
        for fila in DictReader(open("static/csv/transporte.csv")):
            transp = Transporte()
            transp.transporte = fila["Tipo"]
            transp.save()

    def handle(self, *args, **options):
        self.__cargar_bd()
