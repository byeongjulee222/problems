# import datetime
# purchase = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
#
# tier = [0 for _ in range(5)]
#
# info = []
# for i in purchase:
#     info.append(i.split())
#
# date = []
# for i, j in info:
#     date.append(i.split('/'))
# print(info)
# print(date)
# for i in date:
#     print(datetime.date(int(i[0]), int(i[1]), int(i[2])))


def alphaNumber(word):
    alpha = ''
    num = ''
    for w in word:
        if w.isalpha():
            alpha += w
        else:
            num += w

    if len(alpha) == 0 or len(num) == 0: return False
    elif word[0].isdecimal(): return False
    elif num[0] == '0': return False
    elif len(alpha) > 6: return False
    elif len(num) > 6: return False
    elif alpha + num != word: return False
    elif len(alpha) < 3: return False
    for i in alpha:
        if i.isupper():
            return False

    else: return True

def solution(registered_list, new_id):
    answer = ''

    if alphaNumber(new_id):
        if new_id not in registered_list:
            print('ghe')
            return new_id

    alpha = ''
    numb = ''
    for word in new_id:
        if word.isalpha():
            alpha += word
        else:
            numb += word
    new_ = alpha + numb

    print('test', new_)
    if len(numb) == 0:
        numb + '1'
    return answer

print(solution(["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow10"))

# print(alphaNumber('hahaa512'))
