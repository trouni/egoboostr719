import requests


def get_quote(name=None):
    url = "https://api.chucknorris.io/jokes/random?category=dev"
    quote = requests.get(url).json()["value"]

    if name:
        quote = quote.replace("Chuck Norris", name.title())

    return quote


if __name__ == "__main__":
    print(get_quote("Doug"))
