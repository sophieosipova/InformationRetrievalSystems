from string_machers import naive_string_matcher
from string_machers import rabin_karp_matcher
from string_machers import finite_automation_matcher
from string_machers import compute_transition_funcion
from string_machers import KMP_matcher
from string_machers import BM_matcher
import string




if __name__ == "__main__":
    T = "GCATCGCAGAGAGTATACAGTACG" # "one two three one one two three" #
    P = "GCAGAGAG" #"one"#
    print("Простейший алгоритм поиска подстрок:")
    naive_string_matcher(T, P)

    d = 256
    q = 7
    print(f"\nАлгоритм Карпа-Рабина:")
    rabin_karp_matcher(T, P, d, q)

    print(f"\nАвтоматы поиска подстрок:")
    delta = compute_transition_funcion(P, list(string.printable))
    finite_automation_matcher(T, delta, len(P))

    print(f"\nАлгоритм Кнутта-Морриса-Пратта:")
    KMP_matcher(T, P)

    print(f"\nАлгоритм Бойера-Мура:")
    BM_matcher(T, P)
