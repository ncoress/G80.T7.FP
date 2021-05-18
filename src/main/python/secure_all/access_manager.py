"""Module AccessManager with AccessManager Class """

from secure_all.data.access_key import AccessKey
from secure_all.data.access_request import AccessRequest


class AccessManager:
    """AccessManager class, manages the access to a building implementing singleton """
    #pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
    class __AccessManager:
        """Class for providing the methods for managing the access to a building"""

        def request_access_code( self, id_card, name_surname, access_type, email_address, days ):
            """ this method give access to the building"""
            my_request = AccessRequest(id_card, name_surname, access_type, email_address, days)
            my_request.store_request()
            return my_request.access_code

        def get_access_key( self, keyfile ):
            """Returns the access key for the access code & dni received in a json file"""
            my_key = AccessKey.create_key_from_file(keyfile)
            my_key.store_keys()
            return my_key.key

        def open_door( self, key ):
            """Opens the door if the key is valid an it is not expired"""
            if AccessKey.create_key_from_id(key).is_valid():
                AccessKey.store_open_door(key)
                return True

        @staticmethod
        def revoked_key(file):
            """Guarda la llave y devuelve los emails de la clave revocada"""
            my_key = AccessKey.revoke_key(file)
            if AccessKey.create_key_from_id(my_key).is_valid():
                return AccessKey.create_key_from_id(my_key).notification_emails

    __instance = None

    def __new__( cls ):
        if not AccessManager.__instance:
            AccessManager.__instance = AccessManager.__AccessManager()
        return AccessManager.__instance
