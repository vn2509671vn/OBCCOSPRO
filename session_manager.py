import time
from threading import Timer

class SessionManager:
    def __init__(self, timeout=21600):
        # Timeout mặc định là 21600 giây (6 tiếng)
        self.sessions = {}
        self.timeout = timeout

    def add_session(self, username, session):
        # Thêm session mới và thiết lập thời gian hết hạn
        self.sessions[username] = {
            'session': session,
            'last_active': time.time()
        }
        # Tạo một Timer để xóa session khi hết hạn
        self.start_session_timeout(username)

    def get_session(self, username):
        if username in self.sessions:
            session_data = self.sessions[username]
            # Cập nhật thời gian hoạt động cuối cùng
            session_data['last_active'] = time.time()
            return session_data['session']
        return None

    def start_session_timeout(self, username):
        def remove_session():
            self.sessions.pop(username, None)

        # Thiết lập Timer để tự động xóa session sau khi hết timeout
        timer = Timer(self.timeout, remove_session)
        timer.start()
