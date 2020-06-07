## SeqGAN
基于对抗网络的模糊测试。通过SeqGAN生成Modbus的消息。

### 参考：
[SeqGAN：https://arxiv.org/abs/1609.05473](https://arxiv.org/abs/1609.05473)
[基于对抗网络的模糊测试：https://doi.org/10.1145/3203217.3203241.](https://doi.org/10.1145/3203217.3203241.)
[代码参考：https://github.com/GaoQ1/seqgan](https://github.com/GaoQ1/seqgan)

## 训练核心
```
python main.py
```

## 训练语料
使用Modbus-tk生成的真实消息             


## Requirements
 - Python>3.5
 - Keras==2.2.4
 - tensorflow==1.12.0


## 使用步骤

将真实数据保存在train00.txt中，执行kongge.py，生成带有空格分隔的消息，执行main.py,生成数据，运行send.py（这里需要切换至python2.7版本）去掉多余空格并将报文发送至模拟器。使用wireshark查看捕获到的数据异常。
