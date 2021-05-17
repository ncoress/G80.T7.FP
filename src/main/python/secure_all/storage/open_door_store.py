from secure_all.storage.json_store import JsonStore
from secure_all.cfg.access_manager_config import JSON_FILES_PATH
from secure_all.exception.access_management_exception import AccessManagementException


class OpenDoorStore():
    """Extends JsonStore """
    class __OpenDoorStore(JsonStore):
        #pylint: disable=invalid-name
        ID_FIELD = "_AccessKey__key"
        ACCESS_DATE = "__AccessKey__accessDate"
        INVALID_ITEM = "Invalid item to be stored as a key"

        _FILE_PATH = JSON_FILES_PATH + "storeOpenDoor.json"
        _ID_FIELD = ID_FIELD

        def add_item( self, item):
            """Implementing the restrictions related to avoid duplicated keys"""
            #pylint: disable=import-outside-toplevel,cyclic-import
            from secure_all.data.access_key import AccessKey
            if not isinstance(item,AccessKey):
                raise AccessManagementException(self.INVALID_ITEM)

            return super().add_item(item)

    __instance = None

    def __new__( cls ):
        if not OpenDoorStore.__instance:
            OpenDoorStore.__instance = OpenDoorStore.__OpenDoorStore()
        return OpenDoorStore.__instance

    def __getattr__ ( self, nombre ):
        return getattr(self.__instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.__instance, nombre, valor)
