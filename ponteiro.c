#include <stdio.h>
#include <stdlib.h>

int main() {
    // Crie um ponteiro que aponta para um inteiro
    int *ponteiro;

    // Aloque memória para armazenar oito inteiros
    ponteiro = (int *)malloc(8 * sizeof(int));
    if (ponteiro == NULL) {
        printf("Falha na alocação de memória para 8 inteiros.\n");
        return 1;
    }

    printf("Memória alocada para 8 inteiros.\n");

    // Realoque memória para armazenar doze inteiros
    ponteiro = (int *)realloc(ponteiro, 12 * sizeof(int));
    if (ponteiro == NULL) {
        printf("Falha na realocação de memória para 12 inteiros.\n");
        return 1;
    }

    printf("Memória realocada para 12 inteiros.\n");

    // Libere o espaço alocado
    free(ponteiro);

    printf("Memória liberada.\n");

    return 0;
}
