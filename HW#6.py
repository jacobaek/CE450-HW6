Q1
empty = []
def link(first, rest):
    
    return [first, rest]
def tem(lst):
    if type(lst) != list:
            
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])
def cntn_link(lst,n):
    lst=tem(lst)
    print(lst)
    for i in lst:
        if(i==n):
            return True
    return False    

    

print(cntn_link(link(1, link(2, link(3, empty ))),4))

Q2
empty = []

def link(first, rest):
    
    return [first, rest]
def tem(lst):
    if type(lst) != list:
        
        return [lst]
    else:
        return sum([tem(elem) for elem in lst],[])
def prnt_lnk(lst):
    lst= tem(lst)
    return [i for i in lst]



print(prnt_lnk(link(1, link(2, link(3, link(4,[]))))))

Q3

def is_link(s):
    return s == [] or (len(s) == 2 and is_link(s[1]))

def extend_link(s, t):
    assert is_link(s) and is_link(t)
    if s == []:
        return t
            else:
                return  link(s[0],  extend_link(rest(s), t))

def len_link_recursive(s):
    if  s == []:
        return 0
            return  1+len_link_recursive(rest(s))


def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    assert s != [], "empty linked list has no rest."
    return s[1]

def rvrs_lnk(s):
    a = []

    while len_link_recursive(s) > 0:
        a = extend_link([s[0], []], a)
        s = rest(s)
            
            return a


s = [1, [2, [3, [4, [ ] ]]]]
print(rvrs_lnk(s))


Q4

def is_link(s):
    return s == [] or (len(s) == 2 and is_link(s[1]))

def extend_link(s, t):
    assert is_link(s) and is_link(t)
    if s == []:
        return t
            else:
                return  link(s[0],  extend_link(rest(s), t))

def len_link_recursive(s):
    if  s == []:
        return 0
            return  1+len_link_recursive(rest(s))


def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    assert s != [], "empty linked list has no rest."
    return s[1]

def first(s):
    
    assert is_link(s), "first only applies to linked lists."
    assert s != [], "empty linked list has no first element."
    return s[0]

def srt(lnk):
    print(lnk)
    if len_link_recursive(lnk) == 1:
        return True
            elif first(lnk) > first(lnk[1]):
                return False
                    else:
return srt(lnk[1])

lnk1 = link(1, link(2, link(3, link(4, []))))
print(srt(lnk1))
lnk2 = link(1, link(2, link(3, link(4, link(3, [])))))
print(srt(lnk2))
lnk3 = link(3, link(3, link(3, [])))
print(srt(lnk3))


Q5
empty = []
def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))



def len_link_recursive(s):
    if  s == empty:
    return 0
        return  1+len_link_recursive(rest(s))


def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    
        return s[1]
def first(s):
    assert is_link(s), "first only applies to linked lists."
    
    return s[0]
def sum_lnk(lnk1, sqr):
    i=0
    while lnk1!=[]:
        i+=sqr(first(lnk1))
        lnk1=rest(lnk1)
    return i

sqr = lambda x: x * x
dbl = lambda y: 2 * y
lnk1 = link(1, link(2, link(3, link(4, empty))))
print(sum_lnk(lnk1, sqr))
lnk2 = link(3, link(5, link(4, link(6, empty))))
print(sum_lnk(lnk2, dbl))


Q6
empty = []
def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))



def len_link_recursive(s):
    if  s == empty:
    return 0
        return  1+len_link_recursive(rest(s))


def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    
        return s[1]
def first(s):
    assert is_link(s), "first only applies to linked lists."
    
    return s[0]
def extend_link(s, t):
    
    assert is_link(s) and is_link(t)
    if s == empty:
    return t
        else:
            return  link(s[0],  extend_link(rest(s), t))
def change(l,a,b):
    t=[]
    while l!=[]:
        if first(l)==a:
            l[0]=b
        t = extend_link(t,[l[0], []])
        l=rest(l)
    return t

l = link(1, link(2, link(3, empty)))
n=change(l, 3, 1)
print(n)
m=change(n, 1, 2)
print(m)

Q7
def link(first, rest):
    return [first, rest]
def first(s):
    return s[0]
def extend_link(s, t):
    if s == []:
        return t
            else:
                return  link(s[0],  extend_link(s[1], t))
def apnd(l,a):
    return extend_link(l,[a,[]])
def rest(s):
    return s[1]

l = link(1, link(2, link(3, [])))
n = apnd (l, 4)
print(n)
print(first(rest(rest(rest(n)))))

Q8
empty = []
def is_link(s):
    return s == empty or (len(s) == 2 and is_link(s[1]))



def len_link_recursive(s):
    if  s == empty:
    return 0
        return  1+len_link_recursive(rest(s))


def link(first, rest):
    assert is_link(rest), "rest must be a linked list."
    return [first, rest]

def rest(s):
    assert is_link(s), "rest only applies to linked lists."
    
        return s[1]
def first(s):
    assert is_link(s), "first only applies to linked lists."
    
    return s[0]
def extend_link(s, t):
    assert is_link(s) and is_link(t)
    if s == empty:
    return t
        else:
            return  link(s[0],  extend_link(rest(s), t))
def insrt(l, elm, ind):
    count=0
    t=[]
    while l!=[]:
        if count==ind:
            t = extend_link(t,[elm, []])
        t = extend_link(t,[l[0], []])
        if (rest(l))==[] and count<ind:
            t = extend_link(t,[elm, []])
        count+=1
        l=rest(l)
    return t


l = link(11, link(12, link(13, empty)))
n = insrt(l, 2019, 1)
print(n)
m = insrt(n, 2020, 20)
print(m)


