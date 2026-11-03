# Awesome Digital Holographic Imaging / 数字全息成像资料导航

> A curated, evidence-aware collection for **digital holographic imaging and measurement**, with emphasis on **digital in-line holography (DIH/DIHM), digital holographic microscopy (DHM), lensless imaging, volumetric reconstruction, 3-D particle localization, underwater plankton imaging, open data, and optical hardware**.
>
> 一个以**数字全息成像、重建与测量**为边界的双语科研导航库。重点服务同轴/无物镜成像、三维颗粒定位、水下浮游生物和真实光学实验。

**Edition:** v0.1.0 · **Checked:** 2026-11-03 · **Status:** curated links, not a benchmark certification.

## 🔎 Scope / 收录范围

**Included / 核心：** 原始全息图数字采集；同轴、离轴和无物镜全息显微；衍射前向模型；角谱和菲涅耳传播；孪生像抑制；数字重聚焦；自动聚焦；三维颗粒检测、定位、尺寸估计与跟踪；水下全息系统；真实数据及公开标定资源。

**Related only / 仅作补充：** 定量相位成像（QPI）、相位恢复、深度学习、通用光波传播软件，须与数字全息实测或重建直接关联。

**Excluded / 不纳入主体：** 面向VR/AR的全息显示、CGH显示图案设计、光学神经网络的通用任务、普通浮游生物照片数据（非全息）、只有相位恢复而无全息场景的算法目录。

**Important / 使用提醒：** “源代码公开”“算得出3-D体”“有逐目标z输出”“有独立物理z真值”是四种不同的证据。它们在本仓库中保持区分；资源收录不代表其已经达到某个仪器测量精度或可以免训练复现。

## 📚 Navigation / 目录

| Section | Content | 中文 |
|---|---|---|
| [Reviews & foundational papers](resources/reviews.md) | Roadmaps and original studies | 综述、代表论文与研究脉络 |
| [Reconstruction & software](resources/software.md) | Open-source packages and repositories | 数值传播、重建、颗粒处理工具 |
| [3-D particle localization](resources/localization.md) | Focus, depth, diameter, tracking | 自动聚焦、逐颗粒三维定位 |
| [Optical hardware](resources/hardware.md) | Lensless/inline builds, instruments | 光路、无物镜硬件与开源装置 |
| [Datasets & benchmarks](resources/datasets.md) | Real holograms, data caveats | 真实全息数据、标签与评价边界 |
| [Learning & communities](resources/learning.md) | Tutorials, video, workshops | 教程、视频、课程、学术会议 |
| [Evaluation checklist](EVALUATION.md) | Reproducibility and GT standards | 科学评价与复现核验标准 |
| [Machine-readable catalog](data/resources.csv) | Structured source index | 可筛选的完整CSV索引 |

## ⭐ Start here / 优先收藏

| Resource | What you get | For whom |
|---|---|---|
| [Roadmap on Digital Holography](https://doi.org/10.1364/OE.435915) | Broad field overview; 25 sections | 建立数字全息全局认识 |
| [Digital in-line holographic microscopy](https://doi.org/10.1364/AO.45.000836) | Inline foundations; underwater plankton context | 同轴全息与原位水下应用 |
| [Autofocus criteria for plankton holograms (2025)](https://doi.org/10.1016/j.optcom.2025.132666) | 18 real-plankton focus functions | 多颗粒轴向定位、评价指标 |
| [PyHoloscope](https://github.com/MikeHughesKent/PyHoloscope) | Inline reconstruction and autofocus | 成熟Python重建接口 |
| [pyDHM](https://github.com/catrujilla/pyDHM) | Numerical propagators and DHM processing | 比较角谱/菲涅耳数值方法 |
| [ParticleHolography.jl](https://github.com/dainakai/ParticleHolography.jl) | Volumetric reconstruction and particle extraction | 三维颗粒测量，注意双相机示例界限 |
| [Open-source DLHM microscope](https://github.com/unal-optodigital/DLHM-Microscope) | 3-D-printable lensless hardware | 硬件搭建参考 |
| [Baltic Sea plankton dataset](https://zenodo.org/records/18405776) | Real underwater holography-derived plankton crops | 真实海洋目标；**无逐颗粒z真值** |

## 🧭 Research pipeline / 研究管线

```text
Illumination & sample / 光源和水样
      ↓
Sensor intensity hologram / CMOS强度全息图
      ↓
Background & optical calibration / 背景与光学标定
      ↓
Numerical propagation / 数值衍射传播（z-stack）
      ↓
Candidate detection / 颗粒候选检测
      ↓
Per-particle autofocus / 逐颗粒轴向聚焦
      ↓
3-D coordinates & morphology / 三维位置、尺寸与形态
      ↓
Independent GT and uncertainty / 独立参考真值与误差评价
```

请特别区分“人工提供x/y的GT辅助聚焦”和“从全幅全息图自动检测并定位”。请勿把均值残差、两种算法的一致性或选焦索引当作绝对深度误差。

## 🔖 Practical tags / 阅读标记

- **core**：直接数字全息成像与测量；**related**：相邻但有直接技术用途。
- **inline / off-axis / paired-camera / underwater**：实验成像构型，禁止直接混用精度结论。
- **public data ≠ independent GT**：公开图像未必有真实颗粒位置、形态和标定。
- `data/resources.csv` 保存全部条目的来源、构型、任务、限制和核验日期；主要链接来自论文出版社、作者官方仓库、机构存档或数据平台。

## 🤝 Contributing

欢迎通过GitHub Issue或Pull Request推荐新的数字全息**成像**资源。请附带原始来源、采集构型、开源与数据状态，并注明是否有逐颗粒深度真值。详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

This repository contains original concise descriptions and links to third-party sources. External code, data, papers, figures, and licenses remain with their respective owners. Listing here does not redistribute them or certify performance. See [LICENSE](LICENSE) for the license of this index's original text and utilities only.
