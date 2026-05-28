# Task Progress: Explain SPI Teacher Note

## Progress Checklist:
- [x] Open Youdao Note SPI page
- [x] Find the main content iframe and inspect DOM
- [x] Extract markdown formatted text from iframe (Entire 14928 chars retrieved)
- [x] Capture key diagrams as screenshots:
  - [x] `spi_wiring_connections` (Standard multi-slave wiring)
  - [x] `spi_modes_timing` (CPHA/CPOL parameters & table)
  - [x] `w25q128_schematic` (W25Q128 Flash hardware interface)
- [x] Save findings locally & understand the content
- [x] Understand and organize:
  - [x] SPI Pins (MISO, MOSI, SCLK, NSS/CS)
  - [x] SPI Modes (Motorola Mode 0 & 3, TI SSI Mode)
  - [x] SPI Registers (Indirectly from STM32 structure, focused on hardware pins and software CS)
  - [x] Program Design Steps (Standard hardware init & GPIO simulation code)
- [x] Write detailed summary for the user

## Discoveries:
- The note is written by "粤嵌.温工" (Wen Gong from Yueqian).
- SPI is a high-speed, full-duplex, synchronous serial bus. Supports default 10Mbps, up to 37.5MHz on STM32F407.
- SPI Pins: MOSI (Master Out Slave In), MISO (Master In Slave Out), SCLK (Serial Clock), SS/CS (Slave Select).
- Motorola SPI Modes: defined by CPOL (Clock Polarity, idle level) and CPHA (Clock Phase, sample edge).
  - Mode 0: CPOL=0 (idle low), CPHA=0 (sample on 1st edge: rising edge).
  - Mode 3: CPOL=1 (idle high), CPHA=1 (sample on 2nd edge: rising edge).
  - Note: Mode 0 and Mode 3 are the most mainstream modes used.
- TI SPI Mode (SSI): NSS is low during standard SPI frame. In SSI, NSS has an active-high sync pulse of 1 clock width before each frame.
- SPI Flash (W25Q128):
  - Size: 128Mbit (16MB).
  - Structure: Page (256 bytes), Sector (16 pages = 4KB), Block (16 sectors = 64KB).
  - Operations: Write Enable (0x06), Page Program (0x02), Read Data (0x03), Read ID (0x9F / 0x90 / 0xAB), Read Status (0x05), Sector Erase (0x20).
  - W25Q128 IDs: Manufacturer=0xEF, Device=0x17, JEDEC=0xEF4017.
- Hardware connection:
  - PB3 (SPI1_SCK), PB4 (SPI1_MISO), PB5 (SPI1_MOSI) are controlled by STM32 SPI1 hardware.
  - PB14 (F_CS) is controlled by GPIO Software.
- Simulation Code (模拟SPI):
  - In Mode 0: SCLK idle is 0, MOSI is set before SCLK goes high, MISO is read when SCLK is high, SCLK is pulled low.
  - In Mode 3: SCLK idle is 1, SCLK goes low, MOSI is set, SCLK goes high, MISO is read when SCLK is high.

