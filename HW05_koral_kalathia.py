from typing import Iterator

"""
String manipulation program
"""


def reverse(s: str) -> str:
    """This function is to reverse the given string"""
    reversestr: str = ""
    for i in s:
        reversestr = i + reversestr
    return reversestr


def substring(target: str, s: str) -> int:
    """This function finds the index of a target substring in a given string"""
    for i in range(len(s)):
        if target == "":
            return -1
        elif target == s[i:i + len(target)]:
            return i
    return -1


def find_second(target: str, s: str) -> int:
    """The function finds the index of second occurrences of the substring"""
    if target in s:
        f_occ: int = s.find(target)
        s_occ: int = s.find(target, f_occ + 1)
        if target == "":
            return -1
        elif s_occ != 0:
            return s_occ
        else:
            return -1


def get_lines(path: str) -> Iterator[str]:
    """
    The function reads the file
    combine lines that end with a backslash with the subsequent
    line or lines until a line is found that does not end with a backslash
    """
    try:
        fp = open("part_4_test.txt")
    except FileNotFoundError as e:
        print(f"{fp} not found!! {e}")
    else:
        with fp:
            for line in fp:
                line = line.strip('\n')
                while line.endswith("\\"):  # merge continued lines
                    line = line[:line.find("\\")]
                    line = line + fp.readline().strip('\n')

                if '#' in line:
                    if line.startswith("#"):
                        # print(line)
                        del line
                    else:
                        line = line[:line.find("#")]
                        yield line
                else:
                    yield line


if __name__ == '__main__':
    reverse("koral")
    substring("ral", "koral")
    find_second("aa", "aabb")
    for i in get_lines("part_4_test.txt"):
        print(i)
