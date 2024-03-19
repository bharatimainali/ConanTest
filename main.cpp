
#include <spdlog/spdlog.h>

#include <iostream>

int main(){
    spdlog::info("spdlog test");

    std::cout << "test" << std::endl;
    return 0;
}