#include <stdio.h>
#include <stdlib.h>
#include <malloc.h> // alloca 相关的头文件

void stack_vs_heap_comparison() {
    // ----------------------------------------------------
    // 1. 栈分配：静态分配（普通局部变量）
    // ----------------------------------------------------
    int stack_var = 10;
    
    // ----------------------------------------------------
    // 2. 栈分配：动态分配（使用 alloca 函数在栈上动态开辟空间）
    //    特点：随着函数退出，系统会自动释放这部分栈空间，无需程序员 free。
    // ----------------------------------------------------
    int *stack_dyn_arr = (int *)alloca(5 * sizeof(int));
    if (stack_dyn_arr != NULL) {
        for (int i = 0; i < 5; i++) {
            stack_dyn_arr[i] = i * 10;
        }
    }

    // ----------------------------------------------------
    // 3. 堆分配：动态分配（使用 malloc 申请堆空间）
    //    特点：必须手动调用 free 释放，否则会造成内存泄漏。
    // ----------------------------------------------------
    int *heap_arr = (int *)malloc(5 * sizeof(int));
    if (heap_arr != NULL) {
        for (int i = 0; i < 5; i++) {
            heap_arr[i] = i * 100;
        }
    }

    printf("=== 栈与堆物理地址实测 ===\n");
    // 栈区的地址普遍非常高（例如 0x000000FFFFxxxxxx）
    printf("【栈区变量】 stack_var 地址:        %p\n", (void *)&stack_var);
    printf("【栈区动态】 stack_dyn_arr 指向:    %p\n", (void *)stack_dyn_arr);
    
    // 堆区的地址普遍要低得多（例如 0x0000020Dxxxxxx）
    if (heap_arr != NULL) {
        printf("【堆区动态】 heap_arr 指向:         %p\n", (void *)heap_arr);
    }

    // 观察生长方向（分配第二个局部变量）
    int stack_var2 = 20;
    printf("\n=== 观察栈的向下生长 ===\n");
    printf("第一个局部变量地址: %p\n", (void *)&stack_var);
    printf("第二个局部变量地址: %p\n", (void *)&stack_var2);
    if (&stack_var2 < &stack_var) {
        printf(" -> 后定义的变量地址更小，验证了：栈是【向下生长】的！\n\n");
    }

    // 观察堆的向上生长
    int *heap_arr2 = (int *)malloc(5 * sizeof(int));
    if (heap_arr != NULL && heap_arr2 != NULL) {
        printf("=== 观察堆的向上生长 ===\n");
        printf("第一次堆申请指向地址: %p\n", (void *)heap_arr);
        printf("第二次堆申请指向地址: %p\n", (void *)heap_arr2);
        if (heap_arr2 > heap_arr) {
            printf(" -> 后申请的堆内存地址更大，验证了：堆是【向上生长】的！\n\n");
        }
    }

    // 释放堆内存
    free(heap_arr);
    free(heap_arr2);
    
    // 注意：stack_dyn_arr 是通过 alloca 分配在栈上的，绝对【不能】调用 free(stack_dyn_arr)，否则会发生灾难性崩溃！
}

int main() {
    stack_vs_heap_comparison();
    return 0;
}
