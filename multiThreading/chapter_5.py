import multiprocessing
import requests
import time
import threading


def download(url):
    print(f"Starting to download")
    response=requests.get(url)
urls=[
"https://api.example.com/users",
"https://api.example.com/users/42",
"https://api.example.com/products?page=2&limit=10",
"https://shop.demo.io/orders?status=pending",
"https://weather.app/api/current?city=Hyderabad",
"https://newsportal.dev/articles/technology",
"https://maps.service.com/location?lat=17.3850&lng=78.4867",
"https://banking.test/api/accounts/1001/balance",
"https://socialhub.net/posts?tag=reactjs",
"https://fileserver.org/download/report.pdf",
"https://music.api.com/search?q=arijit+singh",
"https://moviesdb.dev/api/movies/top-rated",
"https://university.edu/api/students/567/results",
"https://sportsdata.io/matches/live",
"https://inventory.app/items?category=laptops&sort=price",
"https://api.example.com/users",
"https://api.example.com/users/42",
"https://api.example.com/products?page=2&limit=10",
"https://shop.demo.io/orders?status=pending",
"https://weather.app/api/current?city=Hyderabad",
"https://newsportal.dev/articles/technology",
"https://maps.service.com/location?lat=17.3850&lng=78.4867",
"https://banking.test/api/accounts/1001/balance",
"https://socialhub.net/posts?tag=reactjs",
"https://fileserver.org/download/report.pdf",
"https://music.api.com/search?q=arijit+singh",
"https://moviesdb.dev/api/movies/top-rated",
"https://university.edu/api/students/567/results",
"https://sportsdata.io/matches/live",
"https://inventory.app/items?category=laptops&sort=price","https://api.example.com/users",
"https://api.example.com/users/42",
"https://api.example.com/products?page=2&limit=10",
"https://shop.demo.io/orders?status=pending",
"https://weather.app/api/current?city=Hyderabad",
"https://newsportal.dev/articles/technology",
"https://maps.service.com/location?lat=17.3850&lng=78.4867",
"https://banking.test/api/accounts/1001/balance",
"https://socialhub.net/posts?tag=reactjs",
"https://fileserver.org/download/report.pdf",
"https://music.api.com/search?q=arijit+singh",
"https://moviesdb.dev/api/movies/top-rated",
"https://university.edu/api/students/567/results",
"https://sportsdata.io/matches/live",
"https://inventory.app/items?category=laptops&sort=price","https://api.example.com/users",
"https://api.example.com/users/42",
"https://api.example.com/products?page=2&limit=10",
"https://shop.demo.io/orders?status=pending",
"https://weather.app/api/current?city=Hyderabad",
"https://newsportal.dev/articles/technology",
"https://maps.service.com/location?lat=17.3850&lng=78.4867",
"https://banking.test/api/accounts/1001/balance",
"https://socialhub.net/posts?tag=reactjs",
"https://fileserver.org/download/report.pdf",
"https://music.api.com/search?q=arijit+singh",
"https://moviesdb.dev/api/movies/top-rated",
"https://university.edu/api/students/567/results",
"https://sportsdata.io/matches/live",
"https://inventory.app/items?category=laptops&sort=price",
]

start = time.time()

# for many 
if __name__ =="__main__":
    process=[]
    
    for url in urls:
        p=multiprocessing.Process(target=download, args=(url,))
        p.start()
        process.append(p)
    
    for p in process:
        p.join()
    
    print("done with processing ", time.time()-start)
            
# threads=[]
# for url in urls:
#     t=threading.Thread(target=download, args=(url, ))
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()
# print("Done with threading ", time.time()- start)
