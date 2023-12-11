#include <bits/stdc++.h>

using namespace std;

int encontrarMelhorConjunto(const vector<pair<int, int>> &, set<int> &, const int);

int main() {
    vector<pair<int, int>> itens;
    int n;
    int qtde;
    int peso;
    int casos;

    cin >> casos;

    while (casos--) {
        cin >> n;
        itens.push_back(make_pair(0, 0));

        for (int i = 0; i < n; i++) {
            cin >> qtde >> peso;
            itens.push_back(make_pair(qtde, peso));
        }

        const int pesoMaximo = 51;
        set<int> melhoresItens;
        int melhorValor = encontrarMelhorConjunto(itens, melhoresItens, pesoMaximo);

        cout << melhorValor << " brinquedos\n";

        int pesoTotal = 0;
        for (set<int>::const_iterator si = melhoresItens.begin(); si != melhoresItens.end(); si++) {
            pesoTotal += (itens.begin() + *si)->second;
        }

        cout << "Peso: " << pesoTotal << " kg\nsobra(m) " << n - melhoresItens.size() << " pacote(s)\n\n";
        itens.clear();
    }

    return 0;
}

int encontrarMelhorConjunto(const vector<pair<int, int>> &itens, set<int> &melhoresItens, const int limitePeso) {
    const int n = itens.size();
    int melhoresValores[n][limitePeso];
    set<int> conjuntosSolucao[n][limitePeso];
    set<int> conjuntoVazio;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < limitePeso; j++) {
            melhoresValores[i][j] = 0;
            conjuntosSolucao[i][j] = conjuntoVazio;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int peso = 0; peso < limitePeso; peso++) {
            if (i == 0)
                melhoresValores[i][peso] = 0;
            else {
                int pesoItem = (itens.begin() + i)->second;

                if (peso < pesoItem) {
                    melhoresValores[i][peso] = melhoresValores[i - 1][peso];
                    conjuntosSolucao[i][peso] = conjuntosSolucao[i - 1][peso];
                } else {
                    if (melhoresValores[i - 1][peso - pesoItem] + (itens.begin() + i)->first > melhoresValores[i - 1][peso]) {
                        melhoresValores[i][peso] = melhoresValores[i - 1][peso - pesoItem] + (itens.begin() + i)->first;
                        conjuntosSolucao[i][peso] = conjuntosSolucao[i - 1][peso - pesoItem];
                        conjuntosSolucao[i][peso].insert(i);
                    } else {
                        melhoresValores[i][peso] = melhoresValores[i - 1][peso];
                        conjuntosSolucao[i][peso] = conjuntosSolucao[i - 1][peso];
                    }
                }
            }
        }
    }

    melhoresItens.swap(conjuntosSolucao[n - 1][limitePeso - 1]);
    return melhoresValores[n - 1][limitePeso - 1];
}
