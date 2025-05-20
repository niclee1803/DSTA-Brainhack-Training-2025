# Cryptography Notes
## Ancient cryptography algorithms
* Scytale: key is diameter of rod
* Caesar: shift
* Vignere: keyword + shift

## Entropy
average no of bits used to represent no of possible cases of the system

## Confusion
Cryptographic operation that makes the relationship between key and ciphertext unknown
e.g. substitution operation

## Diffusion
disperses a bit of plaintext to various cyphertext bits to hide the statistical properties of plaintext
e.g. permutation operation, switches location of letters in the string

Must use both for strong encryption algorithm



## Public Key Cryptography
earlier, use same secret key for encryption and decryption (symmetric key cryptography), need a lot more keys if more people join the communication
public key cryptography generates a pair of private key and public key (public key for encryption, private key for decryption)
user keeps private key safely
if new user wants to have crypto communication, only need to send public key to sender


## Kerkhoff's Principle
A crypto system should be secure, even if everything about the system, except the key is public knowledge
The algorithm can be known, but key cannot be known
security must not depend on secrecy of algorithm, but the key

## Digital Signature
information is included in a certain electronic document or logically combined to an electronic form. used to verify the signer and ensure signer signed on certain electronic document
helps find out whetehr document has been tampered with
opposite way as public key cryptography
uses private key to generate signature and public key to verify ciphertext
anyone can use the public key to verify ciphertext that was encrypted with private key and ciphertext act as digital signature


## Cryptographic Hash Function
hash function: any function that can be used to map the data of arbitrary size to fixed-size value
Cryptographic Hash Function: a small change to the message should change hash value so extensively that a new hash value appears uncorrelated with the old hash value
must have these 3 properties:
* preimage resistance: computationally infeasible to find an input that maps to that element when a hash value is given
* secondary preimage resistance: computationally infeasible to find any second input that has the same output as given value
* collision resistance: computationally infeasible to find the different input values for the same hash value

## Information Security Services of Cryptography
* Confidentiality: only the people or processes authorised to view and use contents of a message have access to the contents
* Integrity: ensures a message or transaction has not been tampered with
* Authentication: process of confirming identification by checking provided credentials against those stored
* Non-repudiation: provides evidence for the existence of a message and ensure its contents cannot be disputed once sent