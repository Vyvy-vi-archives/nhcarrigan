def send_heart(color: str = None):
    if color != None:
        crossed = '\u0336'.join(color) + '\u0336'
        print(f"Sending your {crossed}(purple) heart")
    print('💜')

def rand_color():
    print('PURPLE...')
