from log_utils.logger import Logger

import os
import polypasswordhasher.shamirsecret as shamirsecret

logging_config_path: str = "src/logging_debug.conf"
logging_config_absolute_path = os.path.abspath(logging_config_path)
print(logging_config_absolute_path)
logger = Logger(logging_config_absolute_path)

logger.info("infotest")

secret_str: str = "hello"

s = shamirsecret.ShamirSecret(2, secret_str.encode('utf-8'))
a=s.compute_share(1)
b=s.compute_share(2)
c=s.compute_share(3)


# should be able to recover from any two...
t = shamirsecret.ShamirSecret(2)
t.recover_secretdata([a,b])

t = shamirsecret.ShamirSecret(2)
t.recover_secretdata([a,c])

t = shamirsecret.ShamirSecret(2)
t.recover_secretdata([b,c])

# ... or even all three!
t = shamirsecret.ShamirSecret(2)
t.recover_secretdata([a,b,c])

print(f"secretdata: {t.secretdata}")