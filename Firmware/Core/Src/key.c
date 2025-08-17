#include "main.h"
#include "key.h"

/**
 * @brief 按键中断回调
 */
void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if (GPIO_Pin == Func_Pin)
    {
        if (HAL_GPIO_ReadPin(Func_GPIO_Port, Func_Pin) == GPIO_PIN_SET) { Key_Down(); }
        else { Key_Up(); }
    }
}

/**
 * @brief 按键按下
 */
void Key_Down(void)
{
    Light_Start();
    Light_StopAfter(1000);
}

/**
 * @brief 按键松开
 */
void Key_Up(void)
{
}
