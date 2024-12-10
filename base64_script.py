import base64 as b4

interface = """
    1 - Encoder
    2 - Decoder
"""
print(interface)
user_input = int(input("--> "))

def decoder(b64):
    decoded = b4.b64decode(b64.encode('utf-8'))
    return decoded.decode()
def encoder(text):
    encoded = b4.b64encode(text.encode('utf-8'))
    return encoded.decode()

if user_input == 1:
    text = str(input("Enter your text: "))
    print(encoder(text))
elif user_input == 2:
    b64 = input("Enter you Base64: ")
    print(decoder(b64))