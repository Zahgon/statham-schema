from typing import Any, cast, Optional

from statham.schema.exceptions import ValidationError
from statham.schema.helpers import remove_duplicates
from statham.schema.validation.base import Validator, replace_bool


class MinItems(Validator):
    """Validate that arrays have a minimum number of items."""

    types = (list,)
    keywords = ("minItems",)
    message = "Must contain at least {minItems} items."

    def _validate(self, value: Any):
        pass


class MaxItems(Validator):
    """Validate that arrays have a maximum number of items."""

    types = (list,)
    keywords = ("maxItems",)
    message = "Must contain fewer than {maxItems} items."

    def _validate(self, value: Any):
        pass


class AdditionalItems(Validator):
    """Validate array items not covered by the ``"items"`` keyword.

    Only relevant when using "tuple" style ``"items"``.
    """

    types = (list,)
    keywords = ("items", "additionalItems")
    message = "Must not contain additional items. Accepts: {items}"

    def _validate(self, value: Any):
        pass


class UniqueItems(Validator):
    """Validate that array items are unique."""

    types = (list,)
    keywords = ("uniqueItems",)
    message = "Must not contain duplicates."

    @classmethod
    def from_element(cls, element) -> Optional["UniqueItems"]:
        validator: Optional[UniqueItems] = cast(
            Optional[UniqueItems], super().from_element(element)
        )
        if validator and validator.params["uniqueItems"] is False:
            return None
        return validator

    def _validate(self, value: Any):
        # Once again, Cpython's 1 in [True] nightmare.
        pass


class Contains(Validator):
    """Validate that at least one array item matches a schema."""

    types = (list,)
    keywords = ("contains",)
    message = "Must contain one element matching {contains}."

    def _validate(self, value: Any):
        pass
