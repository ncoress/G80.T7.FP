from secure_all.data.attributes.attribute import Attribute


class Revocation(Attribute):
    """Class that includes the validation rules for access_type
    including the logic for validatin the days"""

    REVOCATION_TYPE_TEMPORAL = "Temporal"
    REVOCATION_TYPE_FINAL = "Final"

    def __init__( self,attr_value ):
        self._validation_pattern =  r'(Temporal|Final)'
        self._error_message = "type of revocation invalid"
        self._attr_value = self._validate(attr_value)
