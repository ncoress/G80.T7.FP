import unittest
from secure_all.access_manager import AccessManager
from secure_all import JSON_FILES_PATH
from secure_all.storage.revokeKeys_json_store import RevokeKeysStore
from secure_all.exception.access_management_exception import AccessManagementException

class TestRevokeKeys(unittest.TestCase):
    rev_store = RevokeKeysStore()
    rev_store.empty_store()

    def test_rev_ok(self):
        my_case = JSON_FILES_PATH + "rev_ok.json"
        acc_manager = AccessManager()
        lista_mails = ["mail1@uc3m.es", "mail2@uc3m.es"]
        self.assertEqual(lista_mails, acc_manager.revoked_key(my_case))

    def test_rev_badjson(self):
        my_cas = JSON_FILES_PATH + "revoke_bad_json.json"
        acc_manager = AccessManager()
        with self.assertRaises(AccessManagementException) as c_m:
            acc_manager.revoked_key(my_cas)
        self.assertEqual(c_m.exception.message, "JSON Decode Error - Wrong JSON Format")

if __name__ == '__main__':
    unittest.main()
