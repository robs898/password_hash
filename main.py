from argon2 import PasswordHasher

ph = PasswordHasher()
hash = ph.hash('password123')

if ph.verify(hash, 'password123'):
    print('it worked')
