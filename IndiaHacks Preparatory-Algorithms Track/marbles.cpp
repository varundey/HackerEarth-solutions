#include <iostream>
#include <algorithm>
using namespace std;
int main(void) {
        // Helpers for input and output

        int N, K, i;
        cin >> N >> K;
        int C[N];
        for (int i = 0; i < N; i++) {
                cin >> C[i];
        }
        sort(C, C + N);
        int friends[K];
        int cost = 0;
        for (i = 0; i < K; i++) {
                friends[i] = 0;
        }
        int result = 0;
        int c = N - 1;
        while (c >= 0) {
                result += (friends[cost] + 1) * C[c];
                friends[cost] = friends[cost] + 1;
                cost += 1;
                if (cost >= K) {
                        cost = 0;
                }
                c -= 1;
        }

        cout << result << "\n";

        return 0;
}

