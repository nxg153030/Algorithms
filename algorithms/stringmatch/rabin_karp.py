def rabin_karp_matcher(text, pattern, d, q):
    n = len(text)
    m = len(pattern)
    h = d ** (m - 1) % q
    p = 0
    t_0 = 0
    for i in range(0, m): # preprocessing
        p = ((d * p) + pattern[i]) % q
        t_0 = ((d * t_0) + text[i]) % q

    for s in range(0, n - m): # matching
        if p == t_s:
            if pattern[:m] == text[s + 1: s + m]:
                print(f'Pattern match occurs with shift: {s}')

        if s < n - m:
            t_s_plus_1 = () # need to implement this
