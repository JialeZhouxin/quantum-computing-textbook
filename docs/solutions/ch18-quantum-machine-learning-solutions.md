# 习题解答 · 第18章 量子机器学习

---

### 基础题（1-5）

**6.1** VQC 三步流程：
1. **数据编码**（量子）：将经典数据 $x$ 编码为量子态 $|\psi(x)\rangle$
2. **变分层**（量子）：应用参数化电路 $U(\theta)$ 产生 $|\psi(x,\theta)\rangle$
3. **测量与分类**（量子测量 + 经典后处理）：测量输出态，经典决策边界分类

**6.2** 解析形式：
$R_x(\theta) = \cos(\theta/2)I - i\sin(\theta/2)X$。
$R_x^\dagger(\theta) Z R_x(\theta)|0\rangle = (\cos(\theta/2)I + i\sin(\theta/2)X)Z(\cos(\theta/2)I - i\sin(\theta/2)X)|0\rangle$

计算：$Z$ 的旋转 $\to R_x^\dagger(\theta) Z R_x(\theta) = \cos\theta Z + \sin\theta Y$。

$\langle 0|(\cos\theta Z + \sin\theta Y)|0\rangle = \cos\theta$。$f(\theta) = \cos\theta$，$\partial f/\partial \theta = -\sin\theta$。

偏移规则验证：
$[f(\theta+\pi/2) - f(\theta-\pi/2)]/2 = [\cos(\theta+\pi/2) - \cos(\theta-\pi/2)]/2 = [-\sin\theta - \sin\theta]/2 = -\sin\theta$。✓

**6.3** 贫瘠高原：在深层量子电路中，梯度 $\partial \langle H \rangle/\partial \theta$ 的方差随量子比特数 $n$ 指数级减小。

向朋友解释："就像在巨大的黑暗房间里找一个小开关——随机移动手，方向越深就越难感觉到哪边是正确方向。"

**6.4** 振幅编码 vs 角度编码：

| | 振幅编码 | 角度编码 |
|--|---------|---------|
| 量子比特数 | $\log_2 N$ | $d$（特征数） |
| 电路深度 | $O(N)$ | $O(1)$ |
| NISQ 友好度 | 低 | 高 |

选择：6 个量子比特，深度 $\leq$ 10 层。选**角度编码**（最多 6 个特征），因为振幅编码需要 $2^6=64$ 维数据，电路深度远超 10 层。

**6.5** QGAN vs 经典 GAN：
经典 GAN：生成器（神经网络）→ 判别器（神经网络）。
QGAN：生成器（参数化量子电路）→ 判别器（经典或量子）。

量子生成器通常是一个参数化电路，从 $|0\rangle^{\otimes n}$ 制备目标分布。

---

### 提高题（6-9）

**6.6** 2 层 × 4 量子比特 × 1 参数/量子比特 = 8 个参数。
参数偏移规则每个参数需 2 次运行 = 16 次。但可并行测量，总运行次数 $2 \times$（最大可同时偏移的参数组数）。

**6.7** 贫瘠高原下梯度方差 $\text{Var}[\partial_\theta \langle Z_1 \rangle] \sim O(1/2^n)$。

$n=10$：$\text{Var} \sim 1/2^{10} \approx 10^{-3}$，标准差 $\sim 0.03$
$n=30$：$\text{Var} \sim 1/2^{30} \approx 10^{-9}$，标准差 $\sim 3 \times 10^{-5}$

说明：梯度信号被指数级抑制——优化器无法在合理时间内学习。解决贫瘠高原是 QML 最大的开放挑战之一。

**6.8** 量子核函数 $k(x_i, x_j) = |\langle \psi(x_i) | \psi(x_j) \rangle|^2$ 是两个量子态的重叠度。无法直接测量——需要 SWAP 测试或 Hadamard 测试来估计内积模平方。

Hadamard 测试电路：
```
q0: ──H──●────────H──M── 测量
         │
q1: ─────U_i──────U_j────
```
$U_i|0\rangle = |\psi(x_i)\rangle$。测量结果为 $P(0) - P(1) = \text{Re}\langle \psi(x_i) | \psi(x_j) \rangle$。

**6.9** $R_y(\theta)$ 参数偏移验证。

$f(\theta) = \langle 0| R_y^\dagger(\theta) Z R_y(\theta) |0\rangle = \cos\theta$（与 ch18-6.2 类似，$R_y$ 旋转将 $Z$ 变为 $\cos\theta Z + \sin\theta X$）。

$[f(\theta+\pi/2) - f(\theta-\pi/2)]/2 = [\cos(\theta+\pi/2) - \cos(\theta-\pi/2)]/2 = [-\sin\theta - \sin\theta]/2 = -\sin\theta = \partial f/\partial \theta$ ✓

---

### 综合题（10）

**6.10** 创业公司产品审查清单：

1. **数据规模与编码代价**：验证数据点数和维度。如果 20 比特用振幅编码可处理 $2^{20}$ 维数据，但初始态制备的电路深度 $O(2^{20})$ ——不可实现。如果使用角度编码，只能处理 20 个特征。
   **测试**：要求提供编码电路的具体分解和门数估计。

2. **贫瘠高原分析**：20 比特全局观测量可能导致梯度标准差 $~1/2^{10}$。
   **测试**：要求提供梯度范数随迭代变化曲线，验证网络是否在参数远离初始化的区域训练。

3. **经典基线对比**：99% 在什么数据集上？对比经典 SVM / XGBoost / 神经网络在相同数据上的表现。
   **测试**：要求提供经典基线性能（相同数据集、相同训练/测试划分）。

4. **数据泄露与过拟合**：训练集和测试集是否有重叠？准确率是在保持集上还是在训练集上？
   **测试**：要求提供交叉验证结果、混淆矩阵、以及训练/测试误差曲线。

5. **统计显著性**：99% 是单次运行还是多次平均？多次运行的方差是多少？
   **测试**：要求提供至少 5 次独立运行的平均值和标准差。
