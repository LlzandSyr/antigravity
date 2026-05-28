# Plan: Extract RTC Notes

1. [x] Navigate to the Youdao Note URL (Done)
2. [x] Verify page is loaded (Done)
3. [x] Extract content of the note. (Done)
    - Extracted all text, code snippets, and explanations via JS from the iframe.
    - Scrolled and inspected diagrams for "四、时钟体系" and "五、供电".
4. [ ] Summarize and explain RTC based on the extracted notes. (In Progress)

## Findings
- **Overview**: RTC (Real Time Clock) is an independent BCD timer/counter. It provides calendar clock, alarm interrupts, and periodic wakeup. Uses BCD format for time/date. Keeps running on VBAT when VDD is off.
- **Interrupts**: RTC interrupts connect to EXTI. For Alarm, use EXTI Line 17 & RTC_Alarm IRQ. For Wakeup, use EXTI Line 22 & RTC_WKUP IRQ.
- **Initialization**:
  - Requires PWR clock enabled and Backup Access enabled.
  - LSE (preferred) or LSI clock source.
  - Setup prescalers (`AsynchPrediv` & `SynchPrediv`) to get 1Hz clock (ck_spre).
  - Configure initial Date and Time using BCD or BIN format.
  - Configure Wakeup (disable, select clock, set counter, clear IT flag, enable IT, enable wakeup).
  - EXTI Line 22 and NVIC configuration for RTC WKUP.
- **Wakeup ISR**: Handles `RTC_IT_WUT` and clears flags for both RTC and EXTI.
- **Read/Write**: Uses `RTC_GetTime`/`RTC_GetDate` and `RTC_SetTime`/`RTC_SetDate`.
- **BCD vs BIN**: BCD uses 4-bit binary for each decimal digit (e.g. 10 is `0x10`). BIN is standard binary. STM32 API supports both formats via `RTC_Format_BCD` and `RTC_Format_BIN`.
- **Alarms**: Support Alarm A and Alarm B. Need to disable alarm before configuring to avoid BUG. Uses masks to trigger alarm periodically (e.g. mask Date/Weekday to trigger daily).
- **Backup Registers (BKP)**: 20x 32-bit registers (80 bytes) powered by VBAT. Not reset by system reset. Used to store init flag (e.g., `0x5678` in `RTC_BKP_DR0`) to avoid resetting time on reboot.
