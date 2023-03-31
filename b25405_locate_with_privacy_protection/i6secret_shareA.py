import threading
import queue
import time

from i3rssi_to_predict import i3main

# Simple Caesar cipher function for encryption and decryption
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == "decrypt":
                shift_amount = -shift_amount
            char_ascii = ord(char) + shift_amount
            if char.islower():
                if char_ascii > ord("z"):
                    char_ascii -= 26
                elif char_ascii < ord("a"):
                    char_ascii += 26
            else:
                if char_ascii > ord("Z"):
                    char_ascii -= 26
                elif char_ascii < ord("A"):
                    char_ascii += 26
            result += chr(char_ascii)
        else:
            result += char
    return result

class EncryptThread(threading.Thread):
    def __init__(self, msg_queue, num_decrypt_threads):
        threading.Thread.__init__(self)
        self.msg_queue = msg_queue
        self.num_decrypt_threads = num_decrypt_threads

    def run(self):
        message = "Hello, this is a secret message!"
        encrypted_message = caesar_cipher(message, 3, "encrypt")
        print(f"Encrypted Message: {encrypted_message}")
        for _ in range(self.num_decrypt_threads):
            self.msg_queue.put(encrypted_message)


class DecryptThread(threading.Thread):
    def __init__(self, msg_queue):
        threading.Thread.__init__(self)
        self.msg_queue = msg_queue

    def run(self):
        while not self.msg_queue.empty():
            encrypted_message = self.msg_queue.get()
            decrypted_message = caesar_cipher(encrypted_message, 3, "decrypt")
            print(f"Decrypted Message: {decrypted_message}")
            self.msg_queue.task_done()

# Main program
def main():
    print('用于在线程之间传递加密和解密消息。然后，我们创建一个加密线程和两个解密线程。\
        加密线程将消息加密并将其放入队列中。解密线程将从队列中获取加密消息，对其进行解密，并输出解密后的消息')
    msg_queue = queue.Queue()

    num_decrypt_threads = 2
    encrypt_thread = EncryptThread(msg_queue, num_decrypt_threads)
    decrypt_thread1 = DecryptThread(msg_queue)
    decrypt_thread2 = DecryptThread(msg_queue)

    encrypt_thread.start()
    time.sleep(1)  # Ensure the message is encrypted before starting decryption threads
    decrypt_thread1.start()
    decrypt_thread2.start()

    encrypt_thread.join()
    decrypt_thread1.join()
    decrypt_thread2.join()

    print("All threads 协商通过，可以使用隐私功能")
    i3main()

if __name__ == "__main__":
    main()