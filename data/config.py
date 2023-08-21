from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("ip")
PAY_TOKEN = env.str("PAY_TOKEN")

support_ids = [455636426, 172617890]