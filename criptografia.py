class Criptografia2:
    # criptografia.py
    # -*- coding: iso-8859-1 -*-
    #
    # Exemplo de um algoritmo de criptografia com chave
    # usando o algoritmo criptográfico de Cesar
    #
    # /!\ Este algorítmo é extremamente fraco e serve
    # apenas para demonstração

    maintable = [
    " 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/áéíóúÁÉÍÓÚàÀãõÃÕüÜ",
    "mübõaÚfSÀy,NtvKcJ0ouICHB nT2kzóÕD;Lw/3rlZÉRÃ4ãP6éjiÜAGÍYM8OX5àÓWsVqFUxEpÁQ7hgúá1í9.de",
    ".UPeZO/hIxJlzgcáCÀL5õsvE7au1fóÍ,Q8úq9DéãHGXr3jàR ;oyüdíNMÁwiTÜ24tm6nBÕSÓWKÉb0YÃFVAkpÚ",
    "fuNDEbmlJ2RÀãovCUGta8AÓ,áXúFYÕWQwh/ rZ1MeSTOPs3yd.IKÜ5BknÃqóíÉ7Íõc4zgÚ9üVjéxHàÁ;0L6ip",
    "0É;2vtóQwqaIiKzcBVyG9éãCfsHkmüPFngx/8 WÕeíÜÍDÃULu.ZoMhpbú,NAOÚJ5á7r3ÀSlÓ4T6d1RõàÁjEYX",
    "JhYb1OGÁáIKremü78H2Bsgã.õ69P/Qu;AlVWXàzoCf4íDSNZóÜtRkyipÍajÉ ÓqéFMdúLUEn5xTÕ3,0ÃvÚwcÀ",
    "ÜãÃHYaQÁi94rGm8ÀxZcàóy2kÚqvU7FouP3VzLXBlgjúÍáIJApWsKtÓCwfdSéíeM0hnbõü1OÕ,T5 ./N6D;ERÉ",
    "Zõsd8u1V6aGÀÓÚ/9ÁíÃ2áRH5;X4AvCãWwDüióxÉéjcgJKoyú.eIf7YzhTtUSbBO,mP3pqQÜN0ÍàEkrFlnMLÕ ",
    "6;áMua /.ÍcéP2Ysm,ówÁ347í9iJLnpFHK5àeARÜDõúZüÀgQoÓyqkxObÚÉvBlNrXWÕCETIhd8zV10GtSfÃUjã",
    "hÉÍ,P7úN;zQõÁocDUàI6rC qOB0ãítMYa8.3pÃyT/2ükdEKxf5éJZÓÜÀRuiH4sASXFó91áwjLGWvlÚngbVÕem",
    ]

    def normalize_key(self, key):
        key = [ ord(k) % 10 for k in key ]
        return len(key), key

    def crypt(self, text, key, table):
        size, key = self.normalize_key(key)
        text = list(text)

        pos = 0
        for char in text:
            subtable = table[key[pos % size]]
            new_char_position = table[0].find(char)

            if new_char_position < 0:
                new_char = char
            else:
                new_char = subtable[new_char_position]
            text[pos] = new_char

            pos += 1

        return ''.join(text)

    def uncrypt(self, text, key, table):
        size, key = self.normalize_key(key)
        text = list(text)

        pos = 0
        for char in text:
            subtable = table[key[pos % size]]
            new_char_position = subtable.find(char)

            if new_char_position < 0:
                new_char = char
            else:
                new_char = table[0][new_char_position]

            text[pos] = new_char

            pos += 1

        return ''.join(text)

    def generate_maintable():
        import random
        print("maintable = [")
        x = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,.;/áéíóúÁÉÍÓÚàÀãõÃÕüÜ")
        for i in range(10):
            print('    "%s",' % (''.join(x)))
            random.shuffle(x)
        print("]")

    mensagem = "Vamos invadir a região amanhã às 15hs GMT"
    chave = "mitzuplick"
    mensagem_cifrada = crypt(mensagem, chave, maintable)
    print(f"Mensagem original: {mensagem}")
    print(f"Mensagem cifrada: {mensagem_cifrada}")
    print(f"Mensagem de retorno: {uncrypt(mensagem_cifrada, chave, maintable)}")

class Criptografia:
    # Instalação: pip install cryptography pip install pycrypto
    #
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
    plain_text = cipher_suite.decrypt(cipher_text)

    import gpg

    # Encryption to public key specified in rkey.
    a_key = input("Enter the fingerprint or key ID to encrypt to: ")
    filename = input("Enter the filename to encrypt: ")
    with open(filename, "rb") as afile:
        text = afile.read()
    c = gpg.core.Context(armor=True)
    rkey = list(c.keylist(pattern=a_key, secret=False))
    ciphertext, result, sign_result = c.encrypt(text, recipients=rkey,
                                                always_trust=True,
                                                add_encrypt_to=True)
    with open("{0}.asc".format(filename), "wb") as bfile:
        bfile.write(ciphertext)
    # Decryption with corresponding secret key
    # invokes gpg-agent and pinentry.
    with open("{0}.asc".format(filename), "rb") as cfile:
        plaintext, result, verify_result = gpg.Context().decrypt(cfile)
    with open("new-{0}".format(filename), "wb") as dfile:
        dfile.write(plaintext)
    # Matching the data.
    # Also running a diff on filename and the new filename should match.
    if text == plaintext:
        print("Hang on ... did you say *all* of GnuPG?  Yep.")
    else:
        pass
        
    from Crypto.Cipher import AES
    # Encryption
    encryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    cipher_text = encryption_suite.encrypt("A really secret message. Not for prying eyes.")

    # Decryption
    decryption_suite = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    plain_text = decryption_suite.decrypt(cipher_text)