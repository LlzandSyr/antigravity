# STM32 F407 ADC 初始化与主程序行级走读（Code Walkthrough）

本走读文档将对 `main.c` 中的 `adc_init()` 函数与 `main()` 主函数进行逐行深度拆解，帮助您彻底理解每一行代码的硬件意义。

---

## 一、 `adc_init(void)` 逐行硬件级详解

```c
void adc_init(void)
{
```
* **第 193 行**：定义 ADC 初始化函数入口。

```c
	//使能端口A的硬件时钟
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA,ENABLE);
```
* **第 195 行**：调用 **`RCC（Reset and Clock Control，复位与时钟控制）`** 库函数，开启 **`GPIOA（General Purpose Input Output Port A，通用输入输出端口A）`** 端口在 **`AHB1（Advanced High-performance Bus 1，高级高性能总线1）`** 高速总线上的硬件时钟。
* **硬件意义**：因为我们使用的是 `PA5` 引脚作为模拟信号输入端，如果不开启它对应的端口时钟，整个端口将无法工作。

```c
	//使能ADC1的硬件时钟
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_ADC1,ENABLE);		
```
* **第 199 行**：开启 **`ADC1（Analog-to-Digital Converter 1，模数转换器1）`** 外设在 **`APB2（Advanced Peripheral Bus 2，高级外设总线2）`** 总线上的硬件时钟。
* **硬件意义**：开启 ADC1 模块的电源与时钟，使其能够上电并准备进行模拟转换工作。

```c
	//配置PA5引脚为模拟信号模式
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_5;
```
* **第 202 行**：指定我们将要配置的引脚是第 5 号引脚（即 `PA5`）。

```c
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_AN;
```
* **第 203 行**：将该引脚配置为 **`AN（Analog Mode，模拟输入模式）`**。
* **硬件意义**：**极度关键！** 模拟模式下，引脚内部的施密特触发器（数字输入通道）和输出驱动器会被彻底切断。此时，外界极其微弱的物理电压能直接无损地接入到内部的 ADC 测量核心，防止数字电路的电磁噪声干扰模拟电压！

```c
//	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
//	GPIO_InitStructure.GPIO_OType=GPIO_OType_PP;
//	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;	
```
* **第 204 ~ 206 行**：被注释掉的代码。在 **`AN（Analog Mode，模拟输入模式）`** 下，引脚的速度、推挽开漏特性、上下拉电阻都会由硬件自动断开，因此无需在结构体中配置这些数字参数。

```c
	GPIO_Init(GPIOA,&GPIO_InitStructure);
```
* **第 207 行**：将以上结构体中的参数写入到 **`GPIOA（General Purpose Input Output Port A，通用输入输出端口A）`** 的配置寄存器中，使 `PA5` 物理切换为模拟输入状态。

```c
	//配置ADC（ADC1~ADC3）通用参数
	ADC_CommonInitStructure.ADC_Mode = ADC_Mode_Independent; 	//1个ADC工作
```
* **第 210 行**：设置所有 ADC 模块的通用工作模式为 **`Independent Mode（独立模式）`**。
* **硬件意义**：STM32 内部有 3 个 ADC 测量模块。当前配置为独立工作模式，意味着 **`ADC1（Analog-to-Digital Converter 1，模数转换器1）`** 独自进行电压测量，不与 ADC2 或 ADC3 发生任何协同动作（如双重/三重交替工作）。

```c
	ADC_CommonInitStructure.ADC_Prescaler = ADC_Prescaler_Div8;	//ADC硬件时钟频率=84MHz/8=10.5MHz
```
* **第 211 行**：为整个 ADC 外设设置时钟分频器，这里选择 **`8分频（Prescaler Div8，8分频）`**。
* **硬件意义**：ADC1 挂载在 APB2 总线上（主频通常为 84MHz）。因为 ADC 内部电容充电有物理速度上限，时钟频率不能太高（通常要求在 30MHz 或 36MHz 以下）。这里对其进行 8 分频，将工作时钟降为 `84 MHz / 8 = 10.5 MHz`，保证测量结果百分之百准确稳定。

```c
	ADC_CommonInitStructure.ADC_DMAAccessMode = ADC_DMAAccessMode_Disabled;//不使用DMA
```
* **第 212 行**：关闭多 ADC 联合测量下的 **`DMA（Direct Memory Access，直接存储器访问）`** 通道。因为我们仅使用独立模式，无须联合数据传输。

```c
	ADC_CommonInitStructure.ADC_TwoSamplingDelay = ADC_TwoSamplingDelay_5Cycles;//多个ADC工作才能用得上
```
* **第 213 行**：设置两次采样之间的延迟为 5 个时钟周期。由于我们是独立工作，该参数仅用于规范初始化，实际不起任何干扰作用。

```c
	ADC_CommonInit(&ADC_CommonInitStructure);
```
* **第 214 行**：将上述通用配置参数写入底层的通用控制寄存器中。

```c
	//单独配置ADC1
	ADC_InitStructure.ADC_Resolution = ADC_Resolution_12b;	//输出结果为12bit的分辨率
```
* **第 218 行**：配置测量分辨率为 **`12位（12-bit Resolution，12位分辨率）`**。
* **硬件意义**：使 ADC 内部天平的刻度分为 `2^12 = 4096` 等份。代表输入电压将被转化为 `0`（代表 0V）到 `4095`（代表 3.3V）之间的数字。

```c
	ADC_InitStructure.ADC_ScanConvMode = DISABLE;//DISABLE,只扫描（转换）一个通道；ENABLE，扫描多个通道
```
* **第 219 行**：关闭 **`Scan Mode（扫描模式）`**。
* **硬件意义**：由于我们目前只测量 `PA5` 对应的一个通道，因此关闭顺序扫描，只专注转换这一个通道。

