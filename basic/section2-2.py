#practice
def remove_evenindex(ln):
    return ln[1::2]

print(remove_evenindex(['a', 'b', 'c', 'd', 'e', 'f', 'g']) == ['b', 'd', 'f'] )
print(remove_evenindex([1, 2, 3, 4, 5]) == [2, 4])

def change_domain(email,domain):
    return '@'.join([email.split('@')[0],domain])

print(change_domain('spam@utokyo-ipp.org', 'ipp.u-tokyo.ac.jp') == 'spam@ipp.u-tokyo.ac.jp')

def reverse_totuple(ln):
    ln.reverse()
    return tuple(ln)

print(reverse_totuple([1, 2, 3, 4, 5]) == (5, 4, 3, 2, 1))

def sum_list(ln):
    sum = 0
    for i in ln:
        sum += i
    return sum

print(sum_list([10, 20, 30]) == 60)
print(sum_list([-1, 2, -3, 4, -5]) == -3)

def atgc_countlist(str_atgc):
    list_count = []
    for value in 'ATGC':
        bpcnt = str_atgc.count(value)
        list_count.append([bpcnt, value])
    return list_count
    
print(sorted(atgc_countlist('AAGCCCCATGGTAA')) == sorted([[5, 'A'], [2, 'T'], [3, 'G'], [4, 'C']]))