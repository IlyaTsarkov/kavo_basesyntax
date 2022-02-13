def get_list(func):
    def result(*args, **kwargs):
        res_list = []
        for item in func(*args, **kwargs):
            res_list.append(item)
        res = sorted(res_list)
        return res

    return result


@get_list
def show_list(s):
    return s


my_s = map(int, input().split())
print(show_list(my_s))
