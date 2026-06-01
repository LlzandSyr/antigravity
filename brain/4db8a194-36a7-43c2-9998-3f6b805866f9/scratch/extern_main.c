// extern_main.c
#include <stdio.h>

// ====================================================
// 1. 使用 extern 声明在别的文件中定义的全局变量与函数
//    注意：声明不分配内存空间，它仅仅是向编译器许下承诺：
//    “请先编译通过，这个变量在别的模块里，链接器最后会帮你找到它的！”
// ====================================================
extern int g_shared_var;
extern void print_shared_var();

// ====================================================
// 2. 指针常量与常量指针的演示函数
// ====================================================
void pointer_const_vs_const_pointer_demo() {
    int a = 10;
    int b = 20;

    printf("\n=== 2. 指针常量与常量指针测试 ===\n");

    // 🟢 A. 常量指针（Pointer to Constant）：const 在 * 左边
    //    特点：指针指向的内容是常量的，不能通过该指针修改指向的值；但指针本身（指向哪个地址）可以被改变。
    const int *ptr_to_const = &a;
    // *ptr_to_const = 15; // ❌ 编译报错！无法修改指向的值
    ptr_to_const = &b;     // ✅ 编译通过！可以改变指针本身的指向
    printf("【常量指针】 指向的新值 (*ptr_to_const): %d\n", *ptr_to_const);

    // 🟢 B. 指针常量（Pointer Constant）：const 在 * 右边
    //    特点：指针本身是常量，一旦指向某个地址，就绝不能改变指向；但指向内容的值是可以修改的。
    int * const const_ptr = &a;
    *const_ptr = 15;       // ✅ 编译通过！可以修改指向的值
    // const_ptr = &b;     // ❌ 编译报错！无法改变指针本身的指向
    printf("【指针常量】 修改后的值 (a): %d\n", a);

    // 🟢 C. 指向常量的指针常量：* 左右两边都有 const
    //    特点：指针指向和指向内容全都是只读的。
    const int * const holy_ptr = &a;
    // *holy_ptr = 30;     // ❌ 编译报错！
    // holy_ptr = &b;      // ❌ 编译报错！
    printf("【双重只读】 值 (a): %d\n", *holy_ptr);
}

int main() {
    printf("=== 1. extern 多文件链接测试 ===\n");
    // 成功读取并修改在 extern_def.c 中定义的全局变量
    printf("【extern_main.c】 读取 g_shared_var: %d\n", g_shared_var);
    g_shared_var = 456;
    
    // 调用在 extern_def.c 中定义的函数
    print_shared_var();

    // 演示 const 指针
    pointer_const_vs_const_pointer_demo();

    return 0;
}
