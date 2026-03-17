from abc import ABC, abstractmethod


class NetworkDevice(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_status(self):
        pass


class Server(NetworkDevice):
    def __init__(self, name, ip):
        self.name   = name
        self.ip     = ip
        self.status = 'active'
        self.cpu    = 0

    def get_info(self):
        return f'{self.name} - {self.ip} ({self.cpu}%)'

    def get_type(self):   return 'Server'
    def get_status(self): return self.status


class Router(NetworkDevice):
    def __init__(self, name, ip):
        self.name   = name
        self.ip     = ip
        self.status = 'active'

    def get_info(self):
        return f'{self.name} - {self.ip}'

    def get_type(self):   return 'Router'
    def get_status(self): return self.status


class Switch(NetworkDevice):
    def __init__(self, name, ip):
        self.name   = name
        self.ip     = ip
        self.status = 'active'

    def get_info(self):
        return f'{self.name} - {self.ip}'

    def get_type(self):   return 'Switch'
    def get_status(self): return self.status


class DeviceFactory:
    @staticmethod
    def create_device(device_type, name, ip):
        if device_type.lower() == 'server':
            return Server(name, ip)
        elif device_type.lower() == 'router':
            return Router(name, ip)
        elif device_type.lower() == 'switch':
            return Switch(name, ip)
        else:
            raise ValueError(f'bad type: {device_type}')


class NetworkMonitor:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(NetworkMonitor, cls).__new__(cls)
            cls._instance.devices = []
            cls._instance.alerts  = []
        return cls._instance

    def add_device(self, device):
        self.devices.append(device)
        print(f'device added: {device.get_info()}')

    def add_alert(self, device_name, message):
        alert = f'{device_name}: {message}'
        self.alerts.append(alert)
        print(f'alert: {alert}')

    def display_summary(self):
        print('\n--- monitor ---')
        print(f'devices: {len(self.devices)}')
        print(f'alerts: {len(self.alerts)}')
        for d in self.devices:
            print(f'{d.get_type()}: {d.get_info()}')
        for a in self.alerts:
            print(f'alert info: {a}')


class LogManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LogManager, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def add_entry(self, message):
        self.logs.append(message)
        print(f'log: {message}')


if __name__ == '__main__':
    print('system start')

    d1 = DeviceFactory.create_device('server', 'srv1', '10.0.0.1')
    d2 = DeviceFactory.create_device('router', 'rt1',  '10.0.0.2')
    d3 = DeviceFactory.create_device('switch', 'sw1',  '10.0.0.3')
    d4 = DeviceFactory.create_device('server', 'srv2', '10.0.0.4')

    mon = NetworkMonitor()

    mon.add_device(d1)
    mon.add_device(d2)
    mon.add_device(d3)
    mon.add_device(d4)

    mon.add_alert('rt1', 'high load')
    mon.add_alert('srv2', 'down')

    logger = LogManager()
    logger.add_entry('running')
    logger.add_entry('admin in')

    mon.display_summary()

    print(f'same mon: {mon is NetworkMonitor()}')
    print(f'same log: {logger is LogManager()}')
