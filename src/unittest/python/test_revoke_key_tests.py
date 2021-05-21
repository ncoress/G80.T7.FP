import unittest
from secure_all.access_manager import AccessManager
from secure_all import JSON_FILES_PATH, AccessManagementException
from secure_all.storage.revokeKeys_json_store import RevokeKeysStore
from secure_all.exception.access_management_exception import AccessManagementException

class TestRevokeKeys(unittest.TestCase):
    """Clase test de revoke """
    rev_store = RevokeKeysStore()
    rev_store.empty_store()
    """test válido"""
    def test_rev_ok(self):
        my_case = JSON_FILES_PATH + "rev_ok.json"
        acc_manager = AccessManager()
        lista_mails = ["mail1@uc3m.es", "mail2@uc3m.es"]
        self.assertEqual(lista_mails, acc_manager.revoked_key(my_case))

    """test no válido error en el json"""
    def test_rev_badjson(self):
        my_cas = JSON_FILES_PATH + "revoke_bad_json.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")
    """test no válido error en el json dos etiquetas key"""

    def test_rev_double_key(self):
        my_cas = JSON_FILES_PATH + "revoke_double_key.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")
    """test no válido error en el json sin tipo"""
    def test_rev_no_revocation(self):
        my_cas = JSON_FILES_PATH + "revoke_NO_revocation.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "type of revocation invalid")
    """test no válido error en el json sin reason"""
    def test_rev_no_reason(self):
        my_cas = JSON_FILES_PATH + "revoke_NO_reason.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")
    """test no válido error llave inválida"""
    def test_revoke_long_key(self):
        my_cas = JSON_FILES_PATH + "revoke_long_key.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "key invalid")
    """test no válido error sin llave"""
    def test_revoke_no_key(self):
        my_cas = JSON_FILES_PATH + "revoke_no_key.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "key invalid")

if __name__ == '__main__':
    unittest.main()
