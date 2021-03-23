from log_utils.logger import Logger

import os
import polypasswordhasher.shamirsecret as shamirsecret

logging_config_path: str = "src/logging_debug.conf"
logging_config_absolute_path = os.path.abspath(logging_config_path)
print(logging_config_absolute_path)
logger = Logger(logging_config_absolute_path)

logger.info("infotest")

secret_str: str = "hello test fujifko man akha ajiena nasdufja nasfuj uiqwjiasf asdfjnas asdifjasdf asdfaisfd asdifjasfd asdfiwek asfjiasf asdfawse asfdw"

# 閾値は3に設定したので3つのシェアがあればシークレットを復元できます
s = shamirsecret.ShamirSecret(3, secret_str.encode('utf-8'))
a=s.compute_share(1)
b=s.compute_share(2)
c=s.compute_share(3)
d=s.compute_share(4)

print(f"a: {a}; {a[1]}")
print(f"b: {b}")
print(f"c: {c}")
print(f"d: {d}")

a1 = (1, bytearray(b'fL\\\xc6)\xa5\x94\x1f\x86k\xcf\x06J\xf1\xc28\x82\x92l\xf2\x00\xe4}+\xe2l[>\x0f\x98\xf0\xe9\x96\xbf\xabP\xcc\xae$cY\xcbzDBb\xb6\xcf\x1ae\x85e"[4\xf1L"\xc8\x04\xc9\xe8\xfdUw\xd2\xad\x06\x17q\xae\x99!X\xe3\x922\xc6\x04_\xc4\xfc\xab\xaa\xfb1LF\xeew\xa5\x8az\xfbc8\x1f9(\x8a\xf97\x00\x9f?s\x98\xca%\x05\x15\x04\xdc)\x17A\x00\xde\x86x\xd9\xef\x8e\xf8\x06\xddY>\x17\xe0\x8c1/\x00'))

# should be able to recover from any two...
# 閾値は3に設定したので3つのシェアがあればシークレットを復元できます
t = shamirsecret.ShamirSecret(3)
t.recover_secretdata([a1,b,c])

print(f"recover secretdata: {t.secretdata}")
t = shamirsecret.ShamirSecret(3)
t.recover_secretdata([a1,c,d])

print(f"recover secretdata: {t.secretdata}")
t = shamirsecret.ShamirSecret(3)
t.recover_secretdata([b,c,a1])

print(f"recover secretdata: {t.secretdata}")

# 閾値は3に設定したので3つのシェアがあればシークレットを復元できます
t = shamirsecret.ShamirSecret(4)
t.recover_secretdata([a1,b,c,d])

print(f"recover secretdata: {t.secretdata}")