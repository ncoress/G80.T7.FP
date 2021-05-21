"""Test de revoke key"""

import unittest
from secure_all.access_manager import AccessManager
from secure_all import JSON_FILES_PATH, AccessManagementException
from secure_all.storage.revoke_keys_json_store import RevokeKeysStore

class TestRevokeKeys(unittest.TestCase):
    """Clase test de revoke """
    rev_store = RevokeKeysStore()
    rev_store.empty_store()

    def test_rev_ok(self):
        """test válido"""
        my_case = JSON_FILES_PATH + "rev_ok.json"
        acc_manager = AccessManager()
        lista_mails = ["mail1@uc3m.es", "mail2@uc3m.es"]
        self.assertEqual(lista_mails, acc_manager.revoked_key(my_case))

    def test_rev_badjson(self):
        """test no válido error en el json"""
        my_cas = JSON_FILES_PATH + "revoke_bad_json.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_rev_double_key(self):
        """test no válido error en el json dos etiquetas key"""
        my_cas = JSON_FILES_PATH + "revoke_double_key.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_rev_no_revocation(self):
        """test no válido error en el json sin tipo"""
        my_cas = JSON_FILES_PATH + "revoke_NO_revocation.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "type of revocation invalid")

    def test_rev_no_reason(self):
        """test no válido error en el json sin reason"""
        my_cas = JSON_FILES_PATH + "revoke_NO_reason.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

    def test_revoke_long_key(self):
        """test no válido error llave inválida"""
        my_cas = JSON_FILES_PATH + "revoke_long_key.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "key invalid")

    def test_revoke_no_key(self):
        """test no válido error sin llave"""
        my_cas = JSON_FILES_PATH + "revoke_no_key.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "key invalid")

if __name__ == '__main__':
    unittest.main()
