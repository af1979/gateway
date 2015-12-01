#Python 3.4.3
import sys

def permute(word):
    if len(word) <= 1:
        return [word]

    permutations = permute(word[1:])
    char = word[0]
    result = []

    for permutation in permutations:
        for i in range(len(permutation) + 1):
            result.append(permutation[:i] + char + permutation[i:])
    return result

def main(argv):
    try:
        file_name = argv[1]
    except IndexError:
        print('Must pass file as argument')
        return

    with open(file_name) as f:
        for line in f:
            output = permute(line.strip())
            print(','.join(sorted(output)))

if __name__ == "__main__":
    main(sys.argv)