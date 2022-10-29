import requests
from cashu.tor.tor import TorProxy


def test_tor_setup():
    s = requests.Session()

    tor = TorProxy(keep_alive=False)
    tor.wait_until_startup()
    socks_host, socks_port = "localhost", 9050

    proxies = {
        "http": f"socks5://{socks_host}:{socks_port}",
        "https": f"socks5://{socks_host}:{socks_port}",
    }
    s.proxies.update(proxies)

    resp = s.get("https://google.com")
    resp.raise_for_status()
