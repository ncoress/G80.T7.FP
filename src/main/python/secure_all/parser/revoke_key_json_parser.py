from secure_all.parser.json_parser import JsonParser

class RevokeKeyJsonParser(JsonParser):
    """parser for input key files containing a AccessKey request"""
    #pylint: disable=too-few-public-methods
    ACCESS_KEY = "Key"
    REVOCATION = "Revocation"
    REASON = "Reason"
    _key_list =  [ ACCESS_KEY, REVOCATION, REASON ]
