# 习题解答 · 第17章 变分量子算法：VQE与QAOA

---

### 基础题（1-5题）

**1.** 变分量子-经典混合架构的三个核心组件：

1. **参数化量子电路（Ansatz）**：$U(\vec{\theta})$ 生成试探态 $|\psi(\vec{\theta})\rangle$
2. **量子期望值测量**：在量子硬件上测量哈密顿量的期望值 $\langle H \rangle = \langle \psi(\vec{\theta}) | H | \psi(\vec{\theta}) \rangle$
3. **经典优化器**：根据测量结果更新参数 $\vec{\theta}$，最小化 $\langle H \rangle$

经典-量子之间的迭代循环构成整个算法。

**2.** Rayleigh-Ritz 变分原理证明。

将 $|\psi\rangle$ 在 $H$ 的本征基 $\{|E_i\rangle\}$ 下展开：$|\psi\rangle = \sum_i c_i |E_i\rangle$，且 $\sum_i |c_i|^2 = 1$。

$\langle\psi|H|\psi\rangle = \sum_i |c_i|^2 E_i \geq \sum_i |c_i|^2 E_0 = E_0 \sum_i |c_i|^2 = E_0$

等号当且仅当 $|\psi\rangle = |E_0\rangle$（基态）。因此最小化 $\langle\psi|H|\psi\rangle$ 可逼近基态能量。

**3.** Jordan-Wigner 映射中 Z 串的必要性。

费米子产生/湮灭算符满足反对易关系：$\{a_i^\dagger, a_j\} = \delta_{ij}$。

JW 映射：$a_j^\dagger = \left(\bigotimes_{k=0}^{j-1} Z_k\right) \otimes \sigma_j^+$

Z 串 $\bigotimes_{k=0}^{j-1} Z_k$ 保证了不同轨道算符之间的反对易关系。没有 Z 串（即只使用 Pauli 产生算符）时，映射后的算符会满足对易而非反对易关系。

**4.** H₂ 在 STO-3G 基组下需要 4 个量子比特（两个电子，两个空间轨道，考虑自旋后共 4 个自旋轨道）。实际上 H₂ 的最小基组描述需要 2 个空间轨道 × 2 个自旋 = 4 个自旋轨道。

**5.** 化学精度（Chemical Accuracy）定义为 $1.6 \times 10^{-3}$ Hartree（约 1 kcal/mol）。这是量子化学计算中公认的"足够精确"的标准——在此精度下，化学反应能量的计算与实验测量值可比。

---

### 进阶题（6-10题）

**6.** 哈密顿量泡利串分解。

量子计算机天然只做 $Z$ 基测量。将 $H$ 分解为泡利串之和 $H = \sum_k c_k P_k$（$P_k$ 为 Pauli 张量积），每个 $P_k$ 可根据泡利矩阵的本征基变换转换为 $Z$ 基测量。

- $Z$ 期望值：直接 $Z$ 基测量
- $X$ 期望值：在测量前施加 $H$ 门（$HZH = X$）
- $Y$ 期望值：在测量前施加 $S^\dagger H$ 门

每个泡利串独立测量，结果按系数加权求和。

**7.** 参数偏移规则推导。

$U(\theta) = e^{-i\theta G/2}$，$G^2 = I$。

$U(\theta) = \cos(\theta/2)I - i\sin(\theta/2)G$

$E(\theta) = \langle 0|U^\dagger(\theta) H U(\theta)|0\rangle$

$E(\theta \pm \pi/2) = \langle 0|U^\dagger(\theta) e^{\mp i\pi G/4} H e^{\pm i\pi G/4} U(\theta)|0\rangle$

$e^{\pm i\pi G/4} = \cos(\pi/4)I \pm i\sin(\pi/4)G = (I \pm iG)/\sqrt{2}$

$[E(\theta + \pi/2) - E(\theta - \pi/2)]/2 = \langle 0|U^\dagger(\theta)(-i)[G, H]/2 U(\theta)|0\rangle$

由 $H$ 对 $\theta$ 的偏导：$\partial E/\partial \theta = \langle 0|U^\dagger(\theta)(-i)[G, H]/2 U(\theta)|0\rangle = [E(\theta+\pi/2) - E(\theta-\pi/2)]/2$

**8.** HEA vs UCCSD。

| 方面 | HEA | UCCSD |
|------|-----|-------|
| 电路深度 | 浅（硬件高效） | 深（$O(N^4)$ 门） |
| 化学精度 | 难以达到 | 系统可达 |
| 可表达性 | 有限（纠缠不足） | 充足 |
| NISQ 适用性 | 高 | 低 |

