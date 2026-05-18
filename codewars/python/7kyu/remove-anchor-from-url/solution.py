# Complete the function/method so that it returns the url with anything after the anchor (#) removed.
# Examples
# "www.codewars.com#about" --> "www.codewars.com"
# "www.codewars.com?page=1" -->"www.codewars.com?page=1"
def remove_url_anchor(url):
    return url[:url.index("#")] if "#" in url else url


if __name__ == "__main__":
    print(remove_url_anchor("www.codewars.com#about"))  # www.codewars.com
    print(remove_url_anchor("www.codewars.com?page=1"))  # www.codewars.com?page=1
    print(remove_url_anchor("www.codewars.com/katas/?page=1#about"))  # www.codewars.com/katas/?page=1
