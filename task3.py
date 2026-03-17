from abc import ABC, abstractmethod

class NetworkUser(ABC):
    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def get_permissions(self):
        pass

class GuestUser(NetworkUser):
    def __init__(self, username):
        self.username = username

    def get_role(self):
        return 'Guest'

    def get_permissions(self):
        return []

class OperatorUser(NetworkUser):
    def __init__(self, username):
        self.username = username

    def get_role(self):
        return 'Operator'

    def get_permissions(self):
        return ['monitor_devices', 'view_logs']

class AdminUser(NetworkUser):
    def __init__(self, username):
        self.username = username

    def get_role(self):
        return 'Admin'

    def get_permissions(self):
        return ['monitor_devices', 'manage_devices',
                'access_control', 'view_logs']

class UserFactory:
    @staticmethod
    def create_user(role, username):
        if role.lower() == 'guest':
            return GuestUser(username)
        elif role.lower() == 'operator':
            return OperatorUser(username)
        elif role.lower() == 'admin':
            return AdminUser(username)
        else:
            raise ValueError(f'Unknown Role: {role}')

class SessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Setting up the Session Manager...')
            cls._instance = super(SessionManager, cls).__new__(cls)
            cls._instance.sessions = {}
        return cls._instance

    def login(self, username, role):
        user = UserFactory.create_user(role, username)
        self.sessions[username] = user
        return (f'USER CONNECTED | Name: {username}'
                f' | Type: {user.get_role()}'
                f' | Allowed: {user.get_permissions()}')

    def logout(self, username):
        if username in self.sessions:
            del self.sessions[username]
            return f'USER DISCONNECTED | {username} session ended'
        return 'Request failed: User not found'

    def check_access(self, username, action):
        if username in self.sessions:
            perms = self.sessions[username].get_permissions()
            if action in perms:
                return f'PERMITTED | {username} is allowed to {action}'
            return f'DENIED | {username} lacks permission for {action}'
        return 'Error: Session does not exist'

    def active_sessions(self):
        return list(self.sessions.keys())

if __name__ == '__main__':
    sm1 = SessionManager()
    sm2 = SessionManager()

    print('--- SYSTEM ACCESS CONTROL ---')

    print(sm1.login('operator01', 'operator'))
    print(sm1.login('admin_sys',  'admin'))

    print()
    print(sm1.check_access('operator01', 'monitor_devices'))
    print(sm1.check_access('operator01', 'manage_devices'))
    print(sm1.check_access('admin_sys',  'manage_devices'))
    print(sm1.check_access('admin_sys',  'access_control'))

    print()
    print(f'Current Active Users: {sm1.active_sessions()}')

    print(sm1.logout('operator01'))
    print(f'Current Active Users: {sm1.active_sessions()}')

    print(f'Singleton Integrity: {sm1 is sm2}')
