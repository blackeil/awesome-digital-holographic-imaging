# Open-source reconstruction & analysis / 开源软件

**收录≠复现PASS。** 应检查成像构型、依赖、源码许可证、数据与逐颗粒真值；单相机算法与双相机示例必须区分。



### [PyHoloscope](https://github.com/MikeHughesKent/PyHoloscope)

- **[CORE]** `inline/off-axis` · reconstruction/autofocus · code · ongoing
- Python数字全息显微重建，包含同轴全息、自动聚焦和在线示例。

- **边界：** 聚焦输出不能自动等同逐颗粒known-z精度。



### [pyDHM](https://github.com/catrujilla/pyDHM)

- **[CORE]** `inline/off-axis` · propagation/phase · code · ongoing
- 包含角谱、菲涅耳、Fresnel-Bluestein等传播器以及不同记录配置。



### [HoloPy](https://github.com/manoharan-lab/holopy)

- **[CORE]** `inline/model fitting` · reconstruction/scattering · code · ongoing
- 数字全息图重建、光散射模拟与球形等结构参数拟合。

- **边界：** 单球拟合≠非球形浮游生物真值；许可证须遵守原仓库。



### [pylorenzmie](https://github.com/davidgrier/pylorenzmie)

- **[CORE]** `inline holographic video` · 3D sphere fitting/tracking · code · 2026
- Lorenz–Mie球形颗粒全息拟合、定位和追踪工具。

- **边界：** 适合接近球形且散射模型合理的对象。



### [ParticleHolography.jl](https://github.com/dainakai/ParticleHolography.jl)

- **[CORE]** `inline` · 3D reconstruction/particle detection · code · ongoing
- Julia三维传播、颗粒检测和轨迹关联工具；提供单图Gabor波前接口。

- **边界：** 真实完整教程采用双相机，相机配置需区分。



### [phdemo](https://github.com/dainakai/phdemo)

- **[CORE]** `paired-camera` · dataset/3D pipeline · tutorial/code/data · 2026
- ParticleHolography配套真实双相机水滴实验教程，含图像、标定、三维检测。

- **边界：** 不可直接称为单相机验证。



### [HoloD3](https://github.com/dainakai/HoloD3)

- **[RELATED]** `holographic particle imaging` · 3D particle estimation · code · ongoing
- 从重建全息体最小强度投影检测颗粒并估计深度与直径。

- **边界：** 需检查单相机性能、模型权重与数据配置。



### [DarkTrack](https://github.com/MRogalski96/DarkTrack)

- **[CORE]** `DIHM` · 4D localization/tracking · code · 2022
- MATLAB无物镜同轴全息多颗粒四维跟踪与合成示例。

- **边界：** 公开数据体积较大，真实GT完整性尚未确认。



### [3D-MB-HoloNet](https://github.com/Ni-Chen/3D-MB-HoloNet)

- **[CORE]** `inline` · 3D particle deep learning · code · 2021
- 基于物理点扩散函数先验的三维全息颗粒网络。

- **边界：** 老版依赖；现行分支及预训练权重必须重新核验。



### [Dense-U-net](https://github.com/THUHoloLab/Dense-U-net)

- **[RELATED]** `inline holography` · 3D particle deep learning · code · ongoing
- 数字全息颗粒深度学习方法的开源代码候选。

- **边界：** 复现所需权重、数据与许可证需另行核验。



### [Holo1](https://github.com/CCCofficial/Holo1)

- **[CORE]** `inline/lensless` · plankton 2D detection/reconstruction · code/data · ongoing
- 浮游生物全息裁剪图、传统传播和二维检测流程参考。

- **边界：** 已知原始视频缺口；无经认证的逐颗粒独立z。



### [HoloBio](https://github.com/SOPHIA-Research-Lab/HoloBio)

- **[CORE]** `DHM/DLHM` · reconstruction/bio-analysis · code · 2026
- 数字全息显微重建、微粒跟踪及生物定量分析界面。

- **边界：** 须区分离轴和无物镜配置。



### [DHM in ImageJ](https://github.com/unal-optodigital/DHM)

- **[CORE]** `DHM image-plane` · reconstruction/phase · plugin · ongoing
- ImageJ的数字全息实时重建和仿真插件。

- **边界：** 以其影像面/离轴架构为主要参考。



### [DLHM in ImageJ](https://github.com/unal-optodigital/DLHM)

- **[CORE]** `lensless DHM` · simulation/reconstruction · plugin · ongoing
- 无物镜数字全息ImageJ插件，含衍射前向仿真与重建。



### [DHMx Software Suite](https://github.com/dhm-org/dhm_suite)

- **[RELATED]** `off-axis DHM` · camera/acquisition/reconstruction · code · ongoing
- 相机服务器、实时采集界面与离轴全息重建软件套件。

- **边界：** 主要用于离轴配置，且依赖较旧系统。



### [Standardized QPI-DHM Evaluation Protocol](https://github.com/SOPHIA-Research-Lab/Standardized-QPI-DHM-Evaluation-Protocol)

- **[RELATED]** `DHM/QPI` · quality evaluation · code/data · ongoing
- 数字全息相位图重建质量评估指标、实验图像与数值评估框架。

- **边界：** 侧重QPI，不能替代独立颗粒z真值。



### [HoloD3 Suite overview](https://dainakai.github.io/projects/holod3-suite/)

- **[RELATED]** `holographic particle imaging` · 3D measurement/tracking · software collection · ongoing
- HoloD3、轨迹关联及轨迹平滑系列软件导航。

- **边界：** 不同软件环节的数据合同需核验。


