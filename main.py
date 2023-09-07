import os
import win32.com.client as wincom

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. created by Miss Sayali")
    while True:
        x =input("Enter what you want me to speak:")
        if x=="q":
            os.system("say 'bye bye system'")
            break
        command = f"say {x}"
        os.system(command)

