// compilation_stages_demo.c
#include <stdio.h>

#define CONST_FACTOR 5

// 演示全局变量与 volatile 优化
volatile int g_flag = 1;

int main() {
    int local_var = 10;
    int result = local_var * CONST_FACTOR;
    
    // 假设此处等待外部中断修改 g_flag
    while (g_flag == 1) {
        // 执行一些空操作
    }
    
    return 0;
}
