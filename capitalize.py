import os


def solve(s):
    output = ''
    names = s.split(' ')
    for name in names :
        if name == '':
            output += ' '
        else :
            if len(name) > 1 :
                output += ' ' + name[0].upper() +name[1:]
            else :
                output += ' ' + name.upper()
    return output[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    print(solve(s))

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()