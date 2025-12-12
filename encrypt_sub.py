from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, base64

# همون KEY_HEX که در CryptoUtils.kt گذاشتی
KEY_HEX = "1f2e3d4c5b6a79880a1b2c3d4e5f60718293a4b5c6d7e8f00112233445566778"

def hex_to_bytes(h):
    return bytes.fromhex(h.strip())

def encrypt(plain: str) -> str:
    key = hex_to_bytes(KEY_HEX)
    aesgcm = AESGCM(key)
    iv = os.urandom(12)
    cipher = aesgcm.encrypt(iv, plain.encode("utf-8"), None)
    data = iv + cipher
    return base64.b64encode(data).decode("ascii")

if __name__ == "__main__":
    # این‌جا متن sub واقعی‌ات را بگذار
    # مثلاً محتوای یک فایل sub.txt را می‌خوانیم:
    with open("sub.txt", "r", encoding="utf-8") as f:
        plain = f.read().strip()

    out = encrypt(plain)
    print("Encrypted Base64:\n")
    print(out)
