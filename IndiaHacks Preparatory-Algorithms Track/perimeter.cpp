#include <algorithm>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iterator>
#include <limits>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;


#define REP(i,n)    for(int i=0; i<(n); ++i)
#define FOR(i,a,b)  for(int i=(a); i<=(b); ++i)

const int maxN = 505;
string s[maxN];
int range[maxN][maxN];
int main() {
	int R, C, lastC, res = 0;
	cin >> R >> C;
	REP(r,R) cin >> s[r];
	REP(c,C) range[0][c] = s[0][c] == '.' ? 0 : maxN;
	FOR(r,1,R-1) REP(c,C) if(s[r][c] == '.') range[r][c] = min(range[r-1][c], r); else range[r][c] = maxN;
	REP(r1,R) FOR(r2,r1+1,R-1) {
		lastC = -1;
		REP(c,C) {
			if(s[r1][c] == '.' && s[r2][c] == '.') {
				if(range[r2][c] <= r1) {
					if(lastC != -1) res = max(res, 2*(r2-r1-1)+2*(c-lastC+1));
					else lastC = c; 
				}
			} else {
				lastC = -1;
			}
		}
	}
	if(res == 0) cout << "impossible" << endl;
	else cout << res << endl;
	return 0;
}
