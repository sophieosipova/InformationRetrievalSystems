def naive_string_matcher(t, p):
    """
       Простейший алгоритм поиска подстрок
       :param t: текст
       :param p: образец
       :return: void
    """
    n = len(t)
    m = len(p)
    for s in range(0, n - m + 1):
        if p == t[s:s + m]:
            print("Подстрока найдена на позиции: ", s)



def rabin_karp_matcher(t, p, d, q):
    """
       Простейший алгоритм поиска подстрок
       :param t: текст
       :param p: образец
       :param d: разряд
       :param q: простое число
       :return: void
    """
    n = len(t)
    m = len(p)
    h = pow(d, m-1) % q
    p0 = 0
    t0 = 0
    for i in range(0, m):
        p0 = (d * p0 + ord(p[i])) % q
        t0 = (d * t0 + ord(t[i])) % q
    for s in range(0, n - m + 1):
        if p0 == t0 and p == t[s:s + m]:
            print("Подстрока найдена на позиции: ", s)
        if s < n-m:
            t0 = (d * (t0 - ord(t[s])*h) + ord(t[s+m])) % q




def compute_transition_funcion (p, alph):
    """
       Простейший алгоритм поиска подстрок
       :param p: образец
       :param alp: алфавит
       :return: dictionary (функции перехода)
    """
    m = len(p)
    delta = {}
    for q in range(0, m):
        for a in alph:
            k = min(m, q + 1)
            if (p[:k]) not in (p[:q] + a): #not (p[:q] + a).__contains__(p[:k] ):
                k = 0
            delta.update({(q, a): k})
    return delta

def finite_automation_matcher (t, delta, m):
    """
       Простейший алгоритм поиска подстрок
       :param p: образец
       :param alp: алфавит
       :return: void
    """
    n = len(t)
    q = 0
    for i in range(0, n):
        q = delta.get((q, t[i]))
        if q == m:
            q = 0
            print("Подстрока найдена на позиции: ", i - m + 1)


def compute_prefix_function(p):
    """
       Простейший алгоритм поиска подстрок
       :param p: образец
       :return: array (функции перехода)
    """
    m = len(p)
    pi = list()
    pi.append(0)
    k = 0
    for q in range(1, m):
        while k > 0 and p[k] != p[q]:
            k = pi[k-1]
        if p[k] == p[q]:
            k = k + 1
        pi.append(k)
    return pi

def KMP_matcher (t, p):
    """
       Простейший алгоритм поиска подстрок
       :param p: образец
       :param t: текст
       :return: dictionary (функции перехода)
    """
    n = len(t)
    m = len(p)
    pi = compute_prefix_function(p)
    q = 0
    for i in range(0, n):
        while q > 0 and p[q] != t[i]:
            q = pi[q-1]
        if p[q] == t[i]:
            q += 1
        if q == m:
            q = pi[q-1]
            print("Подстрока найдена на позиции: ", i - m + 1)


def preBmBc(p):
    """
       Функция для вычисления таблицы сдвигов плохих символов
       :param p: образец6
       :return: массив плохих сдвигов
    """
    m = len(p)
    # Заполняем значением по умолчанию, равным длине шаблона
    table = [m for i in range(256)]

    # Вычисление функции по определению
    for i in range(0, m-1):
        table[ord(p[i])] = m - 1 - i
    return table

def isPrefix(p, k):
    """
        Функция, проверяющая, что подстрока x[p…m−1] является префиксом шаблона x.
        :param p: образец
        :param k: начало подстроки
        :return: boolean
    """
    m = len(p)
    j = 0
    for i in range(k, m):
        if p[i] != p[j]:
           return False
        j += 1
    return True

def suffixLength(p, k):
    """
        Функция, возвращающая для позиции k длину максимальной подстроки, которая является суффиксом шаблона  p
        :param p: образец
        :param k: начало подстроки
        :return: length: длина максимальной подстроки, которая является суффиксом шаблона  p
    """
    m = len(p)
    length = 0
    i = k
    j = m - 1
    while i >= 0 and p[i] == p[j]:
        length+=1
        i-=1
        j-=1
    return length

def preBmGs(p):
    """
        Функция для вычисления сдвигов хороших суффиксов.
        :param p: образец
        :return: массив хороших сдвигов
    """

    m = len(p)
    table = [m-1 for i in range(m)]
    j = 0
    for i in range(m-1)[::-1]:
        if suffixLength(p, i) == i + 1:
            for j in range (0,m - 1 - i):
                if table[j] == m:
                    table[j] = m - 1 - i
    for i in range(0, m-1):
        table[m - 1 - suffixLength(p, i)] = m - 1 - i
    return table

def BM_matcher (t, p):
    """
       Простейший алгоритм поиска подстрок
       :param p: образец
       :param t: текст
    """
    # Предварительные вычисления
    m = len(p)
    n = len(t)
    bmBc = preBmBc(p)
    bmGs = preBmGs(p)
    for i in range(m-1, n-1):
        j = m - 1
        while p[j] == t[i]:
            if j == 0:
                print("Подстрока найдена на позиции: ", i)
                break
            i -= 1
            j -= 1
        i += max(bmGs[m - 1 - j], bmBc[ord(t[i])])

