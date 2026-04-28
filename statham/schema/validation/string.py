import re
from typing import Any

from statham.schema.exceptions import ValidationError
from statham.schema.validation.base import Validator
from statham.schema.validation.format import format_checker


class Pattern(Validator):
    """Validate that string values match a regular expression."""

    types = (str,)
    keywords = ("pattern",)
    message = "Must match regex pattern {pattern}."

    def error_message(self):
        pass

    def _validate(self, value: Any):
        pass


class MinLength(Validator):
    """Validate that string values are over a minimum length."""

    types = (str,)
    keywords = ("minLength",)
    message = "Must be at least {minLength} characters long."

    def _validate(self, value: Any):
        pass


class MaxLength(Validator):
    """Validate that string values are under a maximum length."""

    types = (str,)
    keywords = ("maxLength",)
    message = "Must be at most {maxLength} characters long."

    def _validate(self, value: Any):
        pass


class Format(Validator):
    """Validate that string values match a named format.

    Additional formats may be registered via
    :func:`~statham.schema.validation.format.format_checker`.
    """

    types = (str,)
    keywords = ("format",)
    message = "Must match format described by '{format}'."

    def _validate(self, value: Any):
        pass
