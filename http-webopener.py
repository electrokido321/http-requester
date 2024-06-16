import requests
import time

# List of URLs to request
urls = [
    'http://46.166.165.33:4002',
'http://5.189.184.6:80',
'http://156.200.116.69:1976',
'http://207.244.217.18:6565',
'http://185.66.59.77:42647',
'http://223.207.102.16:4000',
'http://85.26.218.112:3128',
'http://191.97.16.6:999',
'http://162.241.45.22:40634',
'http://190.52.178.17:80',
'http://104.239.105.236:6766',
'http://45.4.144.232:4153',
'http://197.232.10.202:41890',
'http://20.204.212.45:3129',
'http://150.230.207.167:80',
'http://154.49.246.35:80',
'http://190.61.88.147:8080',
'http://50.47.75.211:5678',
'http://177.229.210.50:8080',
'http://20.24.43.214:80',
'http://92.247.12.139:9510',
'http://184.178.172.25:15291',
'http://64.202.184.129:35224',
'http://139.180.146.114:34959',
'http://185.190.90.2:4145',
'http://154.16.146.42:80',
'http://177.234.192.47:32213',
'http://200.106.184.97:999',
'http://176.62.188.158:3629',
'http://32.223.6.94:80',
'http://156.239.49.4:3128',
'http://83.218.186.22:5678',
'http://192.81.128.182:8089',
'http://60.217.64.237:35292',
'http://104.233.26.15:5853',
'http://192.141.196.129:8080',
'http://200.108.50.254:4145',
'http://154.203.132.55:8090',
'http://36.94.234.177:5678',
'http://156.239.53.60:3128',
'http://85.117.56.147:8080',
'http://156.239.53.123:3128',
'http://177.93.51.213:999',
'http://104.165.169.61:3128',
'http://199.102.106.94:4145',
'http://45.126.169.233:4145',
'http://38.41.0.60:11201',
'http://72.10.164.178:14743',
'http://103.9.134.234:100',
'http://77.105.136.28:1995',
'http://152.231.25.114:8080',
'http://67.43.228.251:16803',
'http://27.254.46.194:80',
'http://212.192.31.37:3128',
'http://185.105.89.249:4444',
'http://198.74.51.79:8888',
'http://168.232.60.62:5678',
'http://50.172.75.124:80',
'http://38.60.196.242:3128',
'http://188.132.222.37:8080',
'http://189.203.181.34:8080',
'http://156.239.48.111:3128',
'http://18.133.16.21:1080',
'http://154.79.252.174:8080',
'http://91.92.155.207:3128',
'http://38.10.250.5:999',
'http://104.239.80.152:5730',
'http://180.210.222.201:1080',
'http://202.61.251.201:9097',
'http://188.132.222.38:8080',
'http://98.115.234.64:80',
'http://120.194.4.157:82',
'http://182.72.203.246:80',
'http://200.85.137.1:4153',
'http://104.143.248.139:6749',
'http://103.176.179.84:3128',
'http://13.40.239.13:3128',
'http://103.36.11.246:8181',
'http://121.200.60.122:4153',
'http://91.189.177.189:3128',
'http://194.9.80.1:5060',
'http://92.154.84.215:80',
'http://168.205.102.26:8080',
'http://220.248.70.237:9002',
'http://190.58.248.86:80',
'http://1.20.95.95:5678',
'http://142.147.131.163:6063',
'http://27.123.1.33:4153',
'http://101.255.116.125:8080',
'http://184.178.172.3:4145',
'http://185.25.119.34:6129',
'http://103.239.200.226:1337',
'http://41.217.223.145:32650',
'http://46.249.155.6:5678',
'http://206.206.73.251:6867',
'http://46.101.195.252:18282',
'http://46.227.36.1:1088',
'http://202.162.105.202:8000',
'http://67.43.236.19:28449',
'http://179.255.219.182:8080',
'http://41.33.203.233:1975',
'http://46.105.44.110:80',
'http://103.216.49.151:8080',
'http://103.163.244.49:83',
'http://104.239.104.88:6312',
'http://101.109.251.42:4145',
'http://197.234.13.44:4145',
'http://31.128.69.121:8080',
'http://190.97.238.90:999',
'http://154.19.84.127:8080',
'http://116.212.142.75:33427',
'http://159.192.253.92:4145',
'http://103.165.64.86:4153',
'http://72.10.160.91:31711',
'http://176.120.32.135:5678',
'http://115.127.83.142:1234',
'http://181.224.65.50:999',
'http://118.69.62.229:5678',
'http://109.194.22.61:8080',
'http://211.174.105.26:4153',
'http://103.15.245.18:4153',
'http://188.191.164.55:4890',
'http://45.179.71.90:3180',
'http://159.203.104.153:8200',
'http://50.222.245.46:80',
'http://186.251.255.149:31337',
'http://103.37.111.253:18081',
'http://185.108.141.19:8080',
'http://50.168.72.118:80',
'http://118.174.14.65:44336',
'http://110.78.148.198:4145',
'http://147.185.217.38:6472',
'http://179.111.216.102:3629',
'http://45.41.162.168:6805',
'http://200.81.144.9:1080',
'http://103.49.114.195:8080',
'http://103.115.20.52:8199',
'http://103.76.172.230:4153',
'http://27.147.131.122:8090',
'http://103.253.153.242:41762',
'http://45.184.152.81:999',
'http://193.163.200.207:80',
'http://103.180.123.73:8080',
'http://176.9.119.252:30172',
'http://200.108.197.2:8080',
'http://43.132.184.228:8181',
'http://170.83.244.233:8080'
]

# Number of times to request each URL
num_requests = 5

# Function to send HTTP requests
def send_requests(url):
    for _ in range(num_requests):
        try:
            response = requests.get(url, timeout=10)
            print(f"Request to {url} - Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request to {url} failed: {e}")
        time.sleep(1)  # Delay between requests to avoid rate limits or server overload

# Loop through each URL and send requests
for url in urls:
    send_requests(url)