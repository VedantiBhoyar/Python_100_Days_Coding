// https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

def mutate_string(string, position, character):

    altered=list(string)
    altered[position]=character
    return "".join(altered)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
