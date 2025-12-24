import hashlib

EXPECTED_HASH = "e0c6830bae960a200289e1109ab2fae46b72ce2bb985dc965eb8907721ccf734"

PASTEBIN_URL = "https://pastebin.com/wRwnHEwj"
PASTEBIN_PASSWORD = "CheckInD@rkWeb"

def verify_flag(user_input):
    return hashlib.sha256(user_input.encode()).hexdigest() == EXPECTED_HASH

def main():
    print("Freelance Loop - Internal Verification Tool")
    print("===========================\n")

    user_flag = input("Enter verification flag: ").strip()

    if verify_flag(user_flag):
        print("\n[+] Verification successful.")
        print("Pastebin URL:")
        print(PASTEBIN_URL)
        print("\nPastebin Password:")
        print(PASTEBIN_PASSWORD)
    else:
        print("\n[-] Invalid flag.")

if __name__ == "__main__":
    main()
