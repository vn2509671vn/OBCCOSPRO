import pyodbc

class Connection:
    def __init__(self, server_ip, database, username, password, driver="{SQL Server}", timeout=300):
        self.server = server_ip
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver
        self.timeout = timeout
        self.conn = None

    def get_db_connection(self):
        """Thiết lập kết nối đến cơ sở dữ liệu MSSQL."""
        if self.conn is None:
            try:
                self.conn = pyodbc.connect(
                    f"DRIVER={self.driver};"
                    f"SERVER={self.server};"
                    f"DATABASE={self.database};"
                    f"UID={self.username};"
                    f"PWD={self.password};"
                    f"Connection Timeout={self.timeout};"
                )
                print("Kết nối CSDL thành công.")
            except pyodbc.Error as e:
                print(f"Lỗi kết nối CSDL: {e}")
                self.conn = None
        return self.conn

    def close_connection(self):
        """Đóng kết nối với cơ sở dữ liệu."""
        if self.conn is not None:
            self.conn.close()
            print("Đã đóng kết nối CSDL.")
            self.conn = None

    def execute_query(self, query, params=None):
        """Thực thi một truy vấn SQL với các tham số (nếu có)."""
        conn = self.get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                conn.commit()
                print("Thực thi truy vấn thành công.")
                return cursor
            except pyodbc.Error as e:
                print(f"Lỗi khi thực thi truy vấn: {e}")
        return None
