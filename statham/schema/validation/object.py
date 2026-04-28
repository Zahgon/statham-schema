from typing import Any

from statham.schema.exceptions import ValidationError
from statham.schema.validation.base import Validator


class Required(Validator):
    """Validate that object values contain all required properties."""

    types = (dict,)
    keywords = ("required",)
    message = "Must contain all required fields: {required}"

    @classmethod
    def from_element(cls, element):
        required = getattr(element, "required", None) or []
        properties = getattr(element, "properties", None)
        if properties:
            required += properties.required
        if not required:
            return None
        return Required(required)

    def _validate(self, value: Any):
        pass


class AdditionalProperties(Validator):
    """Validate that prohibited properties are not included."""

    types = (dict,)
    keywords = ("__properties__",)
    message = "Must not contain unspecified properties. Accepts: {properties}"

    def error_message(self):
        pass

    def _validate(self, value: Any):
        pass


class MinProperties(Validator):
    """Validate that object values contain a minimum number of properties."""

    types = (dict,)
    keywords = ("minProperties",)
    message = "Must contain at least {minProperties} properties."

    def _validate(self, value: Any):
        pass


class MaxProperties(Validator):
    """Validate that object values contain a maximum number of properties."""

    types = (dict,)
    keywords = ("maxProperties",)
    message = "Must contain at most {maxProperties} properties."

    def _validate(self, value: Any):
        pass


class PropertyNames(Validator):
    """Validate that property names conform to a schema."""

    types = (dict,)
    keywords = ("propertyNames",)
    message = "Property names must match schema {propertyNames}"

    def _validate(self, value: Any):
        pass


class Dependencies(Validator):
    types = (dict,)
    keywords = ("dependencies",)
    message = "Must match defined dependencies: {dependencies}."

    def _validate(self, value: Any):
        pass

    @staticmethod
    def validate_schema_dependency(dependency, value):
        pass
