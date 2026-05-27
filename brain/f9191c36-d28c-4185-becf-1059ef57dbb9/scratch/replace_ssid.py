import sys

def fix_dht11_integration(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Let's completely rewrite the entire main.c file to be absolutely correct
        # No literal \r\n inside comments!
        # Explicit casts for usart_send_string
        # Remove unused variable rt in dht11_read
        
        final_code_str = """#include <stm32f4xx.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <stdlib.h>

// 位带操作映射宏定义用于DHT11 (GPIOG Pin 9)
#define PFout(n)	(*(volatile uint32_t *)(0x42000000 + (GPIOF_BASE + 0x14 - 0x40000000)*32 + n*4))
#define PGout(n)	(*(volatile uint32_t *)(0x42000000 + (GPIOG_BASE + 0x14 - 0x40000000)*32 + n*4))
#define PGin(n)		(*(volatile uint32_t *)(0x42000000 + (GPIOG_BASE + 0x10 - 0x40000000)*32 + n*4))
#define PEout(n)     (*(uint32_t *)(0x42000000+(GPIOE_BASE+0x14-0x40000000)*32+(n)*4))

GPIO_InitTypeDef			GPIO_InitStructure;
EXTI_InitTypeDef   			EXTI_InitStructure;
NVIC_InitTypeDef   		 	NVIC_InitStructure;
USART_InitTypeDef   		USART_InitStructure;

// 标准C库重定向
struct __FILE { int handle; };
FILE __stdout;
FILE __stdin;

int fputc(int ch, FILE *f) {
	while(USART_GetFlagStatus(USART1,USART_FLAG_TC)==RESET);
	USART_SendData(USART1,ch);	
	return ch;
}

void delay_ms(uint32_t t)
{
	while(t--)
	{
		SysTick->CTRL = 0; 
		SysTick->LOAD = 168000-1; 
		SysTick->VAL = 0; 
		SysTick->CTRL = 5; 
		while ((SysTick->CTRL & 0x10000)==0);
	}
	SysTick->CTRL = 0; 
}

void delay_us(uint32_t t)
{
	SysTick->CTRL = 0; 
	SysTick->LOAD = 168*t-1; 
	SysTick->VAL = 0; 
	SysTick->CTRL = 5; 
	while ((SysTick->CTRL & 0x10000)==0);
	SysTick->CTRL = 0; 	
}

void led_init(void)
{
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOF,ENABLE);
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOE,ENABLE);
	
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_9|GPIO_Pin_10;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOF,&GPIO_InitStructure);
	
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_13|GPIO_Pin_14;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOE,&GPIO_InitStructure);
	
	GPIO_WriteBit(GPIOF,GPIO_Pin_9, Bit_SET);
	GPIO_WriteBit(GPIOF,GPIO_Pin_10, Bit_SET);
	GPIO_WriteBit(GPIOE,GPIO_Pin_13, Bit_SET);
	GPIO_WriteBit(GPIOE,GPIO_Pin_14, Bit_SET);
}

void key_init(void)
{
	GPIO_InitTypeDef GPIO_KEY;
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA,ENABLE);
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOE,ENABLE);
	
	GPIO_KEY.GPIO_Pin=GPIO_Pin_0;
	GPIO_KEY.GPIO_Mode=GPIO_Mode_IN;
	GPIO_KEY.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOA,&GPIO_KEY);
	
	GPIO_KEY.GPIO_Pin=GPIO_Pin_2|GPIO_Pin_3|GPIO_Pin_4;
	GPIO_KEY.GPIO_Mode=GPIO_Mode_IN;
	GPIO_KEY.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOE,&GPIO_KEY);
}

void usart1_init(uint32_t baud)
{
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOA,ENABLE);
	RCC_APB2PeriphClockCmd(RCC_APB2Periph_USART1,ENABLE);
	
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_9|GPIO_Pin_10;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOA,&GPIO_InitStructure);	
	
	GPIO_PinAFConfig(GPIOA,GPIO_PinSource9,GPIO_AF_USART1);
	GPIO_PinAFConfig(GPIOA,GPIO_PinSource10,GPIO_AF_USART1);	
	
	USART_InitStructure.USART_BaudRate = baud; 					
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;	
	USART_InitStructure.USART_StopBits = USART_StopBits_1;		
	USART_InitStructure.USART_Parity = USART_Parity_No;			
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
	USART_Init(USART1, &USART_InitStructure);
	
	USART_ITConfig(USART1,USART_IT_RXNE,ENABLE);
	
	NVIC_InitStructure.NVIC_IRQChannel = USART1_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
	
	USART_Cmd(USART1, ENABLE);
}

void usart3_init(uint32_t baud)
{
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOB,ENABLE);
	RCC_APB1PeriphClockCmd(RCC_APB1Periph_USART3,ENABLE);
	
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_10|GPIO_Pin_11;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_AF;
	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_PP;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOB,&GPIO_InitStructure);	
	
	GPIO_PinAFConfig(GPIOB,GPIO_PinSource10,GPIO_AF_USART3);
	GPIO_PinAFConfig(GPIOB,GPIO_PinSource11,GPIO_AF_USART3);	
	
	USART_InitStructure.USART_BaudRate = baud; 					
	USART_InitStructure.USART_WordLength = USART_WordLength_8b;	
	USART_InitStructure.USART_StopBits = USART_StopBits_1;		
	USART_InitStructure.USART_Parity = USART_Parity_No;			
	USART_InitStructure.USART_HardwareFlowControl = USART_HardwareFlowControl_None;
	USART_InitStructure.USART_Mode = USART_Mode_Rx | USART_Mode_Tx;
	USART_Init(USART3, &USART_InitStructure);
	
	USART_ITConfig(USART3,USART_IT_RXNE,ENABLE);
	
	NVIC_InitStructure.NVIC_IRQChannel = USART3_IRQn;
	NVIC_InitStructure.NVIC_IRQChannelPreemptionPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelSubPriority = 0;
	NVIC_InitStructure.NVIC_IRQChannelCmd = ENABLE;
	NVIC_Init(&NVIC_InitStructure);
	
	USART_Cmd(USART3, ENABLE);
}

void usart_send_string(USART_TypeDef* USARTx,uint8_t *str)
{
	uint8_t *p=str;
	if(p==NULL) return;
	while(*p)
	{
		while(USART_GetFlagStatus(USARTx,USART_FLAG_TC)==RESET);
		USART_SendData(USARTx,*p);
		p++;
	}
}

// DHT11 驱动函数
void dht11_init(void)
{
	RCC_AHB1PeriphClockCmd(RCC_AHB1Periph_GPIOG,ENABLE);
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_OD;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOG,&GPIO_InitStructure);	
	PGout(9)=1;
}

int32_t dht11_read(uint8_t *buf)
{
	uint32_t t=0;
	int32_t i,j;
	uint8_t d=0;
	uint8_t *p=buf;
	uint16_t check_sum=0;
	
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_OUT;
	GPIO_InitStructure.GPIO_Speed=GPIO_Low_Speed;
	GPIO_InitStructure.GPIO_OType=GPIO_OType_OD;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOG,&GPIO_InitStructure);	
	
	PGout(9)=0;
	delay_ms(18);
	PGout(9)=1;
	delay_us(30);
	
	GPIO_InitStructure.GPIO_Pin=GPIO_Pin_9;
	GPIO_InitStructure.GPIO_Mode=GPIO_Mode_IN;
	GPIO_InitStructure.GPIO_PuPd=GPIO_PuPd_NOPULL;
	GPIO_Init(GPIOG,&GPIO_InitStructure);	

	t=0;
	while(PGin(9))
	{
		t++;
		delay_us(1);
		if(t>=4000) return -1;
	}	
	
	t=0;
	while(PGin(9)==0)
	{
		t++;
		delay_us(1);
		if(t>=100) return -2;
	}
	
	t=0;
	while(PGin(9))
	{
		t++;
		delay_us(1);
		if(t>=100) return -3;
	}
	
	for(j=0; j<5; j++)
	{
		d=0;
		for(i=7; i>=0; i--)
		{
			t=0;
			while(PGin(9)==0)
			{
				t++;
				delay_us(1);
				if(t>=100) return -4;
			}

			delay_us(40);
		
			if(PGin(9))
			{
				d|=1<<i;
				t=0;
				while(PGin(9))
				{
					t++;
					delay_us(1);
					if(t>=100) return -5;
				}			
			}
		}	
		p[j]=d;
	}
	
	delay_us(50);
	check_sum=(p[0]+p[1]+p[2]+p[3])&0x00FF;
	if(p[4]!=check_sum) return -6;
	
	return 0;
}

void esp8266_init(void)
{
	printf("\\r\\n[DEBUG] ESP8266 Bemfa Cloud Start...\\r\\n");

	// 1. Exit transparent mode
	printf("[DEBUG] Exiting transparent transmission mode (sending +++)...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"+++");
	delay_ms(1500);

	// 2. Close old connection and set CIPMODE=0
	printf("[DEBUG] Setting Normal Transmission Mode (CIPMODE=0)...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CIPCLOSE\\r\\n");
	delay_ms(1000);
	usart_send_string(USART3,(uint8_t *)"AT+CIPMODE=0\\r\\n");
	delay_ms(1000);

	printf("[DEBUG] Sending AT...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT\\r\\n");
	delay_ms(1000);

	printf("[DEBUG] Setting CWMODE...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CWMODE_DEF=1\\r\\n");
	delay_ms(1000);
	
	printf("[DEBUG] Connecting to Wi-Fi (SSID: 114514)...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CWJAP_DEF=\\"114514\\",\\"88888888\\"\\r\\n");
	delay_ms(8000);	
	
	printf("[DEBUG] Setting Auto Connection...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CWAUTOCONN=1\\r\\n");
	delay_ms(2000);		

	printf("[DEBUG] Querying IP address...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CIFSR\\r\\n");
	delay_ms(3000);	
	
	printf("[DEBUG] Connecting to Bemfa Cloud (tcp.bemfa.com:8344)...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CIPSTART=\\"TCP\\",\\"tcp.bemfa.com\\",8344\\r\\n");
	delay_ms(1000);
	
	// 3. Subscribe to Bemfa Cloud light002 (59 bytes)
	printf("[DEBUG] Subscribing to Bemfa Cloud light002...\\r\\n");
	usart_send_string(USART3,(uint8_t *)"AT+CIPSEND=59\\r\\n");
	delay_ms(100);			
	
	usart_send_string(USART3,(uint8_t *)"cmd=1&uid=a8f227ec3a864292a3e2a6bdc4b0ea6d&topic=light002\\r\\n");
	delay_ms(1000);

	printf("[DEBUG] ESP8266 Bemfa Cloud Init Finished!\\r\\n");
}

int main(void)
{
	uint32_t count = 0;
	uint8_t dht_buf[5];
	int32_t rt;
	char msg_buf[128];
	char cmd_buf[32];

	NVIC_PriorityGroupConfig(NVIC_PriorityGroup_2);
	usart1_init(115200);
	usart3_init(115200);
	led_init();
	key_init();
	dht11_init();
	
	esp8266_init();
	
	while(1)
	{
		delay_ms(1000);
		count++;
		
		// Every 30 seconds, read DHT11 and upload data
		if(count >= 30)
		{
			count = 0;
			rt = dht11_read(dht_buf);
			
			if(rt == 0)
			{
				printf("[DEBUG] DHT11 Read Success! Temp: %d.%d C, Humi: %d.%d %%. Uploading to Bemfa Cloud...\\r\\n", 
					dht_buf[2], dht_buf[3], dht_buf[0], dht_buf[1]);
				
				sprintf(msg_buf, "cmd=2&uid=a8f227ec3a864292a3e2a6bdc4b0ea6d&topic=humiture004&msg=temp:%d.%d,humidity:%d.%d\\r\\n",
					dht_buf[2], dht_buf[3], dht_buf[0], dht_buf[1]);
				
				sprintf(cmd_buf, "AT+CIPSEND=%d\\r\\n", (int)strlen(msg_buf));
				usart_send_string(USART3, (uint8_t *)cmd_buf);
				delay_ms(100);
				
				usart_send_string(USART3, (uint8_t *)msg_buf);
			}
			else
			{
				printf("[DEBUG] DHT11 Read Failed (code=%d). Sending Fallback Ping...\\r\\n", (int)rt);
				usart_send_string(USART3,(uint8_t *)"AT+CIPSEND=6\\r\\n");
				delay_ms(100);
				usart_send_string(USART3,(uint8_t *)"ping\\r\\n");
			}
		}
	}
}

void USART1_IRQHandler(void)
{
	uint8_t d;
	if(USART_GetITStatus(USART1,USART_IT_RXNE)==SET)
	{
		d=USART_ReceiveData(USART1);
		if(d=='1') PFout(9)=0;
		if(d=='a') PFout(9)=1;
		USART_ClearITPendingBit(USART1,USART_IT_RXNE);
	}
}

void USART3_IRQHandler(void)
{
	uint8_t d;
	static char rx_win[16] = {0};
	
	if(USART_GetFlagStatus(USART3, USART_FLAG_ORE) == SET)
	{
		USART_ReceiveData(USART3); 
	}
	
	if(USART_GetITStatus(USART3,USART_IT_RXNE)==SET)
	{
		d=USART_ReceiveData(USART3);
		USART_SendData(USART1, d);
		
		for(int i = 0; i < 15; i++)
		{
			rx_win[i] = rx_win[i+1];
		}
		rx_win[15] = d;
		
		if(strstr(rx_win, "msg=on") != NULL)
		{
			PFout(9) = 0;
			memset(rx_win, 0, sizeof(rx_win));
		}
		else if(strstr(rx_win, "msg=off") != NULL)
		{
			PFout(9) = 1;
			memset(rx_win, 0, sizeof(rx_win));
		}
		
		USART_ClearITPendingBit(USART3,USART_IT_RXNE);
	}
}
"""
        new_data = final_code_str.encode('gbk')
        with open(file_path, 'wb') as f:
            f.write(new_data)
        print(f"Successfully fixed DHT11 integration in {file_path}")
            
    except Exception as e:
        print(f"Error for {file_path}: {e}")

fix_dht11_integration(r'd:\project_stm32\main.c')
fix_dht11_integration(r'd:\project_stm32\1.homework\demo1_wifi模块_AT指令\main.c')
