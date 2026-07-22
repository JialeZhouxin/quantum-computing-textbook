# 习题解答 · 第7章 量子比特与单比特门

---

### ★ 基础题（第1-8题）

**1.** 判断并归一化态矢量。

**(a)** $|\psi\rangle = \frac13|0\rangle + \frac23|1\rangle$

范数 $= \sqrt{(1/3)^2 + (2/3)^2} = \sqrt{1/9 + 4/9} = \sqrt{5/9} \neq 1$ → 不合法。

归一化：$|\psi'\rangle = \frac{1}{\sqrt{5}}(|0\rangle + 2|1\rangle)$

**(b)** $|\psi\rangle = \frac{1}{\sqrt{3}}|0\rangle + \sqrt{\frac{2}{3}}|1\rangle$

范数 $= \sqrt{1/3 + 2/3} = 1$ → 合法。

**(c)** $|\psi\rangle = \frac{1+i}{2}|0\rangle + \frac12|1\rangle$

$|(1+i)/2|^2 = (1+1)/4 = 1/2$，$|1/2|^2 = 1/4$，和为 $3/4 \neq 1$ → 不合法。

归一化：乘以 $2/\sqrt{3}$：$|\psi'\rangle = \frac{1+i}{\sqrt{3}}|0\rangle + \frac{1}{\sqrt{3}}|1\rangle$

**(d)** $|\psi\rangle = 0.6|0\rangle + 0.8i|1\rangle$

$|0.6|^2 + |0.8i|^2 = 0.36 + 0.64 = 1$ → 合法。

**2.** 布洛赫球面坐标 $(\theta, \varphi)$。

一般形式：$|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\varphi}\sin(\theta/2)|1\rangle$

**(a)** $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$：$\cos(\theta/2) = \sin(\theta/2) = 1/\sqrt{2} \to \theta = \pi/2$，$e^{i\varphi} = 1 \to \varphi = 0$。$(\theta, \varphi) = (\pi/2, 0)$。

**(b)** $\frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$：$\theta = \pi/2$，$e^{i\varphi} = -i = e^{-i\pi/2} \to \varphi = 3\pi/2$。$(\theta, \varphi) = (\pi/2, 3\pi/2)$。

**(c)** $\frac{\sqrt{3}}{2}|0\rangle + \frac12|1\rangle$：$\cos(\theta/2) = \sqrt{3}/2 \to \theta/2 = \pi/6 \to \theta = \pi/3$，$e^{i\varphi} = 1 \to \varphi = 0$。$(\theta, \varphi) = (\pi/3, 0)$。

**(d)** $0.8|0\rangle + 0.6i|1\rangle$：$\cos(\theta/2) = 0.8 \to \theta/2 = \arccos(0.8) \approx 0.6435 \to \theta \approx 1.287$ rad，$e^{i\varphi} = i = e^{i\pi/2} \to \varphi = \pi/2$。$(\theta, \varphi) \approx (1.287, \pi/2)$。

**3.** 门作用在给定态上的结果。

**(a)** $X|+\rangle = X\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = \frac{1}{\sqrt{2}}(|1\rangle + |0\rangle) = |+\rangle$。$|+\rangle$ 是 $X$ 的本征态（本征值 $+1$）。

**(b)** $Z|-\rangle = Z\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$。$|-\rangle$ 不是 $Z$ 的本征态。

**(c)** $H|-\rangle = \frac{1}{\sqrt{2}}[ (|0\rangle + |1\rangle) - (|0\rangle - |1\rangle) ] / \sqrt{2} = \frac{1}{2}(|0\rangle + |1\rangle - |0\rangle + |1\rangle) = |1\rangle$。

**(d)** $S|+\rangle = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix} \frac{1}{\sqrt{2}}\begin{pmatrix}1\\1\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1\\ i\end{pmatrix} = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$。在 $xy$ 平面旋转 $90^\circ$。

**4.** 投影测量概率。

**(a)** $|-\rangle$ 在 $Z$ 基：$P(0) = |\langle 0|-\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$，$P(1) = 1/2$。

**(b)** $|+\rangle$ 在 $X$ 基：$P(+) = |\langle+|+\rangle|^2 = 1$，$P(-) = 0$。$|+\rangle$ 是 $X$ 的本征态。

