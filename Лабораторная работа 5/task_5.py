from random import sample


def get_random_password(n = 8) -> str:
    dt = 'ABCDEFGHIKLMNOPQRSTVXYZabcdefghiklmnopqrstvxyz0123456789'
    a = sample(dt, n)
    return ''.join(a)


print(get_random_password())
