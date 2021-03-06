"""Module AccessManager with AccessManager Class """

from secure_all.data.access_key import AccessKey
from secure_all.data.access_request import AccessRequest
from secure_all.exception.access_management_exception import AccessManagementException


class AccessManager:
    """AccessManager class, manages the access to a building implementing singleton """
    #pylint: disable=too-many-arguments,no-self-use,invalid-name, too-few-public-methods
    class __AccessManager:
        """Class for providing the methods for managing the access to a building"""

        @staticmethod
        def request_access_code( id_card, name_surname, access_type, email_address, days ):
            """ this method give access to the building"""
            my_request = AccessRequest(id_card, name_surname, access_type, email_address, days)
            my_request.store_request()
            return my_request.access_code

        @staticmethod
        def get_access_key( keyfile ):
            """Returns the access key for the access code & dni received in a json file"""
            my_key = AccessKey.create_key_from_file(keyfile)
            my_key.store_keys()
            return my_key.key

        @staticmethod
        def open_door( key ):
            """Opens the door if the key is valid an it is not expired"""
            if AccessKey.create_key_from_id(key).is_valid() and AccessKey.create_key_from_id(key).is_revoked is False:
                AccessKey.store_open_door(key)
                return True
            raise AccessManagementException("key is revoked")

        @staticmethod
        def revoked_key(file):
            """Guarda la llave y devuelve los emails de la clave revocada"""
            my_key = AccessKey.revoke_key(file)
            if AccessKey.create_key_from_id(my_key).is_valid() and AccessKey.create_key_from_id(my_key).is_revoked is False:
                AccessKey.create_key_from_id(my_key).is_revoked = True
                return AccessKey.create_key_from_id(my_key).notification_emails

    __instance = None

    def __new__( cls ):
        if not AccessManager.__instance:
            AccessManager.__instance = AccessManager.__AccessManager()
        return AccessManager.__instance
