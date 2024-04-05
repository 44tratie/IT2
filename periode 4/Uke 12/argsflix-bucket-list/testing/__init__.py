import traceback

from colorama import Back, Fore, Style

from testing.backend.api import test_api

tests = [test_api]


def run_tests() -> None:
    success_messages = []
    for test in tests:
        print(
            f"{Back.RESET}{Fore.RESET}TESTING: {Back.RESET}{Fore.YELLOW}{test.__name__}{Style.RESET_ALL}"
        )
        try:
            test()
            success_msg = f"TEST: {Back.RESET}{Fore.GREEN}{test.__name__} {Back.GREEN}{Fore.RESET}PASS{Style.RESET_ALL}"
            success_messages.append(success_msg)
            print(success_msg)
        except KeyboardInterrupt:
            print("Exiting tests...")
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
