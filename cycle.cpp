#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::cout << "Simple C++ Project: Cycle Analyzer\n";
    std::cout << "Enter the number of elements in a cycle: ";

    int n;
    if (!(std::cin >> n) || n <= 0) {
        std::cerr << "Invalid number of elements.\n";
        return 1;
    }

    std::vector<int> cycle(n);
    std::cout << "Enter " << n << " values separated by spaces:\n";
    for (int i = 0; i < n; ++i) {
        if (!(std::cin >> cycle[i])) {
            std::cerr << "Failed to read value.\n";
            return 1;
        }
    }

    long long sum = 0;
    for (int value : cycle) {
        sum += value;
    }

    double average = static_cast<double>(sum) / n;

    std::cout << "Cycle values: ";
    for (int value : cycle) {
        std::cout << value << ' ';
    }
    std::cout << "\nSum: " << sum << "\nAverage: " << average << "\n";

    std::cout << "Enter a value to search in the cycle: ";
    int target;
    if (!(std::cin >> target)) {
        std::cerr << "Invalid input.\n";
        return 1;
    }

    auto it = std::find(cycle.begin(), cycle.end(), target);
    if (it != cycle.end()) {
        std::cout << "Value " << target << " found at position " << (it - cycle.begin() + 1) << ".\n";
    } else {
        std::cout << "Value " << target << " not found in the cycle.\n";
    }

    return 0;
}
