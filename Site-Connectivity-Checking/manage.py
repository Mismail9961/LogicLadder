import urllib.request as urllib

def site_connectivity_checking():
    print("Welcome to the site connectivity checker")
    url = input("Enter the url of the site: ")
    response = urllib.urlopen(url)
    print(f"The response code is {response.getcode()}")

site_connectivity_checking()