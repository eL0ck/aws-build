from unittest import TestCase
from yoyo.flojo import dickhead
from click.testing import CliRunner


class TestYoyo(TestCase):
    def test_dickhead(self):
        result = CliRunner().invoke(dickhead, ['-n', 'Derrick'])
        self.assertEqual(result.exit_code, 0, msg="CLI app doesn't take name parameter")
        self.assertEqual(result.output, "Hallo Derrick\n", msg="wrong text displayed")
