from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)

# Endpoint nhận request từ client và gửi tiếp tới API login
@app.route('/obccos/login', methods=['POST'])
def login_obccos():
    # Lấy dữ liệu từ request client gửi lên
    client_data = request.json

    # URL của API login
    target_api_url = "https://api-obccos.vnpt.vn/login"

    # Payload (dữ liệu login)
    payload = json.dumps({
        "user_name": client_data.get('user_name'),
        "password": client_data.get('password')
    })

    # Headers
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Referer': 'https://obccos.vnpt.vn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0'
    }

    try:
        # Gửi request tới API login
        response = requests.post(target_api_url, headers=headers, data=payload)
        
        # Trả lại response của API login cho client
        return jsonify(response.json()), response.status_code
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/obccos/getCosName', methods=['GET'])
def getCosName():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy tham số "stb" từ query parameter
    stb = request.args.get('stb')
    
    if not stb:
        return jsonify({"error": "stb parameter is required"}), 400

    # URL API GET dữ liệu, thêm stb vào query
    url = f"https://api-obccos.vnpt.vn/cnhan/getCosName?stb={stb}"
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header của client
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API khác
    response = requests.get(url, headers=headers)
    
    # Trả về kết quả từ API cho client
    return jsonify(response.json()), response.status_code

@app.route('/obccos/getTTCoban', methods=['GET'])
def getTTCoban():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy tham số "stb" từ query parameter
    stb = request.args.get('stb')
    
    if not stb:
        return jsonify({"error": "stb parameter is required"}), 400

    # URL API GET dữ liệu, thêm stb vào query
    url = f"https://api-obccos.vnpt.vn/cnhan/getTTCoban?stb={stb}"
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header của client
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API khác
    response = requests.get(url, headers=headers)
    
    # Trả về kết quả từ API cho client
    return jsonify(response.json()), response.status_code

@app.route('/obccos/getTTTT', methods=['GET'])
def getTTTT():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy tham số "stb" từ query parameter
    stb = request.args.get('stb')
    
    if not stb:
        return jsonify({"error": "stb parameter is required"}), 400

    # URL API GET dữ liệu, thêm stb vào query
    url = f"https://api-obccos.vnpt.vn/cnhan/getTTTT?stb={stb}"
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header của client
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API khác
    response = requests.get(url, headers=headers)
    
    # Trả về kết quả từ API cho client
    return jsonify(response.json()), response.status_code

# Hàm GET để lấy số lượng tin nhắn chưa đọc
@app.route('/obccos/getUnreadMessageCount', methods=['GET'])
def getUnreadMessageCount():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    url = "https://api-obccos.vnpt.vn/message/getUnreadMessageCount"
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    response = requests.get(url, headers=headers)
    
    return jsonify(response.json()), response.status_code

# Hàm GET để tìm kiếm người dùng với "user_code"
@app.route('/obccos/searchUserCode', methods=['GET'])
def searchUser():
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    user_code = request.args.get('user_code')
    
    if not user_code:
        return jsonify({"error": "user_code parameter is required"}), 400

    url = f"https://api-obccos.vnpt.vn/search-user?user_code={user_code}"
    
    headers = {
        'sec-ch-ua-platform': '"Windows"',
        'Authorization': token,  # Dùng token từ header
        'Referer': 'https://obccos.vnpt.vn/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'Content-Type': 'application/json',
        'sec-ch-ua-mobile': '?0'
    }

    response = requests.get(url, headers=headers)
    
    return jsonify(response.json()), response.status_code

# Hàm GET để tìm kiếm người dùng với "user_code"
@app.route('/obccos/searchUserName', methods=['GET'])
def search_user():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy tham số "user_name" từ query parameter
    user_name = request.args.get('user_name')
    
    if not user_name:
        return jsonify({"error": "user_name parameter is required"}), 400

    # URL API GET dữ liệu
    url = f"https://api-obccos.vnpt.vn/search-user?user_name={user_name}"
    
    # Headers cho request
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    try:
        # Gửi GET request đến API khác
        response = requests.get(url, headers=headers)
        # Trả về kết quả từ API cho client
        return jsonify(response.json()), response.status_code

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/obccos/getList24H', methods=['GET'])
def getList24H():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # URL API GET dữ liệu
    url = "https://api-obccos.vnpt.vn/ob24h/getList24H?stb=&ktv=&page=0&size=10000"
    
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header của client
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API
    response = requests.get(url, headers=headers)
    
    # Trả về kết quả từ API cho client
    return jsonify(response.json()), response.status_code

@app.route('/obccos/HenGoiLaiCKD', methods=['GET'])
def HenGoiLaiCKD():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # URL API GET dữ liệu
    url = "https://api-obccos.vnpt.vn/obAssigneeActionOBHis/get?progId=6583a76346270935aa47ede9&states=4&page=0&size=10000"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header của client
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API
    response = requests.get(url, headers=headers)

    # Trả về kết quả từ API cho client
    return jsonify(response.json()), response.status_code

@app.route('/obccos/HenGoiLaiCKN', methods=['GET'])
def HenGoiLaiCKN():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')
    
    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # URL API GET dữ liệu
    url = "https://api-obccos.vnpt.vn/obAssigneeActionOBHis/get?progId=6583a66046270935aa47ede8&states=4&page=0&size=10000"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Dùng token từ header của client
        'Connection': 'keep-alive',
        'Mac-address': 'WEB',
        'Origin': 'https://obccos.vnpt.vn',
        'Referer': 'https://obccos.vnpt.vn/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'SelectedMenuId': '0',
        'SelectedPath': '',
        'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API
    response = requests.get(url, headers=headers)

    # Trả về kết quả từ API cho client
    return jsonify(response.json()), response.status_code

# Endpoint test server
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Server is running!'})

if __name__ == '__main__':
    CORS(app)
    app.run(host="0.0.0.0", port=9000)
