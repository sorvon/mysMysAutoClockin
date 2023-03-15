import logging
import argparse
import requests

logging.basicConfig(
  level = logging.INFO,
  format = '%(asctime)s %(levelname)s %(message)s',
  datefmt = '%Y-%m-%dT%H:%M:%S')

cookie = ""

def clockin(cookie: str) -> None:
    url = "https://www.hifini.com/sg_sign.htm"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8",
        "cookie": cookie,
        "origin": "https://www.hifini.com",
        "referer": "https://www.hifini.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "Referer": "https://w1.v2free.net/auth/login",
    }
    response = requests.Session().post(url=url, headers=headers)
    # logging.info(response.text)
    if response.status_code == 200:
        logging.info("clock in success")
    else:
        logging.error(response.status_code)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='hifi')
    parser.add_argument('--cookie', type=str)
    args = parser.parse_args()
    cookie_list = args.cookie.split('\n')
    for cookie in cookie_list:
        clockin(cookie)
