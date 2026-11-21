class Solution {
public:
    int countPrimes(int n) {
    if (n <= 2) return 0;

    vector<int> sieve(n, 0); 
    sieve[0] = 1;
    sieve[1] = 1;

    for (long long i = 2; i < n; i++) {
        if (sieve[i] == 0) {
            for (long long j = i * i; j < n; j += i) {
                sieve[j] = 1;
            }
        }
    }

    int ans = 0;
    for (int x : sieve) {
        if (x == 0) ans++;
    }
    return ans;
}
};