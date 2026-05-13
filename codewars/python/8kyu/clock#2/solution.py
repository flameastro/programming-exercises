def past(h, m, s):
    return (s + (m * 60) + (h * 3600)) * 1000



if __name__ == "__main__":
    print(past(1, 1, 1))  # 3661000
    print(past(23, 59, 59))  # 86399000
    print(past(4, 12, 43))  # 15163000
