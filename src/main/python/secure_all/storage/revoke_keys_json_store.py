"""Implements the RequestsJSON Store"""
from secure_all.storage.json_store import JsonStore
from secure_all.cfg.access_manager_config import JSON_FILES_PATH


class RevokeKeysStore():
    """Extends JsonStore """
    class __RevokeKeysStore(JsonStore):
        #pylint: disable=invalid-name
        ID_FIELD = "Key"
        REVOCATION_STORE = "Revocation"
        REASON_STORE = "Reason"

        _FILE_PATH = JSON_FILES_PATH + "storeRevokeKeys.json"
        _ID_FIELD = ID_FIELD

    __instance = None

    def __new__( cls ):
        if not RevokeKeysStore.__instance:
            RevokeKeysStore.__instance = RevokeKeysStore.__RevokeKeysStore()
        return RevokeKeysStore.__instance

    def __getattr__ ( self, nombre ):
        return getattr(self.__instance, nombre)

    def __setattr__ ( self, nombre, valor ):
        return setattr(self.__instance, nombre, valor)
