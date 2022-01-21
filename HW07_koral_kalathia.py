from typing import List, Tuple
from collections import Counter, defaultdict
import string

'''Author: koral kalathia HW07 this file contains different functions to check anagrams, if the string covers all 
alphabet and a web analyzer and what the specific function does is mentioned in their respective docstrings. '''


def anagrams_lst(str1: str, str2: str) -> bool:
    """This function checks if the two strings are anagrams or not by using only Strings or Lists """
    return True if sorted(str1.lower()) == sorted(str2.lower()) else False


def anagrams_dd(str1: str, str2: str) -> bool:
    """This function checks if the two strings are anagrams or not by using only defaultdict """
    dd = defaultdict(int)
    for i in str1.lower():
        dd[i] += 1
    for c in str2.lower():
        if c in dd.keys():
            dd[c] -= 1
        else:
            return False
    for j in dd.values():
        if j != 0:
            return False
        else:
            pass
    return True


def anagrams_cntr(str1: str, str2: str) -> bool:
    """This function checks if the two strings are anagrams or not by only using Counter function """
    return True if Counter(str1.lower()) == Counter(str2.lower()) else False


def covers_alphabet(sentence: str) -> bool:
    """This function checks if sentence includes at least one instance of every character in the alphabet or not"""
    sentence: set = set("".join(sentence.lower().split()))
    s: set = set(string.ascii_lowercase)
    return True if sentence.intersection(s) == s else False


def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
    """This function summarizes the dictionary in the form of key containing the website name and value has the
    person name who visited the website """
    ddi: defaultdict = defaultdict(set)
    lst: List = []
    [ddi[j].add(i) for i, j in weblogs]
    [lst.append((key, list(sorted(value)))) for key, value in ddi.items()]
    return sorted(lst)


print(covers_alphabet("The quick, brown, fox; jumps over the lazy dog!"))
