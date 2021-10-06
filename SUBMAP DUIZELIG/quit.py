woord = "quit"
input_woord = ""
woord_attempt = 0

while input_woord != woord:
    if input("Voer het woord in! : ") == woord:
        print("U heb het woord goed getypt!")
        break

    woord_attempt += 1
    print(f"Poging nmr. {woord_attempt}")
    




