#P6 HMAC

import hmac
import hashlib
import secrets

# Initial sent message
sent_msg = input("Enter message: ")
key = secrets.token_bytes(100)  # Secret key generation

# Generate HMAC for sent message
s_md_1 = hmac.new(key=key, msg=sent_msg.encode(), digestmod=hashlib.md5)
init_msg_digest = s_md_1.hexdigest()

# Simulate receiving the same message
received = sent_msg
r_md_1 = hmac.new(key=key, msg=received.encode(), digestmod=hashlib.md5)
recv_msg_digest = r_md_1.hexdigest()

# Comparing sent and received message digests
print("----- Before Tampering -----")
print("Is the message received without any tampering?:",
      hmac.compare_digest(init_msg_digest, recv_msg_digest))

# Simulate tampering the message
tampered_msg = sent_msg[1:]  # remove first character (just for testing tamper)
md_2 = hmac.new(key=key, msg=tampered_msg.encode(), digestmod=hashlib.md5)
tampered_msg_digest = md_2.hexdigest()

# Comparing tampered message digest with original
print("----- After Tampering -----")
print("Is the message received without any tampering?:",
      hmac.compare_digest(init_msg_digest, tampered_msg_digest))
