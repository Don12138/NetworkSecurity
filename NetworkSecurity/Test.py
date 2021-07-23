import signatureOfRSA
import people
import Vigenere

if __name__ == '__main__':
    Alice = people.People('Alice')
    Bob = people.People('Bob')

    Attacker = people.People('Attacker')

    with open('Alice_Storage/Alice-File.txt', 'rb') as f:
        data_alice = f.read()

    vigenere_alice = Vigenere.vigenere(data_alice, Alice.getVigenere())
    message_alice = vigenere_alice.encrypt()
    print("Alice want to send the message:      "+str(data_alice,'utf-8'))
    print("Alice has sent the message:      "+str(message_alice,'utf-8'))

    vigenere_bob = Vigenere.vigenere(message_alice, Bob.getVigenere())
    vigenere_attacker = Vigenere.vigenere(message_alice, Attacker.getVigenere())
    data_bob = vigenere_bob.decrypt()

    print("Bob has received the message:      "+data_bob)
    print("Attacker has received the message:      "+vigenere_attacker.decrypt())

    signature_alice = signatureOfRSA.SignatureOfRSA(Alice, data_alice)
    signature_alice_message = signature_alice.ensignature()
    print("Alice generated the signature:     "+str(signature_alice_message,'utf-8'))

    signature_bob = signatureOfRSA.SignatureOfRSA(Bob, bytes(data_bob,encoding = "utf8"))
    print("Bob verify the signature:     "+str(signature_bob.verifySignture(Alice.getPublic(),signature_alice_message)))


