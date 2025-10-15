from datetime import datetime

class LogManager:
    def __init__(self):
        self.logs = []  

    def loguear(self, data):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {"timestamp": timestamp, "data": data}
        
        self.logs.append(log_entry)
        
        print(f"Log registrado: {log_entry}")

    def mostrarLogs(self):
        print("Mostrar todos los logs:")
        for log in self.logs:
            print(log)

log_manager = LogManager()

log_manager.loguear({"usuario": "Ana", "accion": "login"})
log_manager.loguear({"usuario": "Juan", "accion": "logout"})

log_manager.mostrarLogs()