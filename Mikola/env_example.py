from  environs import Env
env = Env()
env.read_env()

token = env('Bot_tok')
print(token)