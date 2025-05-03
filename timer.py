import time


user_input = input("Enter number of seconds to wait: ")


seconds = int(user_input)

print(f"Waiting for {seconds} seconds...")
time.sleep(seconds)
print("Done!")