**(c)** $|0\rangle$ 在 $Y$ 基：$|+\rangle_Y = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)$，$|-\rangle_Y = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$。
$P(+_Y) = |_Y\langle+|0\rangle|^2 = |1/\sqrt{2}|^2 = 1/2$，$P(-_Y) = 1/2$。

**(d)** $\frac{1}{\sqrt{2}}(|0\rangle + e^{i\pi/4}|1\rangle)$ 在 $X$ 基：
$\langle+|\psi\rangle = \frac{1}{2}(1, 1)\cdot(1, e^{i\pi/4}) = \frac{1}{2}(1 + e^{i\pi/4})$
$P(+) = (1/4)|1 + e^{i\pi/4}|^2 = (1/4)(2 + 2\cos(\pi/4)) = (1 + 1/\sqrt{2})/2 \approx 0.854$
$P(-) = 1 - P(+) \approx 0.146$

**5.** 验证恒等式。

**(a)** $HSH = R_x(\pi/2)$（忽略全局相位）：

$HSH = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}1&0\\0&i\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac12\begin{pmatrix}1&i\\1&-i\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = \frac12\begin{pmatrix}1+i&1-i\\1-i&1+i\end{pmatrix}$

$R_x(\pi/2) = \cos(\pi/4)I - i\sin(\pi/4)X = \frac{1}{\sqrt{2}}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$

两者相差全局相位 $e^{i\pi/4}$，验证成立。

**(b)** $XR_y(\theta)X = R_y(-\theta)$：

$XR_y(\theta)X = X(\cos(\theta/2)I - i\sin(\theta/2)Y)X = \cos(\theta/2)I - i\sin(\theta/2) XYX$

$XYX = Y$（因为 $X$ 与 $Y$ 反对易：$XY = -YX$，$XYX = -YXX = -Y$）唔，检查：$XYX = X(YX) = X(-XY) = -(X^2)Y = -Y$。

所以 $XR_y(\theta)X = \cos(\theta/2)I + i\sin(\theta/2)Y = R_y(-\theta)$。

**(c)** $S^\dagger = S^3$：

$S = \text{diag}(1, i)$，$S^\dagger = \text{diag}(1, -i)$。
$S^3 = \text{diag}(1, i^3) = \text{diag}(1, -i) = S^\dagger$。成立。

**6.** $R_x(\pi/2)|0\rangle$ 和 $R_y(\pi/2)|0\rangle$。

$R_x(\pi/2) = \frac{1}{\sqrt{2}}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$，$R_x(\pi/2)|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)$。

布洛赫球：从北极（$|0\rangle$）绕 $x$ 轴转 $90^\circ$ 到 $xy$ 平面的 $-y$ 方向。

$R_y(\pi/2) = \frac{1}{\sqrt{2}}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$，$R_y(\pi/2)|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = |+\rangle$。

布洛赫球：从北极绕 $y$ 轴转 $90^\circ$ 到 $+x$ 方向。

**7.** $\langle\psi|X|\psi\rangle$，$|\psi\rangle = \frac{1}{\sqrt{2}}(|0\rangle + e^{i\theta}|1\rangle)$。

$\langle\psi|X|\psi\rangle = \frac12(1, e^{-i\theta})\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1\\ e^{i\theta}\end{pmatrix} = \frac12(1, e^{-i\theta})\begin{pmatrix}e^{i\theta}\\1\end{pmatrix} = \frac{e^{i\theta} + e^{-i\theta}}{2} = \cos\theta$

$\theta$ 从 $0$ 到 $2\pi$：$\cos\theta$ 从 $1$ 减小到 $-1$ 再回到 $1$——布洛赫向量在 $xz$ 平面绕 $z$ 轴旋转。

**8.** $R_z(\theta) = \begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}$（Z 旋转的标准定义）。

$R_z(\theta_1)R_z(\theta_2) = \begin{pmatrix}e^{-i\theta_1/2}&0\\0&e^{i\theta_1/2}\end{pmatrix}\begin{pmatrix}e^{-i\theta_2/2}&0\\0&e^{i\theta_2/2}\end{pmatrix} = \begin{pmatrix}e^{-i(\theta_1+\theta_2)/2}&0\\0&e^{i(\theta_1+\theta_2)/2}\end{pmatrix} = R_z(\theta_1 + \theta_2)$

---

### ★★ 计算题（第9-14题）

**9.** Z-Y 分解 $H = e^{i\alpha}R_z(\beta)R_y(\gamma)R_z(\delta)$。

