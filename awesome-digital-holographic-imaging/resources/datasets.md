# Open holographic datasets / 真实数据与示例

**关键列：raw sensor hologram? independent per-particle z ground truth?** 很多所谓“全息数据集”只提供重建后裁剪图或二维检测图；以下逐项指出限制。



### [Baltic Sea 2024 in-situ plankton holographic image crops](https://zenodo.org/records/18405776)

- **[CORE]** `underwater holography` · plankton image crops · data · 2026
- AUTOHOLO实测后处理浮游生物裁剪图；有采样站位元数据。

- **边界：** 裁剪/处理图，未声明提供原始传感器全息图；无物种或逐颗粒z标签。



### [phdemo paired holograms and calibration images](https://github.com/dainakai/phdemo)

- **[CORE]** `two cameras` · experimental holograms/3D · data · 2026
- 100对1024×1024双相机水滴全息图及标定图，含工作流。

- **边界：** 数据包含双相机输入，不能直接当单幅全息基准。



### [Holo1 cropped holograms](https://github.com/CCCofficial/Holo1)

- **[CORE]** `inline` · plankton/fiber crops · data · ongoing
- 64张真实全息裁剪图，包含浮游生物与纤维案例。

- **边界：** 缺逐颗粒真实z、完整视频和经核验GT。



### [HoloPy official real fitting tutorial](https://holopy.readthedocs.io/en/latest/tutorial/fit_tutorial.html)

- **[CORE]** `inline` · single sphere fitting · tutorial/data · ongoing
- 官方小球真实全息图与背景、参数拟合示例。

- **边界：** 官方拟合参考不是独立物理z真值。



### [PyHoloscope inline demonstration](https://pyholoscope.readthedocs.io/en/latest/index.html)

- **[CORE]** `inline` · refocusing example · tutorial/data · ongoing
- 带数据的同轴全息重聚焦和自动聚焦Notebook入口。

- **边界：** 示例结果不自动代表三维颗粒定量误差。



### [HoloBio biological hologram examples](https://sophia-research-lab.github.io/HoloBio/)

- **[RELATED]** `DHM/DLHM` · bio sample data · tutorial/data · 2026
- 提供代表性生物全息图和显微软件演示资料。

- **边界：** 公开数据内容应逐文件核验。



### [QPI-DHM evaluation sample holograms](https://github.com/SOPHIA-Research-Lab/Standardized-QPI-DHM-Evaluation-Protocol)

- **[RELATED]** `DHM/QPI` · test targets · data/code · ongoing
- 包含USAF分辨率板、星形靶及生物样本的测试全息图。

- **边界：** 偏物镜成像及相位评价。



### [DarkTrack example data entry](https://github.com/MRogalski96/DarkTrack)

- **[RELATED]** `inline DIHM` · 4D tracking data · external data link · ongoing
- 官方仓库提供示例数据的外部下载入口。

- **边界：** 体积较大、内部最小复现样本和GT尚需核验。


