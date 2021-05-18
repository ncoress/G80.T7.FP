from secure_all.data.attributes.attribute import Attribute


class Reason(Attribute):
    """Class that includes the validation rules for access_type
    including the logic for validatin the days"""

    def __init__( self,attr_value ):
        self._validation_pattern =  r'(.{0,100})'
        self._error_message = "type of reason invalid"
        self._attr_value = self._validate(attr_value)
