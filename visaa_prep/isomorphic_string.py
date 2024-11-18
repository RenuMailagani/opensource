def are_isomorphic(s, t):
    if len(s) != len(t):
        return "false"
    map_s_to_t = {}
    map_t_to_s = {}
    for char_s, char_t in zip(s, t):
        if map_s_to_t.get(char_s, char_t) != char_t or map_t_to_s.get(char_t, char_s) != char_s:
            return "false"
        map_s_to_t[char_s] = char_t
        map_t_to_s[char_t] = char_s
    return "true"
N=int(input())
s=input().strip()
t=input().strip()
print(are_isomorphic(s, t))
