#include <stdio.h>

// ----------------------------------------------------
// 1. 宏函数定义的陷阱
// ----------------------------------------------------
// 陷阱 A：由于没有括号导致的优先级错误
#define BAD_SQUARE(x) x * x
#define GOOD_SQUARE(x) ((x) * (x))

// 陷阱 B：自增/自减等副作用导致的双重求值
#define BAD_MAX(a, b) ((a) > (b) ? (a) : (b))

// ----------------------------------------------------
// 2. 内联函数：完美解决上述所有问题
// ----------------------------------------------------
static inline int inline_max(int a, int b) {
    return (a > b) ? a : b;
}

static inline int inline_square(int x) {
    return x * x;
}

int main() {
    printf("=== 陷阱 1：运算符优先级测试 ===\n");
    // 预期结果：(2+3) * (2+3) = 25
    int val1 = BAD_SQUARE(2 + 3);  // 展开为: 2 + 3 * 2 + 3 = 2 + 6 + 3 = 11
    int val2 = GOOD_SQUARE(2 + 3); // 展开为: ((2 + 3) * (2 + 3)) = 25
    int val3 = inline_square(2 + 3); // 函数参数先求值：5，再计算 5 * 5 = 25

    printf("BAD_SQUARE(2 + 3)    = %d (⚠️ 错误！)\n", val1);
    printf("GOOD_SQUARE(2 + 3)   = %d (✅ 修复，但宏写起来极度繁琐)\n", val2);
    printf("inline_square(2 + 3) = %d (✅ 完美且简洁)\n\n", val3);

    printf("=== 陷阱 2：参数副作用（双重求值）测试 ===\n");
    int x = 5;
    int y = 3;
    // 预期：比较 5 和 3，最大值是 5，之后 x 应该自增一次变成 6
    // 实际上 BAD_MAX(x++, y) 会被替换为：((x++) > (y) ? (x++) : (y))
    // 因为 x++ (5) > y (3) 为真，所以执行后面的 x++
    // 结果导致 x 自增了两次！变成 7！
    int max_val1 = BAD_MAX(x++, y);
    printf("使用宏函数 BAD_MAX:\n");
    printf("  返回最大值: %d (⚠️ 预期是 5，结果返回了 6，因为第二次求值时 x 已经是 6 了)\n", max_val1);
    printf("  此时 x 的值: %d (⚠️ 预期是 6，结果变成了 7！x 被多加了一次)\n\n", x);

    // 重置变量测试内联函数
    x = 5;
    y = 3;
    // 内联函数是真正的函数，参数 x++ 传入前会先求值，仅求值一次（传入 5），然后 x 变为 6
    int max_val2 = inline_max(x++, y);
    printf("使用内联函数 inline_max:\n");
    printf("  返回最大值: %d (✅ 符合预期的 5)\n", max_val2);
    printf("  此时 x 的值: %d (✅ 符合预期的 6)\n", x);

    return 0;
}
