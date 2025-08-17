#include "main.h"
#include "tim.h"
#include "light.h"


/**
 * @brief 启动指示灯闪烁
 */
void Light_Start(void)
{
    __HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_2, (__HAL_TIM_GET_AUTORELOAD(&htim2) + 1) / 2);
    HAL_TIM_PWM_Start(&htim2, TIM_CHANNEL_2);
    HAL_TIM_Base_Start(&htim2);
}

/**
 * @brief 停止指示灯闪烁
 */
void Light_Stop(void)
{
    __HAL_TIM_SET_COMPARE(&htim2, TIM_CHANNEL_2, 0);
    HAL_TIM_PWM_Stop(&htim2, TIM_CHANNEL_2);
    HAL_TIM_Base_Stop(&htim2);
}

/**
 * @brief 在指定时间后停止指示灯闪烁
 * @param ms 停止前的延迟时间（毫秒），不得大于 6553.5
 */
void Light_StopAfter(uint16_t ms)
{
    __HAL_TIM_SetAutoreload(&htim3, ms * 10 - 1);
    __HAL_TIM_SetCounter(&htim3, 0);
    HAL_TIM_Base_Start_IT(&htim3);
}

/**
 * @brief 定时中断回调
 */
void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
    if (htim->Instance == TIM3) { Light_Stop(); }
}
