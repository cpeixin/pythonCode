def make_complex(x, y):
    return {'x': x, 'y': y}



if __name__ == '__main__':
    x = make_complex(4,5)["x"]
    print(x)