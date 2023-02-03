def isEven ( num):
  return num % 2 == 0
 
def isPolindome (mstr):
   return mstr == mstr[::-1]


def get_longest_word(mstr):
    words = mstr.split()
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word


