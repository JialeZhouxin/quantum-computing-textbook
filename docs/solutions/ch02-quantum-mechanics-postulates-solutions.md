# 习题解答 · 第2章 量子力学基本假设

---

### 基础题（1-6题）

**1.** 为什么全局相位不可观测？举一个具体的例子说明 $|\psi\rangle$ 和 $e^{i\alpha}|\psi\rangle$ 在投影测量下的区别。

**解：**

全局相位因子 $e^{i\alpha}$ 在计算测量概率时被消去。对于任意投影测量算符 $P_m = |m\rangle\langle m|$：

$$
P(m) = |\langle m|(e^{i\alpha}|\psi\rangle)|^2 = |e^{i\alpha}\langle m|\psi\rangle|^2 = |\langle m|\psi\rangle|^2
$$

测量概率与 $\alpha$ 无关。具体例子：$|\psi\rangle = |0\rangle$ 和 $e^{i\pi/4}|0\rangle$，在计算基下测量，两者都得到 $|0\rangle$ 的概率为 1，完全不可区分。

但**相对相位**（如 $\frac{1}{\sqrt{2}}(|0\rangle + e^{i\beta}|1\rangle)$ 中的 $\beta$）是可观测的——它影响干涉条纹的位置。

**2.** 算符 $\hat{A} = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}$ 是否厄米？求本征值和本征态。

**解：**

$$
\hat{A}^\dagger = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}^\dagger = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix} = \hat{A}
$$

$\hat{A}^\dagger = \hat{A}$，因此是厄米算符。注意 $\hat{A} = Y$（Pauli $Y$ 矩阵）。

求本征值：$\det(\hat{A} - \lambda I) = \det\begin{pmatrix}-\lambda & -i\\ i & -\lambda\end{pmatrix} = \lambda^2 - 1 = 0$，$\lambda = \pm 1$。

$\lambda = 1$：$\begin{pmatrix}-1 & -i\\ i & -1\end{pmatrix}v = 0$，$-v_1 - i v_2 = 0$，$v_1 = -i v_2$，归一化得 $|+\rangle_Y = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$。

$\lambda = -1$：$\begin{pmatrix}1 & -i\\ i & 1\end{pmatrix}v = 0$，$v_1 - i v_2 = 0$，$v_1 = i v_2$，$|-\rangle_Y = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$。

**3.** 对处于 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ 的量子比特进行 Z 基测量，求：(a) 测得 $|0\rangle$ 的概率 (b) 期望值 $\langle Z\rangle$。

**解：**

**(a)** $P(0) = |\langle 0|+\rangle|^2 = |\frac{1}{\sqrt{2}}|^2 = \frac{1}{2}$。同理 $P(1) = \frac{1}{2}$。

**(b)** $\langle Z\rangle = \langle+|Z|+\rangle = \frac{1}{2}(1, 1)\begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}\begin{pmatrix}1\\ 1\end{pmatrix} = \frac{1}{2}(1, -1)\begin{pmatrix}1\\ 1\end{pmatrix} = 0$。

或直接 $\langle Z\rangle = P(0) - P(1) = \frac{1}{2} - \frac{1}{2} = 0$。

**4.** 证明若 $[A, B] = 0$，则 $A$ 和 $B$ 有共同的本征态集合。

**解：**

设 $|\lambda_i\rangle$ 是 $A$ 的本征态，本征值 $\lambda_i$：

$$
A|\lambda_i\rangle = \lambda_i|\lambda_i\rangle
$$

将 $B$ 作用到本征方程两边：

$$
BA|\lambda_i\rangle = B\lambda_i|\lambda_i\rangle = \lambda_i B|\lambda_i\rangle
$$

由 $[A, B] = 0$ 得 $AB = BA$，因此：

$$
A(B|\lambda_i\rangle) = BA|\lambda_i\rangle = \lambda_i (B|\lambda_i\rangle)
$$

$B|\lambda_i\rangle$ 也是 $A$ 的本征态，对应本征值 $\lambda_i$。如果 $\lambda_i$ 非简并，则 $B|\lambda_i\rangle \propto |\lambda_i\rangle$，即 $|\lambda_i\rangle$ 也是 $B$ 的本征态。

如果 $\lambda_i$ 有简并，需在简并子空间中对角化 $B$——但总能找到一组同时是 $A$ 和 $B$ 本征态的正交基。

