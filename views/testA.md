#### 开发环境
最初所提出的基于 `SAC` 的多目标潮流控制方法是基于 `Python 3.6` 环境使用 `Tensorflow 1.14` 版本完成的。

先后对上述开发环境进行了升级，
1. 针对`Windows7`，目前的算法系统最新支持的版本包括：
+ `Tensorflow 2.4.1`
+ `Python 3.8.7`
+ `Streamlit 1.3.1`

<br> 

2. 针对`Windows10`，目前的算法系统最新支持的版本包括：
+ `Tensorflow 2.11.0`
+ `Python 3.10。4`
+ `Streamlit 1.17.0`  
  
<br> 

具体支持环境版本可通过以下控制台命令查看：
```python
pip3 show Tensorflow Streamlit
python --version
Streamlit --version
```


<div class="grid cards" markdown>

- :fontawesome-brands-html5: __HTML__ for content and structure
- :fontawesome-brands-js: __JavaScript__ for interactivity
- :fontawesome-brands-css3: __CSS__ for text running out of boxes
- :fontawesome-brands-internet-explorer: __Internet Explorer__ ... huh?

</div>



#### 测试环境
自 $2019$ 年 $11$ 月以来在国网江苏省电力有限公司控制中心应用。训练数据取自 EMS 系统的历史运行数据快照，每 $5$ 分钟一个数据断面，使用了江苏电网全拓扑节点/断路器模型，约 $1500$ 个节点和 $420$ 台发电机。

#### 控制目标
控制目标是在不违反母线电压约束（$[0.9,1.1] \, p.u.$） 和线路流量限制（ MVA 额定值的 $100\%$ ）的情况下最大限度地减少传输损失（至少减少 $0.5\%$ ）。

#### 测试方法
`SAC` 代理每 5 分钟调整 5 个发电厂 12 台发电机的电压设定值。从 $12/3/2019$ 到 $1/13/2020$，共收集了 $7,249$ 个运行快照。使用实际系统快照的时间序列训练和测试 `SAC` 代理的性能如下图所示，其中正奖励表示成功解决了电压和载流越限问题。