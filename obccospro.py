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

@app.route('/obccos/GetListUser', methods=['GET'])
def GetListUser():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # URL API GET danh sách người dùng
    url = "https://api-obccos.vnpt.vn/list-user?size=9999"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Sử dụng token từ header của client
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
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }

    # Gửi GET request đến API
    response = requests.get(url, headers=headers)

    # Kiểm tra mã phản hồi từ API
    if response.status_code == 200:
        response_json = response.json()
        if response_json['code'] == 200:
            # Trích xuất danh sách người dùng từ response
            users = response_json['data']['data']

            # Lọc các user_name cần thiết
            filtered_users = [
                user for user in users 
                if user['user_name'] in ['tuyenvtt_vtag', 'trild_agg_vnp2', 'thaont1_agg_vnp2', 'loanntp1_agg_vnp2', 'hoangnb_agg_vnp2', 'lyhtt2_agg_vnp2', 'giangtt_agg_vnp2', 'ngochtk1_agg_vnp2', 'nhintb_agg_vnp2', 'luyennt_agg_vnp2', 'binhnny_agg_vnp2', 'nhungbtn_agg_vnp2', 'phuongdtm_agg_vnp2']
            ]

            # Cấu trúc response trả về cho client
            return jsonify({
                "code": 200,
                "data": {
                    "data": filtered_users,
                    "total_page": 1,
                    "total_row": len(filtered_users)
                },
                "error_msg": "",
                "msg": "List user success"
            }), 200
        else:
            return jsonify({"error": response_json.get("error_msg", "Unknown error")}), 400
    else:
        return jsonify({"error": "Failed to fetch data from API"}), response.status_code

@app.route('/obccos/ChuyenOB', methods=['PUT'])
def ChuyenOB():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy các parameters từ query string
    progId = request.args.get('progId') # ID của chương trình CKD hoặc CKN
    id_value = request.args.get('id') # ID của SDT được lưu hẹn gọi lại
    pban = "5fff2235-f72c-8aff-ff80-efcb607008a0" # AGG là 5fff2235-f72c-8aff-ff80-efcb607008a0 nên fix cứng luôn
    ktv = request.args.get('ktv') # user_code của DTV

    # Kiểm tra các parameters bắt buộc
    if not progId or not id_value or not ktv:
        return jsonify({"error": "Missing required parameters"}), 400

    # URL API chuyển TB (OB) với các parameters từ client
    url = f"https://api-obccos.vnpt.vn/cnhan/chuyenTb?progId={progId}&id={id_value}&pban={pban}&ktv={ktv}"

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
        'Authorization': token,  # Sử dụng token từ header của client
        'Connection': 'keep-alive',
        'Content-Length': '0',
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

    payload = {}

    # Gửi PUT request đến API
    response = requests.put(url, headers=headers, data=payload)

    # Trả về kết quả cho client
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to perform request"}), response.status_code

@app.route('/obccos/BaoCaoCKN', methods=['GET'])
def BaoCaoCKN():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy các parameters từ query string
    vnptOrgCode = "AGG"  # Mặc định là 'AGG' nếu không có
    loaiCt = "654a0177809c73686543c3b5"
    fromN = request.args.get('fromN')
    toN = request.args.get('toN')
    page = 1
    size = 100000

    # Nhận giá trị "EMPLOYEENAME" từ query parameter
    employeename = request.args.get('employeename') # employeename là user_name của client truyền vào (ví dụ: thaont1_agg_vnp2)

    # Kiểm tra các parameters bắt buộc
    if not loaiCt or not fromN or not toN or not employeename:
        return jsonify({"error": "Missing required parameters"}), 400

    # URL API báo cáo CKN với các parameters từ client
    url = f"https://api-obccos.vnpt.vn/bcCKN/view32?vnptOrgCode={vnptOrgCode}&loaiCt={loaiCt}&fromN={fromN}&toN={toN}&page={page}&size={size}"

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
    'SelectedMenuId': '0',
    'SelectedPath': '',
    'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    payload = {}

    # Gửi GET request đến API
    response = requests.get(url, headers=headers, data=payload)

    if response.status_code == 200:
        # Lấy dữ liệu JSON từ response
        api_data = response.json()

        # Lọc các phần tử trong "data" có EMPLOYEENAME khớp với giá trị từ query parameter
        if(employeename != 'tgmthanglxn_agg' and employeename != 'gqkn800126_agg_vnp2'):
            filtered_data = [item for item in api_data['data'] if item['EMPLOYEENAME'] == employeename]

            # Cấu trúc lại response để trả về cho client
            result = {
                "SL": len(filtered_data),  # Cập nhật số lượng phần tử sau khi lọc
                "data": filtered_data,
                "errorCode": api_data.get("errorCode"),
                "message": api_data.get("message")
            }
        else:
            result = response

        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code


@app.route('/obccos/BaoCaoCKD', methods=['GET'])
def BaoCaoCKD():
    # Lấy token từ header của request
    token = request.headers.get('Authorization')

    if not token:
        return jsonify({"error": "Authorization token is required"}), 400

    # Lấy các parameters từ query string
    vnptOrgCode = "AGG"  # Mặc định là 'AGG' nếu không có
    loaiCt = "654a0177809c73686543c3b3"
    fromN = request.args.get('fromN')
    toN = request.args.get('toN')

    # Nhận giá trị "EMPLOYEENAME" từ query parameter
    employeename = request.args.get('employeename') # employeename là user_name của client truyền vào (ví dụ: thaont1_agg_vnp2)

    # Kiểm tra các parameters bắt buộc
    if not loaiCt or not fromN or not toN or not employeename:
        return jsonify({"error": "Missing required parameters"}), 400

    # URL API báo cáo CKN với các parameters từ client
    url = f"https://api-obccos.vnpt.vn/bcCKD/view22?vnptOrgCode={vnptOrgCode}&fromN={fromN}&toN={toN}&loaiCt={loaiCt}"

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
    'SelectedMenuId': '0',
    'SelectedPath': '',
    'Token-id': '97388db0-6ce9-11ea-bc55-0242ac130003',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
    }

    payload = {}

    # Gửi GET request đến API
    response = requests.get(url, headers=headers, data=payload)

    if response.status_code == 200:
        # Lấy dữ liệu JSON từ response
        api_data = response.json()

        # Lọc các phần tử trong "data" có EMPLOYEENAME khớp với giá trị từ query parameter
        if(employeename != 'tgmthanglxn_agg' and employeename != 'gqkn800126_agg_vnp2'):
            filtered_data = [item for item in api_data['data'] if item['EMPLOYEENAME'] == employeename]

            # Cấu trúc lại response để trả về cho client
            result = {
                "SL": len(filtered_data),  # Cập nhật số lượng phần tử sau khi lọc
                "data": filtered_data,
                "errorCode": api_data.get("errorCode"),
                "message": api_data.get("message")
            }
        else:
            result = response

        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code
    

# Endpoint test server
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({'message': 'Server is running!'})

if __name__ == '__main__':
    CORS(app)
    app.run(host="0.0.0.0", port=9000)
