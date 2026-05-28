# STM32F4 RTC 与中断配置代码行级深度剖析 (Code Walkthrough)

本篇文档将为您进行**行级（Line-by-Line）**的深度拆解。我们跳过通用的 C 语言基础语法，直奔主题：**每一行 STM32 库函数在硬件和寄存器层面上，到底起到了什么关键作用。**

---

## 一、 全局配置结构体

在函数外部，我们定义了三个库函数的核心结构体：

```c
RTC_InitTypeDef  RTC_InitStructure;   // 用于配置 RTC 的时钟分频系数、小时格式（12h/24h）
RTC_DateTypeDef  RTC_DateStructure;   // 用于装载和读写“年、月、日、星期”日历信息
RTC_TimeTypeDef  RTC_TimeStructure;   // 用于装载和读写“时、分、秒、上午/下午”时间信息
```

---

## 二、 rtc_init() 初始化函数：逐行功能详析

`rtc_init()` 负责打通从“电源解锁”到“时钟分频”，再到“1秒唤醒中断输出”的整个硬件链路。

### 1. 开启电源时钟与解除备份域保护
```c
RCC_APB1PeriphClockCmd(RCC_APB1Periph_PWR, ENABLE);
```
* **硬件作用**：使能 **PWR（电源控制器）** 的外设时钟。
* **为什么要写**：RTC 寄存器属于备份域（Backup Domain）。在 STM32 中，备份域的控制开关归 PWR 模块管理，必须先给 PWR 供电才能操作写保护。

```c
PWR_BackupAccessCmd(ENABLE);
```
* **硬件作用**：解除备份域寄存器的**写保护**限制。
* **为什么要写**：防止程序跑飞时意外修改 RTC 时间，硬件默认禁止写入。此行代码相当于“拉开安全锁”，允许 CPU 向 RTC 寄存器写入数据。

---

### 2. 时钟源配置（启动 LSI 内部低速时钟）
```c
RCC_LSICmd(ENABLE);
```
* **硬件作用**：开启芯片内部的**低速振荡器 LSI**。
* **为什么要写**：作为 RTC 走时的“心脏跳动源”。（若使用外部 LSE 晶振，此处则配置为 `RCC_LSEConfig(RCC_LSE_ON)`）。

```c
while(RCC_GetFlagStatus(RCC_FLAG_LSIRDY) == RESET);
```
* **硬件作用**：循环等待，直到 LSI 时钟标志位变为 Ready（稳定起振状态）。
* **为什么要写**：时钟源刚开启时频率不稳定，如果不加这行等待，后面的硬件初始化可能会因为没有稳定的心跳脉冲而失败。

```c
RCC_RTCCLKConfig(RCC_RTCCLKSource_LSI);
```
* **硬件作用**：将稳定运行的 LSI 时钟，选择并连接为 RTC 模块的输入时钟源。

```c
RCC_RTCCLKCmd(ENABLE);
```
* **硬件作用**：正式使能（开启）RTC 模块的全局工作时钟。

```c
RTC_WaitForSynchro();
```
* **硬件作用**：等待 RTC 的 APB 寄存器与 RTC 核心时钟完成**读取同步**。
* **为什么要写**：CPU 的运行主频极高（168MHz），而 RTC 的时钟频率极低（32kHz）。如果不等待同步直接去读写寄存器，CPU 会读到未更新完毕的“脏数据”导致时钟紊乱。

---

### 3. 时钟分频配置（将 32000Hz 转换为标准 1Hz 走时）
```c
RTC_InitStructure.RTC_AsynchPrediv = 0x7F; // 异步分频系数，写入 127
```
* **硬件作用**：将输入时钟（LSI = 32000Hz）先进行一次 **128 分频**（计算公式：`0x7F + 1 = 128`）。此时时钟频率降为：`32000 / 128 = 250Hz`。

```c
RTC_InitStructure.RTC_SynchPrediv = 0xF9;  // 同步分频系数，写入 249
```
* **硬件作用**：将上述 250Hz 时钟再进行一次 **250 分频**（计算公式：`0xF9 + 1 = 250`）。此时频率降为：`250 / 250 = 1Hz`（即标准的 1 秒 1 次脉冲）。

```c
RTC_InitStructure.RTC_HourFormat = RTC_HourFormat_24;
```
* **硬件作用**：设置 RTC 内部的计数模式为 **24 小时格式**。

```c
RTC_Init(&RTC_InitStructure);
```
* **硬件作用**：将上述分频和小时格式配置参数一次性写入到 RTC 核心控制寄存器中。

---

### 4. 设置出厂默认时间与日期
```c
RTC_DateStructure.RTC_Year = 0x17;                     // 年份：17年
RTC_DateStructure.RTC_Month = RTC_Month_November;      // 月份：11月
RTC_DateStructure.RTC_Date = 0x29;                     // 日期：29号
RTC_DateStructure.RTC_WeekDay = RTC_Weekday_Wednesday; // 星期：星期三
RTC_SetDate(RTC_Format_BCD, &RTC_DateStructure);       // 写入日期寄存器
```
* **为什么要写 0x 前缀**：STM32 内部使用的是 **BCD 码格式**（即十六进制代表十进制）。写入 `0x17` 代表 17 年，如果误写成十进制的 `17`，硬件会将其错误翻译为 11 年。

```c
RTC_TimeStructure.RTC_H12     = RTC_H12_PM;
RTC_TimeStructure.RTC_Hours   = 0x14;                  // 小时：14点（下午2点）
RTC_TimeStructure.RTC_Minutes = 0x56;                  // 分钟：56分
RTC_TimeStructure.RTC_Seconds = 0x55;                  // 秒钟：55秒
RTC_SetTime(RTC_Format_BCD, &RTC_TimeStructure);       // 写入时间寄存器
```
* **硬件作用**：将出厂默认的小时、分钟、秒钟初始值写入到时间计数器中，作为走时起点。

