from log_utils.logger import Logger

import os
import polypasswordhasher.shamirsecret as shamirsecret

logging_config_path: str = "src/logging_debug.conf"
logging_config_absolute_path = os.path.abspath(logging_config_path)
print(logging_config_absolute_path)
logger = Logger(logging_config_absolute_path)

logger.info("infotest")

#secret_str: str = "hello test fujifko man akha ajiena nasdufja nasfuj uiqwjiasf asdfjnas asdifjasdf asdfaisfd asdifjasfd asdfiwek asfjiasf asdfawse asfdw"
secret_str: str = "hello test"

# 閾値は3に設定したので3つのシェアがあればシークレットを復元できます
s = shamirsecret.ShamirSecret(3, secret_str.encode('utf-8'))
a=s.compute_share(1)
b=s.compute_share(2)
c=s.compute_share(3)
d=s.compute_share(4)

logger.info(f"a: {a}")
logger.info(f"b: {b}")
logger.info(f"c: {c}")
logger.info(f"d: {d}")

a1 = (1, bytearray(b'\xb4|\xf9\xa0\xc0\xf0\xa7 \xf4\xbc'))
b1 = (2, bytearray(b'RH\xe0Zo]\xdc\xdc\x80e'))
c1 = (3, bytearray(b'\x8eQu\x96\xc0\x8d\x0f\x99\x07\xad'))
d1 = (4, bytearray(b'NC\xad\xe2`\xefk\xc0;\x08'))

byte1 = b'\xb4|\xf9\xa0\xc0\xf0\xa7 \xf4\xbc'

# should be able to recover from any two...
# 閾値は3に設定したので3つのシェアがあればシークレットを復元できます
t = shamirsecret.ShamirSecret(3)
a1_valid_share = t.is_valid_share(a1)
logger.info(f"a1_valid_share: {a1_valid_share}")

t.recover_secretdata([a1,b1,c1])
logger.info(f"recover secretdata: {t.secretdata}")

t = shamirsecret.ShamirSecret(3)
t.recover_secretdata([a1,c1,d1])
logger.info(f"recover secretdata: {t.secretdata}")

shamirsecret.ShamirSecret()
t = shamirsecret.ShamirSecret(3)
t.recover_secretdata([b,c,a1])
logger.info(f"recover secretdata: {t.secretdata}")

# 閾値は3に設定したので3つのシェアがあればシークレットを復元できます
t = shamirsecret.ShamirSecret(4)
t.recover_secretdata([a1,b,c,d])
logger.info(f"recover secretdata: {t.secretdata}")