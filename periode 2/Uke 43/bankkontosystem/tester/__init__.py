import traceback

from colorama import Back, Fore, Style

from tester.test_bankkonto import test_bankkonto
from tester.test_bsu import test_bsu
from tester.test_kredittkonto import test_kredittkonto
from tester.test_sparekonto import test_sparekonto

tester = test_sparekonto, test_bankkonto, test_bsu, test_kredittkonto


def kjør_tester() -> None:
    success_messages = []
    for test in tester:
        print(
            f"{Back.RESET}{Fore.RESET}TESTER: {Back.RESET}{Fore.YELLOW}{test.__name__}{Style.RESET_ALL}"
        )
        try:
            test()
            success_msg = f"TEST: {Back.RESET}{Fore.GREEN}{test.__name__} {Back.GREEN}{Fore.RESET}PASS{Style.RESET_ALL}"
            success_messages.append(success_msg)
            print(success_msg)
        except KeyboardInterrupt:
            print("Avslutter tester...")
            exit()
        except Exception:
            traceback.print_exc()
            success_msg = f"TEST: {Back.RESET}{Fore.RED}{test.__name__} {Back.RED}{Fore.RESET}FAIL{Style.RESET_ALL}"
            success_messages.append(success_msg)
            print(success_msg)
        print(f"-----------------------")

    print("Test results:")
    for msg in success_messages:
        print(msg)
