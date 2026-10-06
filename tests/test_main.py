from contextlib import redirect_stdout
from io import StringIO
import unittest

from helloworld import main


class MainTests(unittest.TestCase):
    def test_main_prints_hello_word(self) -> None:
        output = StringIO()

        with redirect_stdout(output):
            main()

        self.assertEqual("helloWord\n", output.getvalue())


if __name__ == "__main__":
    unittest.main()
