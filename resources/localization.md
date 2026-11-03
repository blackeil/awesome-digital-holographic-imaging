# Three-dimensional particle localization / 逐颗粒三维定位

**重点任务：** 从单幅全息图出发生成多深度重建体，在没有GT x/y提示的情况下检测颗粒，并为每个目标分别输出 `x, y, z, diameter`；能够用独立已知的轴向距离进行误差评价。

## Directly relevant methods / 直接相关方法

| Resource | Geometry / 成像方式 | Outputs / 目标 | Main limitation / 证据边界 |
|---|---|---|---|
| [ParticleHolography.jl](https://github.com/dainakai/ParticleHolography.jl) | inline; single-frame wavefront API | volume, candidates and per-object depth | Real end-to-end tutorial uses dual-camera phase retrieval |
| [DarkTrack](https://github.com/MRogalski96/DarkTrack) | digital in-line | 3-D positions and 4-D tracks | Large companion dataset; independent real z GT needs auditing |
| [HoloD3](https://github.com/dainakai/HoloD3) | particle holograms | depth, diameter | Check weights and single-frame accuracy |
| [HoloPy](https://github.com/manoharan-lab/holopy) | scattering-based inline | fitted sphere xyz and radius | Sphere assumptions; fitted parameters ≠ independent size/z truth |
| [pylorenzmie](https://github.com/davidgrier/pylorenzmie) | colloid inline videos | 3-D localization and scattering fit | Sphere scattering-model assumptions |
| [3D-MB-HoloNet](https://github.com/Ni-Chen/3D-MB-HoloNet) | model-based single hologram | particle volumes | Test weights/data/environment before treating as turnkey |
| [Holo1](https://github.com/CCCofficial/Holo1) | low-cost inline | 2-D image processing and reconstruction | No verified end-to-end per-particle z |

## Focus-function evidence / 选焦文献

- **[Moreno et al., 2025 — 18 autofocus criteria on plankton holograms](https://doi.org/10.1016/j.optcom.2025.132666).** 当下非常相关：研究真实浮游生物和不同像元尺寸下的聚焦指标，报告Q、D、MDCT等结果。评估参照为人工选定焦面，**不能等同独立位移台known-z**。特别值得在开展新指标测试前完整阅读方法和适用场景。
- **[PyHoloscope autofocus examples](https://github.com/MikeHughesKent/PyHoloscope).** 可复用的传播和焦点评分实现；具体指标须冻结，不能看GT后事后选最佳。
- **[ParticleHolography.jl](https://dainakai.github.io/ParticleHolography.jl/stable/).** 三维体重建、投影及颗粒提取工作流，评估前需要明确输入条件。

## Minimum acceptable evaluation / 最低评价要求

1. 先固定光学参数与传感器z参考面，保持原始完整强度全息图、背景、波长、介质折射率和像元尺寸的可追溯性。
2. 区分**GT-ROI辅助聚焦**与**整幅图自动检测+独立z定位**。
3. 对每个GT颗粒给出候选匹配、`z_truth`、`z_pred`、`|error|`；漏检、额外候选和扫描边界峰不得删除。
4. 仅对具有独立GT的真实实验报告真实测量误差；合成真值、两方法一致度、模型拟合残差各有不同用途。
5. 监测空白输入反向传播后的边界条纹、背景聚焦假峰和归一化敏感性。
