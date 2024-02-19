import Crypto.Util.number
import hashlib

# Numero de bits
bits = 1024
A = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
B = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

print("A:", A)
print("B:", B)

# Obtener los primos para Alice y Bob
pA = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
pB = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)

print("pA:", pA)
print("pB:", pB)

na = A * B
print("na:", na)

nb = pA * pB
print("nb:", nb)

phiA = (A - 1) * (B - 1)
print("phiA:", phiA)

phiB = (pA - 1) * (pB - 1)
print("phiB:", phiB)

# Por razones de eficiencia usaremos el numero 4 de Fermat, 65537
e = 65537

# Calcular la llave privada de alice y bob
dA = Crypto.Util.number.inverse(e, phiA)
print("dA:", dA)

dB = Crypto.Util.number.inverse(e, phiB)
print("dB:", dB)


msg = "Hello World!"
hash_msg = hashlib.sha256(msg.encode()).hexdigest()
hash_msg_int = int(hash_msg, 16)

c = pow(hash_msg_int, dA, na)

d = pow(c, e, na)

if(hash_msg_int == d):
    print("Que rico")




