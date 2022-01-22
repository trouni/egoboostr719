import requests


def get_quote(name=None):
    url = "https://api.chucknorris.io/jokes/random?category=dev"
    quote = requests.get(url).json()["value"]

    if name:
        quote = quote.replace("Chuck Norris", name.title())

    return quote


def get_gh_user_info(username):
    url = f"https://api.github.com/users/{username}"
    return requests.get(url).json()


if __name__ == "__main__":
    print(get_quote("Doug"))