$H = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$，$\det H = -1$。调整相位使行列式为 1：$H' = e^{i\pi/2}H = \frac{1}{\sqrt{2}}\begin{pmatrix}i&i\\i&-i\end{pmatrix}$。

展开 $R_z(\beta)R_y(\gamma)R_z(\delta)$：
$$
\begin{pmatrix}e^{-i\beta/2}&0\\0&e^{i\beta/2}\end{pmatrix}
\begin{pmatrix}\cos(\gamma/2)&-\sin(\gamma/2)\\\sin(\gamma/2)&\cos(\gamma/2)\end{pmatrix}
\begin{pmatrix}e^{-i\delta/2}&0\\0&e^{i\delta/2}\end{pmatrix}
$$
比较参数可得一个解：
$\alpha = \pi/2$，$\beta = \pi/2$，$\gamma = \pi/2$，$\delta = 0$。

验证：$e^{i\pi/2}R_z(\pi/2)R_y(\pi/2)R_z(0) = i\begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1&-1\\1&1\end{pmatrix}$
$= \frac{i}{\sqrt{2}}\begin{pmatrix}e^{-i\pi/4}&-e^{-i\pi/4}\\e^{i\pi/4}&e^{i\pi/4}\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} = H$

**10.** $HR_z(\theta)H = R_x(\theta)$。

$HR_z(\theta)H = \frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}\begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}$

$= \frac12\begin{pmatrix}e^{-i\theta/2}&e^{i\theta/2}\\e^{-i\theta/2}&-e^{i\theta/2}\end{pmatrix}\begin{pmatrix}1&1\\1&-1\end{pmatrix}
= \frac12\begin{pmatrix}e^{-i\theta/2}+e^{i\theta/2}&e^{-i\theta/2}-e^{i\theta/2}\\e^{-i\theta/2}-e^{i\theta/2}&e^{-i\theta/2}+e^{i\theta/2}\end{pmatrix}$
$= \begin{pmatrix}\cos(\theta/2)&-i\sin(\theta/2)\\-i\sin(\theta/2)&\cos(\theta/2)\end{pmatrix} = R_x(\theta)$

$HTH$：$T = \begin{pmatrix}1&0\\0&e^{i\pi/4}\end{pmatrix} = R_z(\pi/4)$（差一全局相位）。
$HTH = HR_z(\pi/4)H = R_x(\pi/4)$。

**11.** $R_z(\pi/2)R_x(\pi/2)R_z(\pi/2)$。

**(a)** 矩阵形式：
$R_z(\pi/2) = \begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}$，$R_x(\pi/2) = \frac{1}{\sqrt{2}}\begin{pmatrix}1&-i\\-i&1\end{pmatrix}$。

先计算 $R_x(\pi/2)R_z(\pi/2) = \frac{1}{\sqrt{2}}\begin{pmatrix}e^{-i\pi/4}&-ie^{i\pi/4}\\-ie^{-i\pi/4}&e^{i\pi/4}\end{pmatrix}$

再乘左 $R_z(\pi/2)$：
$U = \begin{pmatrix}e^{-i\pi/4}&0\\0&e^{i\pi/4}\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}e^{-i\pi/4}&-ie^{i\pi/4}\\-ie^{-i\pi/4}&e^{i\pi/4}\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}e^{-i\pi/2}&-i\\-i&e^{i\pi/2}\end{pmatrix} = \frac{1}{\sqrt{2}}\begin{pmatrix}-i&-i\\-i&i\end{pmatrix}$

**(b)** $U = \frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\1&-1\end{pmatrix} \cdot (-i) = -iH$。不计全局相位 $-i$，等于 $H$ 门。

**(c)** 布洛赫球：$R_z(\pi/2)$ 绕 $z$ 转 $90^\circ$，$R_x(\pi/2)$ 绕 $x$ 转 $90^\circ$，再 $R_z(\pi/2)$ 绕 $z$ 转 $90^\circ$。净效果是一个绕 $(\hat{x}+\hat{z})/\sqrt{2}$ 轴旋转 $\pi$——即 $H$ 门。

**12.** 任意单比特门 $U$ 的 Z-Y 分解定理：$U = e^{i\alpha}R_z(\phi)R_x(\theta)R_z(\psi)$。

