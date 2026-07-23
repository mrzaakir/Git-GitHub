#include <cstdio>
#include <cstdlib>

int main() {
    std::printf("Simple C Project: Cycle Analyzer\n");
    std::printf("Enter the number of elements in a cycle: ");

    int n;
    if (std::scanf("%d", &n) != 1 || n <= 0) {
        std::fprintf(stderr, "Invalid number of elements.\n");
        return 1;
    }

    int *cycle = (int*)std::malloc(sizeof(int) * n);
    if (!cycle) {
        std::fprintf(stderr, "Memory allocation failed.\n");
        return 1;
    }

    std::printf("Enter %d values separated by spaces:\n", n);
    for (int i = 0; i < n; ++i) {
        if (std::scanf("%d", &cycle[i]) != 1) {
            std::fprintf(stderr, "Failed to read value.\n");
            std::free(cycle);
            return 1;
        }
    }

    long long sum = 0;
    for (int i = 0; i < n; ++i) sum += cycle[i];

    double average = (double)sum / n;

    std::printf("Cycle values: ");
    for (int i = 0; i < n; ++i) std::printf("%d ", cycle[i]);
    std::printf("\nSum: %lld\nAverage: %.2f\n", sum, average);

    std::printf("Enter a value to search in the cycle: ");
    int target;
    if (std::scanf("%d", &target) != 1) {
        std::fprintf(stderr, "Invalid input.\n");
        std::free(cycle);
        return 1;
    }

    int found = 0;
    for (int i = 0; i < n; ++i) {
        if (cycle[i] == target) {
            std::printf("Value %d found at position %d.\n", target, i + 1);
            found = 1;
            break;
        }
    }
    if (!found) std::printf("Value %d not found in the cycle.\n", target);

    std::free(cycle);
    return 0;
}
