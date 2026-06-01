// segfault_demo.c
#include <stdio.h>
#include <stdlib.h>

// 演示 1：修改常量区只读数据（经典段错误触发场景）
void trigger_readonly_segfault() {
    printf("--- 触发只读内存段错误演示 ---\n");
    char *str = "Hello World"; // 存储在常量区（.rodata），只读
    str[0] = 'h';              // ❌ 试图修改只读内存，操作系统将立刻抛出段错误并终止程序！
}

// 演示 2：解引用空指针 / 野指针
void trigger_null_pointer_segfault() {
    printf("--- 触发空指针解引用段错误演示 ---\n");
    int *p = NULL;
    *p = 100;                  // ❌ 解引用虚拟地址 0，触发 MMU 硬件异常，系统终止程序！
}

// 演示 3：无限递归导致栈溢出段错误
void infinite_recursion(int depth) {
    char buffer[1024]; // 每次调用在栈上占用 1KB 空间
    buffer[0] = 'A';
    if (depth % 1000 == 0) {
        printf("当前递归深度: %d\n", depth);
    }
    infinite_recursion(depth + 1); // ❌ 无限递归，压干栈空间，触发栈溢出段错误！
}

int main(int argc, char *argv[]) {
    // 默认不运行任何崩溃，由参数控制，避免直接崩溃退出导致调试困难
    if (argc < 2) {
        printf("请提供参数以运行特定崩溃演示：\n");
        printf("  1 : 触发修改只读内存段错误\n");
        printf("  2 : 触发空指针解引用段错误\n");
        printf("  3 : 触发无限递归栈溢出段错误\n");
        return 0;
    }

    int choice = atoi(argv[1]);
    switch (choice) {
        case 1:
            trigger_readonly_segfault();
            break;
        case 2:
            trigger_null_pointer_segfault();
            break;
        case 3:
            infinite_recursion(1);
            break;
        default:
            printf("无效的参数！\n");
            break;
    }
    return 0;
}
