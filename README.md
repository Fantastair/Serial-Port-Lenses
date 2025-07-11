# 串口透镜

一个小站点，串联在usart串口通信线路上，不干扰原始的通信，查看通信信息。

我不仅希望这个项目的成品能够成为开发调试的实用工具，也希望在项目制作中引入一些富有挑战性的内容。



### 概念构思

一个小长方盒，两端是通信接口，用于串联在原始通信线路上；上面是一块屏幕，实时显示通信内容；侧面有一个接口，可以连接电脑，发送监听到的信息；附加一些其他的小按钮，方便调试使用。



### 硬件设计

- #### 主控芯片

    选用STM32F103C8T6芯片作为数据监听与输出控制器，刚好有3个usart外设，两个的rx用于监听两根通信线，第三个用于和电脑通信。

    > 这一部分涉及基础的串口通信内容，没有过多的新鲜性，唯一有意思的是这次的接收实际上是窃听，属于通信中的第三者。我决定这个项目不再采用开发板搭建，而是直接自己绘制并焊接芯片外围电路。

- #### 屏幕

    本来打算用串口屏，但是我希望整个装置可以由电池独立供电，串口屏可能功耗偏高了，作为基础的文字显示需求使用裸屏即可。

    > 像素屏显示文字也是老技能了，这里也没有其他过多的需求。

- #### 电源

    采用可充电锂电池

    > 电源是所有电子系统的基础组成部分，电源的输出一般不会满足系统的需求，往往需要转换，这也是我一直十分头疼的问题。我为电赛绘制的电源模块使用的是隔离电源模块，这是我苦苦搜寻找到的最无脑也是效果最让我满意的模块，但是用在这个项目里显然不合适，我不得不再次直面低压电源转换这个问题。除此之外，还有充电电路的设计，希望网上的资源足够稳健。这也算是补全一块经验了。

- #### 主机通信

    我希望足够简单，最好是能牵一根USB线就能通信，这就需要芯片的外围电路上集成串口转USB电路，最好这个接口把充电的功能也包了。

    > C8T6 和 CH340 的原理图应该不难找，这回的电路设计有的整了。

- #### 其他附加功能

    我目前想到的一个就是不用区分两个通信线是rx还是tx，要是接反了，通过一个机械开关一键反接回来；另外要支持待机和唤醒，这个大多数MCU都有，甚至一些小芯片也有这个功能（我见过外挂的ADC采集芯片支持休眠和唤醒的）

    > 反接就是一个双刀双掷开关吧，待机需要研究一下，没怎么用过。



### 软件设计

这个没什么难度了，收发数据和显示罢了。

不过既然能和电脑连接通信，那么我的传统艺能，一个好看好用的上位机软件自然是少不了了。与电脑通信的主要目的是解决小屏幕显示信息量有限的问题。



### 外壳设计

方正小巧、舒适圆角、简约外观、3D打印。

### 

## 25.7.7更新

第一轮设计与测试已经结束了，结果是失败的（最小系统并没有正常运行），由于第一步迈得太大了，导致我不知道是哪个环节出了问题，我一共焊了两块板子，都失败了，应该排除了焊接因素，问题主要出在电路设计上。目前的测试结果为：STlink能够识别设备，但是第一次下载了程序以后就不能下载了（我印象中第一次下载是成功了的，反正后面是下不进去），然后测试外挂晶振都没有起振（不清楚是不是探针太粗了压根没测到），供电上可能存在几处短路或设计缺陷（上电后出现引脚处冒烟现象），电源相关模块里有一个东西比较烫，摆得比较密，摸不出来是哪一个元件在发热。总之这一版问题还是比较大。

由此我决定，分阶段设计制作，首先制作一个简化版，在此基础上拓展成为最初设想的完全体。

简化版抛弃 屏幕、电池、SWD调试功能，通过串口下载程序，通过上位机显示数据，通过USB供电。
