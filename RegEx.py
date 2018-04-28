# 传说中的正则表达式
import re # 正则表达式的模块
# pattern1 in string 一个简单的自带的匹配
import re

# python自带的匹配
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(pattern1 in string)    # True
print(pattern2 in string)    # False


# 正则表达式的匹配
pattern1 = "cat"
pattern2 = "bird"
string = "dog runs to cat"
print(re.search(pattern1, string))  # <_sre.SRE_Match object; span=(12, 15), match='cat'>
# 会返回找到了谁，在哪里
print(re.search(pattern2, string))  # None


# multiple patterns ("run" or "ran")
ptn = r"r[au]n"       # start with "r" means raw string
print(re.search(ptn, "dog runs to cat"))    # <_sre.SRE_Match object; span=(4, 7), match='run'>
# 指定多个找的可能性
# 前方的r代表正则表达式

# 多个字母集合
print(re.search(r"r[A-Z]n", "dog runs to cat"))     # None
print(re.search(r"r[a-z]n", "dog runs to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='run'>
print(re.search(r"r[0-9]n", "dog r2ns to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='r2n'>
print(re.search(r"r[0-9a-z]n", "dog runs to cat"))  # <_sre.SRE_Match object; span=(4, 7), match='run'>


# \d : 相当于所有的数字
print(re.search(r"r\dn", "run r4n"))                # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \D : 所有不是数字的东西
print(re.search(r"r\Dn", "run r4n"))                # <_sre.SRE_Match object; span=(0, 3), match='run'>
# \s : any white space [\t空白\n换行\r\f\v] 各种和空白有关的东西
print(re.search(r"r\sn", "r\nn r4n"))               # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
# \S : 除了\s之外的东西
print(re.search(r"r\Sn", "r\nn r4n"))               # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \w : 小写大写数字下划线
print(re.search(r"r\wn", "r\nn r4n"))               # <_sre.SRE_Match object; span=(4, 7), match='r4n'>
# \W : 补集
print(re.search(r"r\Wn", "r\nn r4n"))               # <_sre.SRE_Match object; span=(0, 3), match='r\nn'>
# \b : 匹配前一个后一个只有一个空格
print(re.search(r"\bruns\b", "dog runs to cat"))    # <_sre.SRE_Match object; span=(4, 8), match='runs'>
# \B : 都可以匹配empty string (but not at the start or end of a word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))  # <_sre.SRE_Match object; span=(8, 14), match=' runs '>
# \\ : match \　匹配\
print(re.search(r"runs\\", "runs\ to me"))          # <_sre.SRE_Match object; span=(0, 5), match='runs\\'>
# . : match anything (except \n) 除了换行以外的所有
print(re.search(r"r.n", "r[ns to me"))              # <_sre.SRE_Match object; span=(0, 3), match='r[n'>
# ^ : match line beginning句首才会被匹配
print(re.search(r"^dog", "dog runs to cat"))        # <_sre.SRE_Match object; span=(0, 3), match='dog'>
# $ : match line ending句尾～
print(re.search(r"cat$", "dog runs to cat"))        # <_sre.SRE_Match object; span=(12, 15), match='cat'>
# ? : may or may not occur 有没有都可以
print(re.search(r"Mon(day)?", "Monday"))            # <_sre.SRE_Match object; span=(0, 6), match='Monday'>
print(re.search(r"Mon(day)?", "Mon"))               # <_sre.SRE_Match object; span=(0, 3), match='Mon'>


# multi-line
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))                     # None
print(re.search(r"^I", string, flags=re.M))         # <_sre.SRE_Match object; span=(18, 19), match='I'>
# 每一行当成一句话，这样子可以匹配新行的句首　Ｍ　multiline　

# * : occur 0 or more times出现０或好多次
print(re.search(r"ab*", "a"))                       # <_sre.SRE_Match object; span=(0, 1), match='a'>
print(re.search(r"ab*", "abbbbb"))                  # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# + : occur 1 or more times１或多次
print(re.search(r"ab+", "a"))                       # None
print(re.search(r"ab+", "abbbbb"))                  # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>

# {n, m} : occur n to m times：ｎ或多次
print(re.search(r"ab{2,10}", "a"))                  # None
print(re.search(r"ab{2,10}", "abbbbb"))             # <_sre.SRE_Match object; span=(0, 6), match='abbbbb'>


# group
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())                                # 021523, Date: Feb/12/2017
print(match.group(1))                               # 021523
print(match.group(2))                               # Date: Feb/12/2017

match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))                            # 021523
print(match.group('date'))                          # Date: Feb/12/2017

# findall
print(re.findall(r"r[ua]n", "run ran ren"))         # ['run', 'ran']

# | : or
print(re.findall(r"(run|ran)", "run ran ren"))      # ['run', 'ran']

# re.sub() replace
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))     # dog catches to cat

# re.split()
print(re.split(r"[,;\.]", "a;b,c.d;e"))             # ['a', 'b', 'c', 'd', 'e']


# compile
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))     # <_sre.SRE_Match object; span=(4, 7), match='ran'>
