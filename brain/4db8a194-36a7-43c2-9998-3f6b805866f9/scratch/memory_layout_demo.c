#include <stdio.h>
#include <stdlib.h>

// 1. 全局变量，已初始化且不为0 -> 存储在 .data 段
int g_init_var = 100;

// 2. 全局变量，未初始化 -> 存储在 .bss 段 (会被自动初始化为 0)
int g_uninit_var;

// 3. 全局常量 -> 存储在 .rodata 段 (文字常量区/只读数据区)
const int g_const_var = 999;

void demo_function(int arg_var) {
    // 4. 局部变量 -> 存储在栈区 (Stack)
    int local_var = 10;
    
    // 5. 局部静态变量，已初始化 -> 存储在 .data 段
    static int static_init_var = 200;
    
    // 6. 局部静态变量，未初始化 -> 存储在 .bss 段
    static int static_uninit_var;

    // 7. 局部只读变量 -> 存在栈区（但在编译期会做常量优化）
    const int local_const = 30;

    // 8. 字符串字面量 -> 指针 p 存在栈上，但指向的字面量 "Hello World" 存在 .rodata 段
    char *str_literal = "Hello World";

    // 9. 动态内存分配 -> 指针 heap_ptr 存在栈上，指向的内存存在堆区 (Heap)
    int *heap_ptr = (int *)malloc(sizeof(int));
    if (heap_ptr != NULL) {
        *heap_ptr = 888;
    }

    printf("=== 内存地址分布实测 (从低地址到高地址) ===\n");
    
    // 代码段
    printf("【代码段 .text】   函数地址 demo_function:   %p\n", (void *)demo_function);
    
    // 只读常量区
    printf("【只读常量区 .rodata】 全局常量 g_const_var:  %p\n", (void *)&g_const_var);
    printf("【只读常量区 .rodata】 字符串字面量地址:      %p\n", (void *)str_literal);
    
    // 全局静态区 (.data段)
    printf("【已初始化数据 .data】 全局变量 g_init_var:  %p\n", (void *)&g_init_var);
    printf("【已初始化数据 .data】 静态变量 static_init_var: %p\n", (void *)&static_init_var);
    
    // 全局静态区 (.bss段)
    printf("【未初始化数据 .bss】  全局变量 g_uninit_var: %p\n", (void *)&g_uninit_var);
    printf("【未初始化数据 .bss】  静态变量 static_uninit_var: %p\n", (void *)&static_uninit_var);
    
    // 堆区
    if (heap_ptr != NULL) {
        printf("【堆区 Heap】         动态分配 heap_ptr 指向: %p\n", (void *)heap_ptr);
    }
    
    // 栈区
    printf("【栈区 Stack】        函数形参 arg_var:         %p\n", (void *)&arg_var);
    printf("【栈区 Stack】        局部变量 local_var:       %p\n", (void *)&local_var);
    printf("【栈区 Stack】        局部只读 local_const:     %p\n", (void *)&local_const);
    printf("【栈区 Stack】        指针变量 heap_ptr 本身:    %p\n", (void *)&heap_ptr);

    // 释放堆内存
    free(heap_ptr);
}

int main() {
    demo_function(5);
    return 0;
}
