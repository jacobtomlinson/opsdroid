"""A mocked skill."""

from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class TestSkill(Skill):
    """A mocked skill."""

    @match_regex("test")
    def test_method(self, message):
        """A test method skill."""
        pass

    @property
    def bad_property(self):
        """Bad property which raises exceptions."""
        raise Exception
