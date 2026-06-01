// extern_def.c
#include <stdio.h>

// 1. 实际定义一个全局变量（占内存空间）
int g_shared_var = 123;

// 2. 实际定义一个全局函数
void print_shared_var() {
    printf("【extern_def.c】 中的全局函数被调用，读取 g_shared_var: %d\n", g_shared_var);
}
