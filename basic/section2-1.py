# 2-1
word1 = 'hello'
type(word1)

word2 = str(123)
word = 'hello'
print(word[2])
print(word[-1])

digits1 = '0123456789'
print(digits1[1:4])
print(digits1[-4:-1])
print(digits1[3:9:2])

escaped1 = 'This is \'MINE\''

#practice
def remove_punctuations(str_engsentences):
    str1 = str_engsentences.replace('.', '') # 指定の文字を空文字に置換
    str1 = str1.replace(',', '')
    str1 = str1.replace(':', '')
    str1 = str1.replace(';', '')
    str1 = str1.replace('!', '')
    str1 = str1.replace('?', '')
    return str1

print(remove_punctuations('Quiet, uh, donations, you want me to make a donation to the coast guard youth auxiliary?') == 'Quiet uh donations you want me to make a donation to the coast guard youth auxiliary')

def atgc_bppair(str_atgc):
    str1 = str_atgc.replace('A','t')
    str1 = str1.replace('T','a')
    str1 = str1.replace('G','c')
    str1 = str1.replace('C','g')
    str1 = str1.upper()
    return str1

print(atgc_bppair('AAGCCCCATGGTAA') == 'TTCGGGGTACCATT')

def atgc_count(str_atgc, str_bpname):
    return str_atgc.count(str_bpname)

print(atgc_count('AAGCCCCATGGTAA', 'A') == 5)

def check_lower(str_engsentences):
    if str_engsentences == str_engsentences.lower():
        return True
    return False

print(check_lower('down down down') == True)
print(check_lower('There were doors all round the hall, but they were all locked') == False)