**5.** 一个二能级系统的哈密顿量为 $H = \hbar\omega Z/2$，初始态为 $|+\rangle$，求任意时刻 $t$ 的态矢量。

**解：**

时间演化算符 $U(t) = e^{-iHt/\hbar} = e^{-i\omega t Z/2} = \cos(\omega t/2) I - i\sin(\omega t/2) Z$。

$$
|\psi(t)\rangle = U(t)|+\rangle = \cos(\omega t/2)|+\rangle - i\sin(\omega t/2) Z|+\rangle
$$

由 $Z|+\rangle = |-\rangle$：

$$
|\psi(t)\rangle = \cos(\omega t/2)|+\rangle - i\sin(\omega t/2)|-\rangle
$$

用 $|0\rangle, |1\rangle$ 展开：

$$
|\psi(t)\rangle = \frac{\cos(\omega t/2) - i\sin(\omega t/2)}{\sqrt{2}}|0\rangle + \frac{\cos(\omega t/2) + i\sin(\omega t/2)}{\sqrt{2}}|1\rangle
$$

即 $|\psi(t)\rangle = \frac{e^{-i\omega t/2}}{\sqrt{2}}|0\rangle + \frac{e^{i\omega t/2}}{\sqrt{2}}|1\rangle$——布洛赫球上绕 $z$ 轴旋转，角速度 $\omega$。

**6.** 简述量子不可克隆定理的证明思路。

**解：**

假设存在一个克隆算符 $U$，使得对任意 $|\psi\rangle$：

$$
U(|\psi\rangle \otimes |0\rangle) = |\psi\rangle \otimes |\psi\rangle
$$

对两个不同态 $|\psi\rangle$ 和 $|\phi\rangle$ 分别作用：

$$
U(|\psi\rangle|0\rangle) = |\psi\rangle|\psi\rangle,\quad U(|\phi\rangle|0\rangle) = |\phi\rangle|\phi\rangle
$$

取内积：左边内积 $\langle\phi|\psi\rangle\langle 0|0\rangle = \langle\phi|\psi\rangle$，右边内积 $\langle\phi|\psi\rangle\langle\phi|\psi\rangle = (\langle\phi|\psi\rangle)^2$。

因此 $\langle\phi|\psi\rangle = (\langle\phi|\psi\rangle)^2$，解得 $\langle\phi|\psi\rangle = 0$ 或 $1$。除非两态正交或相同，否则矛盾。所以不存在能克隆任意量子态的幺正算符。

---

### 提高题（7-12题）

**7.** 证明不确定关系 $\Delta A \Delta B \ge \frac{1}{2}|\langle[A, B]\rangle|$。

**解：**

定义 $|f\rangle = (A - \langle A\rangle)|\psi\rangle$，$|g\rangle = (B - \langle B\rangle)|\psi\rangle$。

由 Cauchy-Schwarz 不等式：

$$
\langle f|f\rangle\langle g|g\rangle \ge |\langle f|g\rangle|^2
$$

$\langle f|f\rangle = (\Delta A)^2$，$\langle g|g\rangle = (\Delta B)^2$。

$\langle f|g\rangle = \langle AB\rangle - \langle A\rangle\langle B\rangle$。

将 $\langle f|g\rangle$ 分解为实部和虚部：

$$
|\langle f|g\rangle|^2 \ge |\text{Im}\langle f|g\rangle|^2 = \left|\frac{\langle f|g\rangle - \langle g|f\rangle}{2i}\right|^2
$$

$\langle f|g\rangle - \langle g|f\rangle = \langle[A, B]\rangle$。代入即得：

$$
(\Delta A)^2(\Delta B)^2 \ge \left|\frac{\langle[A, B]\rangle}{2i}\right|^2 = \frac{1}{4}|\langle[A, B]\rangle|^2
$$

两边开方：$\Delta A \Delta B \ge \frac{1}{2}|\langle[A, B]\rangle|$。

**8.** 一个量子比特的布洛赫矢量为 $\vec{r} = (\sin\theta\cos\phi, \sin\theta\sin\phi, \cos\theta)$，求对应的态矢量。

**解：**

布洛赫球面上纯态的一般形式：

