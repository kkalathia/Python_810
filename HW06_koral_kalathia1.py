from typing import Any, List, Optional


def list_copy(l: List[Any]) -> List[Any]:
    return [x for x in l]


def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
    return [x for x in l1 if x in l2]


def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
    return [x for x in l1 if x not in l2]


def remove_vowels(string: str) -> str:
    vowels = 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'
    string: str = string.split(" ")
    return (" ".join([x for x in string if not x.startswith(vowels)]))


def check_pwd(password: object) -> object:
    pwd: List = list(password)
    if pwd[0].isdigit():
        a = [x for x in pwd if x.islower()]
        b = [y for y in pwd if y.isupper()]
        if len(a) >= 1 and len(b) >= 2:
            return True
        else:
            return False
    else:
        return False


class DonutQueue:
    def __init__(self) -> None:
        self.queue = list()
        self.vip_q = list()
        self.nc = list()

    def arrive(self, name: str, vip: bool) -> None:
        if vip == True:
            self.vip_q.append(name)
        else:
            self.queue.append(name)

    def next_customer(self) -> Optional[str]:
        self.nc = self.vip_q + self.queue
        if len(self.vip_q) > 0:
            f_n: str = self.nc[0]
            self.vip_q.pop(0)
            return f_n
        elif len(self.queue) > 0:
            f_n: str = self.nc[0]
            self.queue.pop(0)
            return f_n
        else:
            return None

    def waiting(self) -> Optional[str]:
        if len(self.vip_q) > 0:
            if len(self.queue) > 0:
                return ', '.join(self.vip_q + self.queue)
        elif len(self.queue) > 0:
            return ', '.join(self.queue)
        else:
            return None


if __name__ == '__main__':
    lc = list_copy(['1', '2', '3', '4', '5'])
    li = list_intersect(['1', '2', '3', '4'], ['2', '3', '5', '6', '7'])
    ld = list_difference(['1', '2', '3', '4'], ['2', '10', '11', '12'])
    rv = remove_vowels("I am Koral Kalathia")
    cp = check_pwd("1Koral")
    cp1 = check_pwd("1KOral")
    print(lc)
    print(li)
    print(ld)
    print(rv)
    print(cp)
    print(cp1)
    dq = DonutQueue()
    dq.arrive("Pooja", False)
    dq.arrive("Koral", True)
    dq.arrive("Hardik", True)
    dq.arrive("Heli", False)
    print(dq.next_customer())
    print(dq.next_customer())
    print(dq.waiting())
    print(dq.next_customer())
    print(dq.next_customer())
    print(dq.waiting())
