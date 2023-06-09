# include <iostream>
# include <algorithm>
# include <string>
using namespace std;

# ifdef _WIN32
    # define API __declspec(dllexport)
# else
    # define API
# endif

extern "C" {

API int damerau_levenshtein_distance(char* s_char, char* t_char) {
    string s = string(s_char);
    string t = string(t_char);

    int len_s = s.length();
    int len_t = t.length();
    int d[len_s + 1][len_t + 1];

    for (int i = 0; i <= len_s; i++) {
        d[i][0] = i;
    }

    for (int j = 0; j <= len_t; j++) {
        d[0][j] = j;
    }

    for (int i = 1; i <= len_s; i++) {
        for (int j = 1; j <= len_t; j++) {
            int cost = (s[i - 1] == t[j - 1]) ? 0 : 1;

            d[i][j] = min({
                d[i - 1][j] + 1,  // удаление
                d[i][j - 1] + 1,  // вставка
                d[i - 1][j - 1] + cost  // замена
            });

            if (i > 1 && j > 1 && s[i - 1] == t[j - 2] && s[i - 2] == t[j - 1]) {
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + cost);  // транспозиция
            }
        }
    }

    return d[len_s][len_t];
}

}