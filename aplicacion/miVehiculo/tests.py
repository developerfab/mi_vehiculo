from django.test import TestCase
from datetime import datetime
from miVehiculo.models import *
from utils import *

# Create your tests here.
class UserTest(TestCase):
    """
    Test para el objeto usuario
    """
    def setUp(self):
        """
        se crea el usuario previo a la ejecucion de pruebas
        """
        usuario = Usuario.objects.create_user("ozkar","qwerty@qwerty.com","pass", documento=12345, fecha_licencia=datetime.strptime("15/08/2014", "%d/%m/%Y"), tipo_licencia="A2")

    def register(self):
        """
        Test para el registro de usuarios
        params: nombre de usuario, correo, password, documento, fecha de expedicion de la licencia.
        """
        user = Usuario.objects.create_user("fab","asdf@asdf.com","pass", documento=1023921320, fecha_licencia=datetime.strptime("04/04/2015", "%d/%m/%Y"), tipo_licencia="B1")
        user.save()
        user_test = Usuario.objects.get(username="fab")
        #se hace fallar la prueba
        #self.assertEqual(user_test.email, "asdf@asdf1.com")
        #se hace pasar la prueba
        self.assertEqual(user_test.email, "asdf@asdf.com")

    def renovacion_licencia(self):
        """
        Test para la solicitud de fecha de expedicion de la licencia
        params: registro de usuario
        """
        user = Usuario.objects.create_user("fab","asdf@asdf.com","pass", documento=1023921320, fecha_licencia=datetime.strptime("04/05/2015", "%d/%m/%Y"), tipo_licencia="A1")
        user.save()
        user_test = Usuario.objects.get(username="fab")
        self.assertEqual(str(user_test.fecha_licencia), "2015-05-04")

    def login(self):
        """
        Login del usuario
        """
        self.client.login(username="ozkar", password="pass")
        sesion = self.client.session['_auth_user_id']
        self.assertEqual(int(sesion), 1)

    def calculo_licencia(self):
        """
        Test para el modulo del calculo de vencimiento de la fecha del pase
        """
        usuario = Usuario.objects.get(username="ozkar")
        fecha = fechaLicencia(usuario.fecha_licencia, usuario.tipo_licencia)
        self.assertEqual(fecha, "2015-08-15")
        

class VehiculoTest(TestCase):
    """
    Test para el objeto de vehiculo
    """
    def register(self):
        """
        Test para el registro de vehiculos.
        params : usuario, tipo de vehiculo, placa
        """
        user = Usuario.objects.create_user("fab","asdf@asdf.com","pass", documento=1023921320, fecha_licencia=datetime.strptime("04/04/2015", "%d/%m/%Y"))
        user.save()
        #se crea el segundo usuario
        user2 = Usuario.objects.create_user("oscar","qwert@ase.com","pass", documento=12345, fecha_licencia=datetime.strptime("05/04/2012", "%d/%m/%Y"))
        user2.save()
        #se crea el vehiculo relacionado con el primer usuario
        vehiculo = Vehiculo.objects.create(propietario=user, tipo="camioneta", placa="asd 123")
        vehiculo.save()
        #se crea el segundo vehiculo relacionado con el segundo usuario
        vehiculo2 = Vehiculo.objects.create(propietario=user2, tipo="camioneta", placa="asd 122")
        vehiculo2.save()
        #se hace la consulta en la base de datos
        vehiculo_test = Vehiculo.objects.get(placa="asd 122")
        self.assertEqual(vehiculo_test.propietario, user2)

class ImpuestoTest(TestCase):
    def setUp(self):
        """
        se crea el usuario previo a la ejecucion de pruebas
        """
        usuario = Usuario.objects.create_user("ozkar","qwerty@qwerty.com","pass", documento=12345, fecha_licencia=datetime.strptime("15/08/2014", "%d/%m/%Y"), tipo_licencia="A2")

    def registro_fecha_impuesto(self):
        """
        Test para el registro de la fecha de pago de un impuesto sobre un vehiculo
        """
        user = Usuario.objects.create_user("fab","asdf@asdf.com","pass", documento=1023921320, fecha_licencia=datetime.strptime("04/04/2015", "%d/%m/%Y"))
        user.save()
        #se crea el vehiculo
        vehiculo = Vehiculo.objects.create(propietario=user, tipo="camioneta", placa="asd 123")
        vehiculo.save()
        #se crea un impuesto en la BD
        impuestoObj = Impuesto.objects.create(impuesto="SOAT")
        impuestoObj.save()
        #se crea la relacion entre el vehiculo, impuesto y fecha
        fecha = FechaImpuesto.objects.create(vehiculo=vehiculo, impuesto=impuestoObj, fecha=datetime.strptime("11/08/2014", "%d/%m/%Y"))
        fecha.save()
        fecha_test = FechaImpuesto.objects.get(vehiculo=vehiculo)
        self.assertEqual(fecha_test.vehiculo.propietario.username, "fab")

