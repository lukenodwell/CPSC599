#include <iostream>
#include <vector>

using namespace std;

int main() {
    int p;
    while (cin >> p && p != 4) {
        int count = 0;
        bool is_prime = false;

        while (!is_prime) {
            vector<int> pf;
            count++;

            while (p % 2 == 0) {
                pf.push_back(2);
                p /= 2;
            }

            for (int i = 3; i * i <= p; i += 2) {
                while (p % i == 0) {
                    pf.push_back(i);
                    p /= i;
                }
            }

            if (p > 2) pf.push_back(p);
            if (pf.size() == 1) is_prime = true;

            p = 0;
            for (int i = 0; i < pf.size(); i++) {
                p += pf[i];
            }
        }
        cout << p << " " << count << "\n";
    }
    return 0;
}