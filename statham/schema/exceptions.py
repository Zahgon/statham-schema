from typing import Dict

from statham.schema.constants import JSONElement


class StathamError(Exception):
    """Base exception for errors relating to :mod:`statham`."""


class SchemaDefinitionError(StathamError):
    """Raised when invalid schemas are declared in model definitions."""

    @classmethod
    def reserved_attribute(cls, attribute_name: str) -> "SchemaDefinitionError":
        pass


class ValidationError(StathamError):
    """Raised when JSON Schema validation fails for input data."""

    @classmethod
    def from_validator(cls, property_, value, message) -> "ValidationError":
        pass

    @classmethod
    def combine(
        cls, property_, value, exceptions, message
    ) -> "ValidationError":
        pass

    @classmethod
    def multiple_composition_match(cls, matching_models, data):
        pass


class SchemaParseError(StathamError):
    """Raised when parsing JSON Schema documents to statham models."""

    @classmethod
    def missing_title(
        cls, schema: Dict[str, JSONElement]
    ) -> "SchemaParseError":
        return cls(
            "No title defined in schema. Use "
            "`statham.titles.title_labeller` to pre-process the "
            f"schema: {schema}"
        )

    @classmethod
    def unresolvable_declaration(cls) -> "SchemaParseError":
        return cls(
            "Schema document has an unresolvable declaration tree. This "
            "generally occurs due to cyclical references."
        )

    @classmethod
    def invalid_type(cls, value):
        return cls(f"Got invalid type keyword: {value}.")


# pylint: disable=line-too-long
class FeatureNotImplementedError(SchemaParseError):
    """Raised when parsing valid JSON Schema features currently unsupported by ``statham``."""

    @classmethod
    def unsupported_keywords(cls, keywords) -> "FeatureNotImplementedError":
        return cls(
            f"The following provided keywords are not supported: {keywords}"
        )