NISQ 设备上推荐 HEA——更浅的电路在噪声环境下保真度更高。UCCSD 需要容错量子计算机。

**9.** SPSA（Simultaneous Perturbation Stochastic Approximation）在每次迭代中随机扰动所有参数方向，只做 2 次函数求值（而非 $2p$ 次）。因为 VQE 的测量结果本身有统计噪声，精确梯度计算既昂贵又无必要——随机近似足够。

**10.** 泡利串分组（图着色）。

将每个泡利串视为图的顶点，如果两个泡利串不对易则连边。对图进行着色（最小颜色数），同色顶点对应的泡利串可以同时测量。

集合 $\{Z_0Z_1, Z_1Z_2, X_0X_1, Y_0Y_1\}$：
- $Z_0Z_1$ 与 $Z_1Z_2$ 对易（仅 Z 算符）
- $X_0X_1$ 与 $Y_0Y_1$ 反对易（$X$ 与 $Y$ 反对易）
- $Z_0Z_1$ 与 $X_0X_1$ 反对易（$Z$ 与 $X$ 反对易）

分组方案：$\{Z_0Z_1, Z_1Z_2\}$，$\{X_0X_1\}$，$\{Y_0Y_1\}$——3 组。

---

### 应用题（11-15题）

**11.** 三角形图 MaxCut。

**(a)** 成本函数：$C = \frac12\sum_{(i,j)\in E} (1 - z_i z_j)$，对于三角形图三条边权重都为 1。
$C(z) = \frac12[(1 - z_0 z_1) + (1 - z_1 z_2) + (1 - z_2 z_0)] = \frac32 - \frac12(z_0 z_1 + z_1 z_2 + z_2 z_0)$

**(b)** 成本哈密顿量：$\hat{H}_C = -\frac12\sum_{(i,j)} Z_i Z_j = -\frac12(Z_0 Z_1 + Z_1 Z_2 + Z_2 Z_0)$

**(c)** $p=1$ QAOA 电路：
```
q0: ──H──Rz(-γ)──●───────────Rx(2β)───
                 │
q1: ──H──Rz(-γ)──X───Rz(-γ)──Rx(2β)───
                     │
q2: ──H──────────────X───────Rx(2β)───
```

**12.** 4-正则图 $p=1$ QAOA。

$\langle Z_i Z_j \rangle = \sin(2\beta)\sin(2\gamma)\cos^2(2\gamma)$

**(a)** 最大化近似比即最大 $\langle Z_i Z_j\rangle$。数值搜索 $(\gamma, \beta) \in [0, \pi] \times [0, \pi/2]$：
最优值约 $\gamma^* \approx 0.15\pi$，$\beta^* \approx 0.25\pi$。

**(b)** 对应 $\langle Z_i Z_j \rangle_{\text{max}} \approx 0.385$。近似比 $r = \frac12(1 + \langle Z_i Z_j \rangle) / \frac12(1 + 1) \approx 0.692$——这是 $p=1$ QAOA 的理论保证。

**13.** 测量分组节省。

无分组：$N_{\text{term}} \times N_{\text{shot}} = 50 \times 10^4 = 5 \times 10^5$ 次测量。
分组后：$K \times N_{\text{shot}} = 8 \times 10^4$ 次测量。
节省比例：$(50 - 8)/50 = 84\%$。

**14.** ZNE 外推。

$\lambda = 1, 2, 3$，$\langle H \rangle_\lambda = -1.02, -1.08, -1.18$。

设 $E(\lambda) = E_0 + \epsilon\lambda + \delta\lambda^2$。

代入三点：
$E_0 + \epsilon + \delta = -1.02$
$E_0 + 2\epsilon + 4\delta = -1.08$
$E_0 + 3\epsilon + 9\delta = -1.18$

解：$\delta = -0.02$，$\epsilon = -0.02$，$E_0 = -0.98$ Hartree。

零噪声能量估计：$E_0 \approx -0.98$ Hartree。

**15.** VQE vs QAOA 对比。

| 角度 | VQE | QAOA |
|------|-----|------|
| 算法结构 | 任意参数化 Ansatz | 特定层状结构（$e^{-i\gamma H_C} e^{-i\beta H_M}$） |
| 参数空间 | 多样（HEA, UCCSD, ...） | 固定结构，$2p$ 个参数 |
| 应用领域 | 量子化学、材料模拟 | 组合优化（MaxCut, TSP, ...） |
| 理论基础 | Rayleigh-Ritz 变分原理 | 绝热定理 + 逼近论 |

选择 VQE：当目标是量子化学/材料计算时。
选择 QAOA：当目标是组合优化问题时。