```c
	ADC_InitStructure.ADC_ContinuousConvMode = ENABLE;//ENABLE，ADC会一直连续工作转化；DISABLE，只转换一次。
```
* **第 220 行**：开启 **`Continuous Conversion Mode（连续转换模式）`**。
* **硬件意义**：**极其省心！** 开启后，单片机只需要在开机时下达一次“开始”指令，ADC1 就会在硬件后台一刻不停地循环测量，源源不断地更新寄存器中的值。程序需要时随时读取即可，无需每次都手动触发。

```c
	ADC_InitStructure.ADC_ExternalTrigConvEdge = ADC_ExternalTrigConvEdge_None;
```
* **第 221 行**：关闭任何外部硬件引脚或定时器的触发源。
* **硬件意义**：完全使用软件指令（即后面在 `main` 函数里执行的代码触发）来启动第一次测量。

```c
	//ADC_InitStructure.ADC_ExternalTrigConv = ADC_ExternalTrigConv_T1_CC1;//该代码是不会生效
```
* **第 222 行**：被注释掉的代码。因为上面一行配置了不使用任何硬件触发，所以此处配置具体的触发源不会起作用。

```c
	ADC_InitStructure.ADC_DataAlign = ADC_DataAlign_Right;//右对齐存储
```
* **第 223 行**：将数据对齐格式配置为 **`Right Alignment（右对齐）`**。
* **硬件意义**：将 12 位的测量结果放在 16 位盒子的最右边（低 12 位，高 4 位用 0 填充）。数值直接映射为正常的 `0` 到 `4095`，极度方便软件层直接读取并套用公式计算。

```c
	ADC_InitStructure.ADC_NbrOfConversion = 1;//当前转换通道数量为1
```
* **第 224 行**：指定当前规则转换序列中的通道数量为 1 个。

```c
	ADC_Init(ADC1, &ADC_InitStructure);
```
* **第 225 行**：把上述个性化参数写入到 **`ADC1（Analog-to-Digital Converter 1，模数转换器1）`** 对应的控制寄存器中。

```c
	//指定ADC1对通道5进行转换，转换排序为1，采样点时间为3个ADC硬件时钟（采样时间越长，数据越准确）
	ADC_RegularChannelConfig(ADC1, ADC_Channel_5, 1, ADC_SampleTime_3Cycles);
```
* **第 228 行**：设定具体的通道采配参数：
  * 对 `ADC1` 的 **`Channel 5（通道5，对应 PA5 引脚）`** 进行转换；
  * 该通道在轮流采样的队伍中排第 `1` 位；
  * 采样的开合时间选择 **`3个ADC周期（3 Cycles，3个周期）`**（电容充电 3 个周期，虽然充电时间极短，但转换速度最快。如果需要测高阻抗传感器，可以适当调长该参数以提高准确度）。

```c
	//使使能ADC1工作
	ADC_Cmd(ADC1, ENABLE);
}
```
* **第 232 ~ 234 行**：使能并真正开启 ADC1 的物理测量电路。至此，整个 ADC 的硬件电路部分完全就绪！

---

## 二、 `main(void)` 执行流程与应用层计算走读

```c
int main(void)
{
	uint16_t adc_value,adc_voltage;
```
* **第 237 ~ 239 行**：主函数入口。在 **`RAM（Random Access Memory，随机存取存储器）`** 中声明两个变量：`adc_value` 用于存放原始数字，`adc_voltage` 用于存放计算出的毫伏级电压。

```c
	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	usart1_init(115200);
	led_init();
	adc_init();
```
* **第 241 ~ 244 行**：常规外设的初始化。把中断优先级分组设为组 2，配置调试串口的波特率为 115200，初始化板载发光二极管，并调用我们的 `adc_init()`。

```c
	ADC_SoftwareStartConv(ADC1);
```
* **第 245 行**：调用软件触发指令，启动 **`ADC1（Analog-to-Digital Converter 1，模数转换器1）`** 进行第一次转换。
* **硬件意义**：**只用执行一次！** 因为我们在上面配置了“连续转换模式”，这次软件点火之后，硬件就会在后台无限循环测量，从此再也不需要这句代码。

```c
	printf("This is adc test\r\n");
```
* **第 247 行**：串口打印测试启动提示语。

```c
	while(1)
	{
		adc_value = ADC_GetConversionValue(ADC1);//转换结果值的范围为0~4095
```
* **第 250 ~ 252 行**：进入无限主循环。
* **第 252 行**：直接调用 `ADC_GetConversionValue(ADC1)` 读出 ADC1 内部数据寄存器当前的数值并存入 `adc_value`。这个值必定是 `0`（代表 0V）到 `4095`（代表 3.3V）之间的数字。

```c
		adc_voltage = adc_value *3300/4095;
```
* **第 253 行**：**应用开发中最核心的换算公式！**
  * 我们要把 `0 ~ 4095` 的比例值换算为实际毫伏数（`0 ~ 3300` 毫伏）。
  * 换算关系为：`电压 / 3300毫伏 = 测量值 / 4095`。
  * 变形后即得：`电压 = 测量值 * 3300 / 4095`。
  * **应用层技巧**：之所以不写成 `adc_value * 3.3 / 4095` 浮点数，是为了**避免使用浮点数导致单片机内核计算变慢**。乘以 `3300` 直接得出整数级的**毫伏（mv）**数，既保证了微伏级的超高精度，又保持了极快的纯整数运算速度！

```c
		printf("adc_value:%d adc_voltage:%dmv\r\n",adc_value,adc_voltage);
		delay_ms(1000);
	}
}
```
* **第 254 ~ 257 行**：在控制台上打印出原始 ADC 数值和毫伏电压值，然后延时 1 秒，不断循环。