---

### 5. 自动唤醒定时器（WUT）中断配置
```c
RTC_WakeUpCmd(DISABLE);
```
* **硬件作用**：暂时**关闭**自动唤醒功能。
* **为什么要写**：RTC 硬件规定，在修改唤醒频率、重装载值之前，必须先关闭该功能，否则配置寄存器会处于锁死状态。

```c
RTC_WakeUpClockConfig(RTC_WakeUpClock_CK_SPRE_16bits);
```
* **硬件作用**：选择我们前面分频出来的标准 1Hz 信号（`CK_SPRE`）作为唤醒定时器的计数时钟源。

```c
RTC_SetWakeUpCounter(1-1);
```
* **硬件作用**：设置自动重装载计数值为 `0`（硬件会自动加 1，即 `0 + 1 = 1`）。
* **为什么要写**：配合上面的 1Hz 时钟源，意味着**唤醒计数器每隔 1 秒就会向下溢出并产生一次唤醒警报**。

```c
RTC_ClearITPendingBit(RTC_IT_WUT);
```
* **硬件作用**：清除 RTC 内部可能残留的自动唤醒中断挂起标志位，防止一开机就误触发中断。

```c
RTC_ITConfig(RTC_IT_WUT, ENABLE);
```
* **硬件作用**：使能（开启）RTC 自动唤醒功能向外发送中断信号的物理通道。

```c
RTC_WakeUpCmd(ENABLE);
```
* **硬件作用**：配置完毕，重新开启自动唤醒计数器，使其开始每秒倒计时。

---

### 6. EXTI 22 号中断线配置（紧急信号接线板）
```c
EXTI_InitStructure.EXTI_Line = EXTI_Line22;
```
* **硬件作用**：指定我们当前配置的是 **22 号外部中断线**。
* **为什么要写**：在 STM32 硬件设计中，RTC 的唤醒事件在芯片内部是强行连接在第 22 号外部中断线上。

```c
EXTI_InitStructure.EXTI_Mode = EXTI_Mode_Interrupt;
```
* **硬件作用**：设置 EXTI 工作在**中断触发模式**（产生 CPU 中断，而不是产生硬件事件）。

```c
EXTI_InitStructure.EXTI_Trigger = EXTI_Trigger_Rising;
```
* **硬件作用**：设置触发源为**上升沿触发**（即当 RTC 唤醒警报电平由低变高的瞬间拉响警报）。

```c
EXTI_InitStructure.EXTI_LineCmd = ENABLE;
```
* **硬件作用**：使能并开启 EXTI 22 号线的物理传输功能。

```c
EXTI_Init(&EXTI_InitStructure);
```
* **硬件作用**：将上述参数写入 EXTI 控制寄存器中生效。

---

### 7. NVIC 配置（贴身秘书接听控制）
```c
NVIC_InitStructure.NVIC_IRQChannel = RTC_WKUP_IRQn;
```
* **硬件作用**：指定当前需要配置的中断通道为 **`RTC_WKUP_IRQn`（RTC 唤醒通道）**。

```c
NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0x03;
NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0x03;
```
* **硬件作用**：设置中断的抢占优先级为 3，响应优先级为 3。

```c
NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
```
* **硬件作用**：在 NVIC 中开启对该中断通道的监听，允许其打断 CPU 的主程序运行。

```c
NVIC_Init(&NVIC_InitStructure);
```
* **硬件作用**：将 NVIC 参数写入系统控制寄存器中生效。

---

## ⚡ 三、 RTC_WKUP_IRQHandler() 中断服务程序

每当 1 秒钟唤醒时间到，CPU 就会被强行打断，进入本函数：

```c
void RTC_WKUP_IRQHandler(void)
{
	// 1. 软件读取状态：确认是不是真的因为 RTC 的自动唤醒事件（WUT）触发的这次中断
	if(RTC_GetITStatus(RTC_IT_WUT) != RESET)
	{
		printf("RTC_WKUP_IRQHandler\r\n");
        
		// 2. 清除 RTC 内部的自动唤醒中断挂起位
		RTC_ClearITPendingBit(RTC_IT_WUT);
        
		// 3. 清除 EXTI 外部中断控制器 22 号线上的中断挂起位
		EXTI_ClearITPendingBit(EXTI_Line22);
	} 
}
```
* **⚠️ 为什么第 2、3 步清挂起位（ClearPendingBit）是死命令？**
  当中断发生时，硬件会将对应寄存器的标志位置 1（挂起）。**CPU 只有检测到这些标志位被清零（置 0）后，才会认为这次中断已经处理完毕。**
  如果不清除，CPU 一退出中断函数，又会瞬间检测到标志位为 1，从而无休止地重新进入中断，导致整个单片机彻底卡死。

---

## ⏱️ 四、 主循环读取时间与日期（while 循环内）

```c
RTC_GetTime(RTC_Format_BCD, &RTC_TimeStructure);
```
* **硬件作用**：首先获取 RTC 的 **Time 影子寄存器** 的数值。
* **💡 先时间、后日期规则**：STM32 硬件规定，当读取 Time 寄存器时，Date 寄存器的值会被锁定；当读取 Date 寄存器后，锁才解除。这样可以避免在深夜 23:59:59 读取时由于跨天导致时间日期对不上的问题。因此**必须先读 Time，再读 Date**。

```c
RTC_GetDate(RTC_Format_BCD, &RTC_DateStructure);
```
* **硬件作用**：随后获取 RTC 的 **Date 影子寄存器** 的数值，并自动解除寄存器锁。
