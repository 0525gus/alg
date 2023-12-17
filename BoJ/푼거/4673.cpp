#include <iostream>
using namespace std;

bool flag[10001];

int d(int n) {
	int x = n;
	while (n != 0) {
		x += n % 10;
		n /= 10;
	}
	return x;
}
int main() {
	for (int i = 1;i < 10001;i++) {
		if (d(i) < 10001)flag[d(i)] = true;
	}

	for (int i = 1; i < 10001; i++) {
		if (!flag[i]) {
			cout << i << endl;
		}
	}
	return 0;
}
