import socket


class Resolver:

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]


resolve = Resolver()  # calls __init__()
print(resolve('google.com'))  # 172.217.163.46
print(resolve.__call__('google.com')) # 172.217.163.46

# Print cache
print(resolve._cache)
