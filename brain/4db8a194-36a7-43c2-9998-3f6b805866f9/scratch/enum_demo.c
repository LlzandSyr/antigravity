#include <stdio.h>

// ----------------------------------------------------
// 1. 传统枚举定义：容易发生命名冲突
// ----------------------------------------------------
typedef enum {
    COLOR_RED,
    COLOR_GREEN,
    COLOR_BLUE
} Color;

// ----------------------------------------------------
// 2. 位掩码 (Bitmask) 枚举的应用
// ----------------------------------------------------
typedef enum {
    PERMISSION_NONE    = 0,
    PERMISSION_READ    = 1 << 0, // 1 (二进制 0001)
    PERMISSION_WRITE   = 1 << 1, // 2 (二进制 0010)
    PERMISSION_EXECUTE = 1 << 2  // 4 (二进制 0100)
} Permission;

// ----------------------------------------------------
// 3. 【超级加分项】X-Macro 自动同步维护枚举与字符串数组
// ----------------------------------------------------
#define DEVICE_STATE_LIST(X) \
    X(STATE_POWER_OFF)       \
    X(STATE_BOOTING)         \
    X(STATE_RUNNING)         \
    X(STATE_FAULT)

// 使用 X-Macro 自动展开生成枚举定义：
// STATE_POWER_OFF, STATE_BOOTING, STATE_RUNNING, STATE_FAULT
#define GENERATE_ENUM(ENUM) ENUM,
typedef enum {
    DEVICE_STATE_LIST(GENERATE_ENUM)
} DeviceState;
#undef GENERATE_ENUM

// 使用 X-Macro 自动展开生成与之同步的字符串数组
#define GENERATE_STRING(STRING) #STRING,
const char* DeviceStateString[] = {
    DEVICE_STATE_LIST(GENERATE_STRING)
};
#undef GENERATE_STRING

int main() {
    printf("=== 1. 基础枚举与位掩码测试 ===\n");
    Color my_color = COLOR_GREEN;
    printf("当前颜色数值 (COLOR_GREEN): %d\n\n", my_color);

    // 位掩码组合
    int user_perm = PERMISSION_READ | PERMISSION_WRITE;
    printf("用户权限值: %d\n", user_perm);
    if (user_perm & PERMISSION_READ) {
        printf(" -> 具有【读】权限\n");
    }
    if (user_perm & PERMISSION_WRITE) {
        printf(" -> 具有【写】权限\n");
    }
    if (!(user_perm & PERMISSION_EXECUTE)) {
        printf(" -> 没有【执行】权限\n");
    }
    printf("\n");

    printf("=== 2. X-Macro 自动反射打印测试 ===\n");
    // 假设设备当前进入了 RUNNING 状态
    DeviceState current_state = STATE_RUNNING;
    
    // 打印它的整数值，并同时打印其优雅的文本名字！
    printf("当前设备状态码: %d\n", current_state);
    printf("当前设备状态名: %s\n", DeviceStateString[current_state]);
    
    return 0;
}
