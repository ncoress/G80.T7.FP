"""Implements the RequestsJSON Store"""
from secure_all.storage.json_store import JsonStore
from secure_all.cfg.access_manager_config import JSON_FILES_PATH


class OpenDoorStore():
    """Extends JsonStore """
    class __OpenDoorStore(JsonStore):
        #pylint: disable=invalid-name
        ID_FIELD = "Key"
        ACCESS_DATE = "Access_date"

        _FILE_PATH = JSON_FILES_PATH + "storeOpenDoor.json"
        _ID_FIELD = ID_FIELD

    __instance = None

    def __new__( cls ):
        if not OpenDoorStore.__instance:
            OpenDoorStore.__instance = OpenDoorStore.__OpenDoorStore()
        return OpenDoorStore.__instance

    def __getattr__ ( self, nombre ):
        return getattr(self.__instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.__instance, nombre, valor)