$$
|\psi\rangle = \cos\frac{\theta}{2}|0\rangle + e^{i\phi}\sin\frac{\theta}{2}|1\rangle
$$

验证：$\langle X\rangle = r_x = \sin\theta\cos\phi$，$\langle Y\rangle = r_y = \sin\theta\sin\phi$，$\langle Z\rangle = r_z = \cos\theta$。

例如 $\vec{r} = (1, 0, 0)$（$+x$ 方向）：$\theta = \pi/2, \phi = 0$，$|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$。

**9.** 对处于 $|0\rangle$ 的量子比特施加 $R_y(\theta)$ 门，然后测量 $X$。求测量结果为 $|+\rangle$ 的概率。

**解：**

$R_y(\theta) = \cos(\theta/2)I - i\sin(\theta/2)Y$。

$$
R_y(\theta)|0\rangle = \cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle
$$

测量 $X$ 基，测得 $|+\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ 的概率：

$$
P(+) = |\langle +|R_y(\theta)|0\rangle|^2 = \left|\frac{1}{\sqrt{2}}(\langle 0| + \langle 1|)(\cos(\theta/2)|0\rangle + \sin(\theta/2)|1\rangle)\right|^2
$$

$$
= \left|\frac{1}{\sqrt{2}}(\cos\frac{\theta}{2} + \sin\frac{\theta}{2})\right|^2 = \frac{1}{2}\left(\cos\frac{\theta}{2} + \sin\frac{\theta}{2}\right)^2
$$

$$
= \frac{1}{2}\left(1 + 2\sin\frac{\theta}{2}\cos\frac{\theta}{2}\right) = \frac{1 + \sin\theta}{2}
$$

当 $\theta = \pi/2$ 时，$P(+) = (1 + 1)/2 = 1$，即 $R_y(\pi/2)|0\rangle = |+\rangle$，测量 $X$ 必然得到 $|+\rangle$。

**10.** 给定 $|+\rangle$ 态，设计一个测量区分它和 $|-\rangle$，成功概率为多少？

**解：**

$|+\rangle$ 和 $|-\rangle$ 正交（$\langle+|-\rangle = 0$），因此可以用投影测量完美区分。

在 $X$ 基下测量：测量算符为 $\{P_+ = |+\rangle\langle +|, P_- = |-\rangle\langle -|\}$。

- 若态为 $|+\rangle$：测得 $|+\rangle$ 概率为 1，$|-\rangle$ 概率为 0
- 若态为 $|-\rangle$：测得 $|+\rangle$ 概率为 0，$|-\rangle$ 概率为 1

成功概率 $= 100\%$。一般地，任意两个正交纯态都可以用投影测量完美区分。

**11.** 证明时间演化算符的幺正性。

**解：**

时间演化算符 $U(t) = e^{-iHt/\hbar}$，其中 $H$ 是厄米算符（$H^\dagger = H$）。

$$
U^\dagger(t) = (e^{-iHt/\hbar})^\dagger = e^{iH^\dagger t/\hbar} = e^{iHt/\hbar}
$$

$$
U^\dagger(t)U(t) = e^{iHt/\hbar}e^{-iHt/\hbar} = e^0 = I
$$

同理 $U(t)U^\dagger(t) = I$。因此 $U(t)$ 是幺正算符。

物理意义：幺正演化保内积、保概率、保信息——封闭量子系统的演化是可逆的。

**12.** 解释非正交态不可区分性的物理意义。

**解：**

两个非正交态 $|\psi\rangle$ 和 $|\phi\rangle$（$0 < |\langle\phi|\psi\rangle| < 1$）不能被单次测量完美区分。

物理意义：
1. **量子密码学的安全性基础**：窃听者不能完美区分非正交的量子态，因此任何窃听行为都会引入可检测的扰动
2. **信息压缩的极限**：非正交态编码的信息无法被完全提取
3. **量子态识别的不可能**：没有测量可以从单次拷贝中完全确定未知量子态

这一性质蕴含了量子信息与经典信息的根本区别。

---

### 拓展题（13-15题）

**13.** POVM 测量与投影测量有何不同？举例说明 POVM 在量子态区分中的优势。

**解：**

**投影测量**：测量算符 $\{P_m\}$ 满足 $P_m P_n = \delta_{mn} P_m$（正交投影），$\sum_m P_m = I$。