证明：$R_z(\phi)R_x(\theta)R_z(\psi) = \begin{pmatrix}e^{-i\phi/2}&0\\0&e^{i\phi/2}\end{pmatrix}\begin{pmatrix}\cos(\theta/2)&-i\sin(\theta/2)\\-i\sin(\theta/2)&\cos(\theta/2)\end{pmatrix}\begin{pmatrix}e^{-i\psi/2}&0\\0&e^{i\psi/2}\end{pmatrix}$

$= \begin{pmatrix}e^{-i(\phi+\psi)/2}\cos(\theta/2) & -i e^{-i(\phi-\psi)/2}\sin(\theta/2) \\ -i e^{i(\phi-\psi)/2}\sin(\theta/2) & e^{i(\phi+\psi)/2}\cos(\theta/2)\end{pmatrix}$

任意 $U \in SU(2)$ 可写为 $U = \begin{pmatrix}a & b \\ -b^* & a^*\end{pmatrix}$。取 $\theta/2 = \arccos(|a|)$，$\phi = -\arg(a) - \arg(b)$，$\psi = -\arg(a) + \arg(b)$ 即可匹配。加上全局相位 $e^{i\alpha}$ 可覆盖 $U(2)$。

**13.** 相位帧跟踪。

初始帧：0

- 物理 $R_x(\pi/2)$：帧不变（帧跟踪只在虚拟 Z 门时更新）
- 虚拟 $R_z(\pi/3)$：帧更新为 $-\pi/3$ 或等价地 $\pi/3$ 虚旋转。累积帧 $= \pi/3$
- 物理 $R_x(\pi/2)$：此时实际做的 $X$ 旋转的相位根据帧调整。等价于在全局旋转 $R_x(\pi/2)$ 之前插入了相位偏移
- 虚拟 $R_z(\pi/4)$：帧更新。累积帧 $= \pi/3 + \pi/4 = 7\pi/12$
- 物理 $R_x(\pi/2)$：同上

总帧偏移 $= \pi/3 + \pi/4 = 7\pi/12$。

**(b)** 净幺正算符：
$U = R_z(7\pi/12) R_x(\pi/2) R_z(-7\pi/12) R_z(7\pi/12) R_x(\pi/2) R_z(-7\pi/12) R_z(\pi/3+\pi/4) ...$

简化：三个物理 $R_x(\pi/2)$ 的净效果是 $R_x(3\pi/2) = -iX$。加上帧旋转的虚 Z 门，总效果是绕 $x$ 轴旋转 $3\pi/2$。

**14.** 拉比频率 $\Omega = 2\pi \times 30$ MHz。

**(a)** $\pi$ 脉冲：$\Omega t_\pi = \pi$，$t_\pi = \frac{\pi}{2\pi \times 30 \times 10^6} = \frac{1}{60 \times 10^6} \approx 16.7$ ns。

**(b)** $R_x(\pi/3)$：$\Omega t = \pi/3$，$t = \frac{\pi/3}{2\pi \times 30 \times 10^6} = \frac{1}{180 \times 10^6} \approx 5.56$ ns。

**(c)** 高斯脉冲：$\Omega(t) = \Omega_0 e^{-t^2/2\sigma^2}$，面积 $A = \int_{-\infty}^{\infty}\Omega(t)dt = \Omega_0 \sigma \sqrt{2\pi}$。

令 $A = \pi$：$\sigma \sqrt{2\pi} \cdot 2\pi \times 30 \times 10^6 = \pi$。

$\sigma = \frac{\pi}{2\pi \times 30 \times 10^6 \cdot \sqrt{2\pi}} = \frac{1}{60 \times 10^6 \cdot \sqrt{2\pi}} \approx 6.65$ ns。

---

### ★★★ 综合题（第15-18题）

**15.** 欧拉分解证明。

$U = \begin{pmatrix}a & b \\ -b^* & a^*\end{pmatrix}$，$|a|^2 + |b|^2 = 1$。

$R_z(\beta)R_y(\gamma)R_z(\delta) = \begin{pmatrix}e^{-i(\beta+\delta)/2}\cos(\gamma/2) & -e^{-i(\beta-\delta)/2}\sin(\gamma/2) \\ e^{i(\beta-\delta)/2}\sin(\gamma/2) & e^{i(\beta+\delta)/2}\cos(\gamma/2)\end{pmatrix}$

