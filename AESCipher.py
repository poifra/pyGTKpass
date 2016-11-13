import hmac

import struct

from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

import os
from os.path import exists

import pickle

class FileManagement():
	def __init__(self, password, keysize=32, kdfIterations=1024, saltMarker=b'$'):
		self.SALT_MARKER = saltMarker
		self.ITERATIONS = kdfIterations
		self.keysize = keysize

		if not isinstance(password, bytes):
			raise ValueError("Password must be a bytes instance")

		if not keysize in [16, 24, 32]:
			raise ValueError("Keysize must be either 16, 24 or 32 bits")

		self.bs = AES.block_size
		self.header = self.SALT_MARKER + struct.pack('>H', self.ITERATIONS) + self.SALT_MARKER
		self.salt = os.urandom(self.bs - len(self.header))
		kdf = PBKDF2(password, self.salt, self.keysize, min(self.ITERATIONS, 65535))
		key = kdf[:keysize]
		self.iv = os.urandom(self.bs)
		self.cipher = AES.new(key, AES.MODE_CBC, self.iv)

	def encrypt(self, dataLst, file):
		with open(file, 'wb') as f:
		#	f.write(self.header + self.salt)
		#	f.write(self.iv)
			byteRep = pickle.dumps(dataLst, pickle.HIGHEST_PROTOCOL)
			
			#create padding to reach the next 16 byte multiple
			length = 16 - (len(byteRep) % 16)
			byteRep += bytes([length])*length
			f.write(self.cipher.encrypt(byteRep))

	def decrypt(self, file):
		with open(file, 'rb') as f:
			#retrieve info from header in file
		#	salt = f.read(self.bs)
		#	self.iv = f.read(self.bs)
			byteRep = f.read()
			dataLst = self.cipher.decrypt(byteRep)
			dataLst = dataLst[:-dataLst[-1]]
			dataLst = pickle.loads(dataLst)
			return dataLst