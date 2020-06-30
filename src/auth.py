import random, requests, time

class Auth:
    _threshold = 200
    _accounts = []

    @staticmethod
    def setup(accounts:list, threshold: int):
        Auth._threshold = threshold
        Auth._accounts = accounts

    @staticmethod
    def get():
        account = random.choice(Auth._accounts)
        return (account["username"], account["token"])

    @staticmethod
    def check(request:requests.Response):
        try:
            if int(request.headers["X-RateLimit-Remaining"]) < Auth._threshold:
                for _ in range(request.headers["X-RateLimit-Reset"]):
                    time.sleep(1)
        except:
            pass