import sys


def get_path(n, m):   
    array_circular = list(range(1, n + 1))

    current_index = 0
    path = []

    while True:
        path.append(array_circular[current_index])
        next_index = (current_index + m - 1) % n

        if next_index == 0:
            break

        current_index = next_index

    return path

if __name__ == "__main__":
    
    n = int(sys.argv[1])
    m = int(sys.argv[2])


    path = get_path(n,m)
    print(''.join(map(str,path)))

