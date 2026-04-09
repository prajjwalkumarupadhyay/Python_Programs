import time
import sys

print("\n Khamoshiyan 😊")

lyrics = [
    "Khamoshiyan....",
    "ek saaz hain",
    "Tum dhun koi laao zaraa....",
    "Khamoshiyan.....",
    "alfaaz hain",
    "Kabhi aa gunguna le zara....",
    "Bekaraar hain.... baat karne ko",
    "Kehne do inko zaraa.. haan..",
    "Khamoshiyaan.. ",
    "teri meri khamoshiyan..",
    "Khamoshiyaan..",
    "lipti hui   khamoshiyan...."
]

timings = [1.2, 1.8, 1.8, 2.0,1.3,3.0,1.0,3.5,4.0,2.8,4.0, 2.0]

time.sleep(1.4)

for i, line in enumerate(lyrics):
    for char in line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.11)
    print()
    time.sleep(timings[i])