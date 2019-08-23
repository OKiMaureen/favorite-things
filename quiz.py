from cryptography.fernet import Fernet

key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='

# Oh no! The code is going over the edge! What are you going to do?
message = b'gAAAAABdYEILmN350MALKsHH2P60geG1ONPCQlanD7myxghrTUCwTWaG5W6nVtNCSdkHjOQRRIDBlhEn0240NB9c1rHf0eXCBb9thDUfFtDc8wKVSpO_4OP4uNigHutJ5mOguXABTlDt1wX5Iw09bcwNVGFzTW4iPIHl1kvJ5T4xSGOHfiaCwOE='

def main():
    f = Fernet(key)
    print(f.decrypt(message))


if __name__ == "__main__":
    main()
