import sys
from io import StringIO
import traceback as tb

failed_tests = 0
passed_tests = 0

class TestCase:

    def __init__(self, name=None, desc=None):
        self._stdout = None
        self._string_io = None
        self.name = name
        self.desc = desc
        self.passed = True
        self.error_msg = None

    def __enter__(self):

        global passed_tests, failed_tests

        if self.name is not None:
            name = self.name
        else:
            name = f"Test {passed_tests + failed_tests + 1}"

        print(f"{name} : ", end="")

        self._stdout = sys.stdout
        sys.stdout = self._string_io = StringIO()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        global passed_tests, failed_tests
        sys.stdout = self._stdout

        if self.passed and not exc_type:
            passed_tests += 1
            print("\u001b[32mOK\u001b[0m")
            return True
    
        failed_tests += 1
        print("\u001b[1;31mERREUR\u001b[22;0m")

        print("\u001b[38;5;8m" + "-"*40 + "\u001b[0m")

        if self.error_msg is not None:
            print(f"\u001b[31m{self.error_msg}\u001b[0m")

        if exc_type:
            print(f"\u001b[31m{exc_type.__name__} : {exc_value}\u001b[0m")

        if self.desc is not None:
            print("\nDescription du test :")
            print(self.desc)
            print("")

        output = self._string_io.getvalue()

        if len(output) > 0:
            print("Affichage lors de l'éxécution du test : ")
            print(output)
            print("")

        if exc_type:
            print("Erreur lors de l'éxécution du test : ")
            print(f"{exc_type.__name__} : {exc_value}")
            tb.print_tb(traceback)

        print("\u001b[38;5;8m" + "-"*40 + "\u001b[0m")
        
        return True

    def fail(self, msg=None):
        self.error_msg = msg
        self.passed = False


def tests_summary():
    print("\n" + "=" * 20 + "[ Résultats ]" + "=" * 20)
    print(f"\nTests réussis : \u001b[32m{passed_tests}\u001b[0m")
    print(f"Tests échoués : \u001b[31m{failed_tests}\u001b[0m")
    print(f"Total : \u001b[1m{passed_tests} / {failed_tests + passed_tests}\u001b[22m\n")

def print_test_start():
    print("\n" + "=" * 20 + "[ Tests ]" + "=" * 20)
    print("")