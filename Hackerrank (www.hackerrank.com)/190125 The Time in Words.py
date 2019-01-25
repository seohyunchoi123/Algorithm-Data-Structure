# Question Link : https://www.hackerrank.com/challenges/the-time-in-words/problem

def timeInWords(h, m):
    string = ['o\' clock ', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven',  'twelve', 'thirteen', 'fourteen', 'quarter',
              'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five',
              'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half']
    if m > 30: # deceding strings of m, h, conjunction
        m = 60 - m
        h += 1
        conj = 'to'
    elif m == 0:
        return "{} {}".format(string[h], string[0])
    else:
        conj = 'past'

    if m == 1: # deciding whether it's minute or minutes or none
        return "{} minute {} {}".format(string[m], conj, string[h])
    elif m == 15 or m == 30:
        return "{} {} {}".format(string[m], conj, string[h])
    else:
        return "{} minutes {} {}".format(string[m], conj, string[h])

# Time Complexity : O(1)
# Space Complexity : O(1)