参数匹配：
$\gamma$ 由 $|a|$ 决定：$\cos(\gamma/2) = |a|$，$\gamma = 2\arccos(|a|)$。
$\beta + \delta = -2\arg(a)$，$\beta - \delta = -2\arg(b) - \pi$。
解出 $\beta$ 和 $\delta$。加上全局相位 $\alpha = 0$（因 $\det U = 1$）。

**16.** DRAG 原理。

**(a)** 高斯脉冲 $\Omega(t) = \Omega_0 e^{-t^2/2\sigma^2}$，频谱 $\tilde{\Omega}(\omega) \propto e^{-\omega^2\sigma^2/2}$。$\pi$ 脉冲的带宽 $\sim 1/\sigma$。旁瓣在 $\omega \approx \pm 2\pi/\sigma$ 处仍有显著功率。当频谱在 $\omega_q + \alpha$（$|1\rangle \leftrightarrow |2\rangle$ 跃迁）处有足够功率时，会激发泄漏。

$\alpha = -300$ MHz，旁瓣在 $\omega = 2\pi \times 300$ MHz 处的功率比中心低 $\exp(-2\pi^2\sigma^2 f^2)$。

**(b)** 标准脉冲只使用 $x$ 分量驱动 $|0\rangle \leftrightarrow |1\rangle$ 跃迁。DRAG 添加与 $\dot{\Omega}_x$ 成正比的 $y$ 分量：$\Omega_y(t) \propto \dot{\Omega}_x(t)$。这会有效"消去"在 $|1\rangle \leftrightarrow |2\rangle$ 能级上的布居，因为附加的 $y$ 分量产生破坏性干涉。

**(c)** 更快的门 $\to$ 更短的 $\sigma \to$ 更宽的频谱 $\to$ 更多的 $|2\rangle$ 泄漏。DRAG 主动抵消泄漏，允许在给定泄漏容忍度下使用更短的脉冲（更高的速度）。

**17.** 随机基准测试。

| $m$ | $P(0)$ |
|:---:|:---:|
| 1 | 0.992 |
| 2 | 0.984 |
| 4 | 0.968 |
| 8 | 0.940 |
| 16 | 0.880 |
| 32 | 0.780 |
| 64 | 0.620 |

**(a)** 拟合 $P(0) = A p^m + B$。$m \to \infty$ 时 $P(0) \to B$（均匀分布 $B=0.5$）。

取 $m=1$：$0.992 = Ap + 0.5 \implies Ap = 0.492$
$m=64$：$0.620 = A p^{64} + 0.5 \implies A p^{64} = 0.120$

$p^{63} = 0.120/0.492 \approx 0.244$，$p = (0.244)^{1/63} \approx 0.978$。

$A = 0.492/p \approx 0.503$。

**(b)** 平均门保真度 $F_{\text{avg}} = 1 - (1-p)/2 \approx 1 - (1 - 0.978)/2 = 1 - 0.011 = 0.989$。

**18.** 综合。

**(a)** $U = \frac{1}{\sqrt{2}}\begin{pmatrix}1&-i\\-i&1\end{pmatrix} = R_x(\pi/2)$。

**(b)** 欧拉 Z-Y 分解：查 Z-Y 分解表知 $R_x(\pi/2) = e^{i\pi/4}R_z(-\pi/2)R_y(\pi/2)R_z(\pi/2)$。
或直接用：$R_x(\pi/2) = R_z(-\pi/2)R_y(\pi/2)R_z(\pi/2)$（差全局相位）。

**(c)** 物理实现方案：
- 物理 $R_y(\pi/2)$ 脉冲：$\Omega = 2\pi \times 40$ MHz，$t = \pi/(2\Omega) = 6.25$ ns
- 虚拟 $R_z(-\pi/2)$：帧跟踪，无需实际脉冲
- 虚拟 $R_z(\pi/2)$：帧跟踪

**(d)** 如果虚拟 $Z$ 门有 $1\%$ 角度误差，则 $R_z(\pi/2)$ 变为 $R_z(0.505\pi)$。与理想门的保真度损失可由迹距离估算。对于 $1\%$ 的小角度误差，门保真度损失约 $(\delta\theta)^2/4 \approx (0.01 \times \pi/2)^2/4 \approx 6 \times 10^{-5}$。这是一个很小的误差——虚拟 Z 门的精确性（不受物理脉冲噪声影响）是其优势。
