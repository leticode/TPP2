class Servidor:
    hosts = set()

    def __init__(self, host):
        self.host = host
        if host in Servidor.hosts:
            print("nombre no disponible")
        else:
            print("-----------------------")
            print("Nombre disponible. Host: ", self.host)
            print("-----------------------")
            Servidor.hosts.add(host)
        
host = Servidor("Leticia")
host2 = Servidor("qwertyuioplñkjhgfd")
host3 = Servidor("Leticia")