**POVM**：测量算符 $\{E_m\}$ 满足 $E_m \geq 0$，$\sum_m E_m = I$，但不要求正交性。$E_m = M_m^\dagger M_m$，$P(m) = \text{Tr}(E_m \rho)$。

POVM 的优势：当需要区分的态不正交时，POVM 可以在「确定性」和「不确定结论」之间做最优权衡。

**例子**：区分 $|\psi_1\rangle = |0\rangle$ 和 $|\psi_2\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$。

用投影测量无法完美区分。用 POVM：

$$
E_1 = \frac{\sqrt{2}}{1+\sqrt{2}}|1\rangle\langle 1|,\quad
E_2 = \frac{\sqrt{2}}{1+\sqrt{2}}|-\rangle\langle -|,\quad
E_3 = I - E_1 - E_2
$$

$E_3$ 对应"不确定"结论。当态为 $|\psi_1\rangle$ 时，测到 $E_1$ 的概率为 0（因为 $|0\rangle$ 与 $|1\rangle$ 正交），测到 $E_2$ 的概率很小。当态为 $|\psi_2\rangle$ 时相反。POVM 可以给出「结论确定时的错误率为 0」，代价是有时得到"不确定"。

**14.** 一个二能级系统与谐振子耦合，写出总哈密顿量并解释 RWA 近似的适用条件。

**解：**

总哈密顿量（JC 模型）：

$$
H = \frac{\hbar\omega_q}{2}\sigma_z + \hbar\omega_r a^\dagger a + \hbar g(\sigma_+ + \sigma_-)(a + a^\dagger)
$$

展开耦合项：

$$
\sigma_+ a^\dagger: \text{同时激发量子比特和谐振子（能量不守恒，快速振荡）}
$$

$$
\sigma_- a: \text{同时退激发（能量不守恒）}
$$

$$
\sigma_+ a: \text{量子比特激发，谐振子退激发（近共振）}
$$

$$
\sigma_- a^\dagger: \text{量子比特退激发，谐振子激发（近共振）}
$$

在相互作用表象下，前两项以 $e^{\pm i(\omega_q + \omega_r)t}$ 振荡，后两项以 $e^{\pm i(\omega_q - \omega_r)t}$ 振荡。

**RWA 适用条件**：耦合强度 $g$ 远小于失谐 $\Delta = |\omega_q - \omega_r|$，且 $\omega_q + \omega_r$ 远大于 $\omega_q - \omega_r$。在此条件下，快速振荡项在时间平均下贡献可忽略。

在 RWA 下：

$$
H_{\text{RWA}} = \frac{\hbar\omega_q}{2}\sigma_z + \hbar\omega_r a^\dagger a + \hbar g(\sigma_+ a + \sigma_- a^\dagger)
$$

在超导量子比特中，$g/2\pi \sim 100\text{ MHz}$，$\omega_q/2\pi \sim \omega_r/2\pi \sim 5\text{ GHz}$，$\omega_q + \omega_r \sim 10\text{ GHz} \gg g$，RWA 是很好的近似。

**15.** （思考题）"量子测量导致坍缩"是量子力学的公设。有没有不依赖于坍缩的量子力学解释？简要说明多世界解释的观点。

**解：**

有多种不依赖坍缩的解释：

**多世界解释（Everett，1957）**：认为整个宇宙的态矢量始终按照薛定谔方程确定性地演化，不存在坍缩。测量过程被视为观察者与系统之间的纠缠：

1. 初始态：$(|0\rangle + |1\rangle)/\sqrt{2} \otimes |\text{观察者}\rangle$
2. 测量后（幺正演化）：$(|0\rangle|\text{看到0}\rangle + |1\rangle|\text{看到1}\rangle)/\sqrt{2}$
3. 叠加态从未消失——这个世界"分支"了

观察者只感知到一个分支，因此"感觉"发生了坍缩。所有测量结果都在不同的分支中实现。

**其他解释**：
- 隐变量理论（Bohm）：粒子有确定轨迹，由引导方程决定
- 自发定域理论（GRW）：坍缩是真实的物理过程，随机发生
- QBism：波函数是观察者的信念状态，测量是信念更新

每种解释都在实验上等价于标准量子力学——目前没有实验能区分它们。选择哪种解释是一个哲学偏好。
