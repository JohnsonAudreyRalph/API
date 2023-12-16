import requests

base_url = 'http://johnsonaudreyralph.top/delete_data_view/'

for i in range(39, 256):
    url = f"{base_url}{i}"
    response = requests.get(url)
    
    if response.status_code == 200:
        print(f"Yêu cầu cho URL {url} đã được gửi thành công!")
    else:
        print(f"Có lỗi xảy ra khi gửi yêu cầu đến URL {url}.")
