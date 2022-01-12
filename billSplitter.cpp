#include <iostream>

int main()
{
    std::cout << "Enter total amount to be paid : ";

    double amnt{};
    std::cin >> amnt;

    std::cout << "Enter number of people : ";
    int numPpl{};
    std::cin >> numPpl;

    double totalPerPerson {amnt / numPpl};
    int rupeesPerPerson {static_cast<int>(totalPerPerson)};
    int paisePerPerson {static_cast<int>((totalPerPerson-rupeesPerPerson)*100)};

    std::cout << "Each person has to pay " << rupeesPerPerson << " rupees and " << paisePerPerson << " paise.\n";

    return 0;
}
