import requests
from threading import Thread

def send_request(url):
    response = requests.get(url)
    print(response.status_code)

url = input('Enter the URL: ')
num_requests = int(input('How many times do you want to do it? '))
num_threads = int(input('How many threads? '))

threads = []

for _ in range(num_requests):
    while True:
        if len(threads) < num_threads:
            thread = Thread(target=send_request, args=(url,))
            thread.start()
            threads.append(thread)
            break
        else:
            for thread in threads:
                if not thread.is_alive():
                    threads.remove(thread)
                    break

for thread in threads:
    thread.join()
