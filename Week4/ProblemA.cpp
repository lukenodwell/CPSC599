#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, q;
    cin >> n >> q;

    vector<bool> prime(n + 1, true);
    vector<int> queries(q);

    prime[0] = prime[1] = false;

    for (int i = 2; i * i <= n; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                prime[j] = false;
            }
        }
    }

    int prime_count = 0;
    for (int i = 2; i <= n; i++) {
        if (prime[i]) prime_count++;
    }

    cout << prime_count << "\n";

    for (int i = 0; i < q; i++) {
        cin >> queries[i];
    }

    for (int i = 0; i < q; i++) {
        cout << prime[queries[i]] << "\n";
    }

    return 0;
}