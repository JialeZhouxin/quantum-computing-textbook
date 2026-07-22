# 习题解答 · 第12章 超导硬件实现与门物理

---

### 基础题（1-6题）

**1.** 约瑟夫森结基本方程。

约瑟夫森方程（约瑟夫森关系）：
- 电流-相位关系：$I = I_c \sin\varphi$
- 电压-相位关系：$V = \frac{\Phi_0}{2\pi}\frac{d\varphi}{dt}$

其中 $\varphi$ 是结两端超导相位差，$\Phi_0 = h/2e$ 是磁通量子，$I_c$ 是临界电流。

约瑟夫森能量：$E_J = \int IV\,dt = \frac{\Phi_0 I_c}{2\pi}(1 - \cos\varphi)$。$E_J = \frac{\Phi_0 I_c}{2\pi}$。

**2.** Transmon vs 电荷量子比特。

Transmon 的主要改进：增大 $E_J/E_C$ 比值（通常 > 50），使电荷能级色散指数衰减。电荷噪声敏感度降低，因为电荷波动引起的频率偏移随 $E_J/E_C$ 增大而指数减小。Transmon 的 $T_1$ 和 $T_2$ 因此大幅提升（从 $\mu$s 到数百 $\mu$s）。

**3.** Transmon 参数计算。

$E_J/h = 20$ GHz，$E_C/h = 400$ MHz，$E_J/E_C = 50$。

**(a)** $\omega_{01}/2\pi \approx \sqrt{8E_J E_C} - E_C = (\sqrt{8 \times 20 \times 0.4} - 0.4)$ GHz $= (\sqrt{64} - 0.4) = 8 - 0.4 = 7.6$ GHz。

**(b)** 非谐性 $\alpha = -E_C$，$\alpha/2\pi = -E_C/h = -400$ MHz。

**(c)** $\pi$ 脉冲：$\Omega_0 t_\pi = \pi$，$t_\pi = \frac{\pi}{\Omega_0} = \frac{\pi}{2\pi \times 40 \times 10^6} = 12.5$ ns。

**4.** RWA。

旋转波近似：在相互作用表象中忽略以 $\omega_d + \omega_{01}$（~10 GHz）快速振荡的项，因为这些项在时间平均下贡献为零。

成立条件：$\Omega_0 \ll \omega_d + \omega_{01}$（拉比频率远小于和频）。在超导量子比特中，$\Omega_0 \sim 10-100$ MHz，$\omega_d + \omega_{01} \sim 10$ GHz，条件满足。

**5.** 虚拟 Z 门。

原理：通过更新控制系统的相位参考系来实现 $Z$ 旋转，无需向量子比特发送物理脉冲。后续 $X$/$Y$ 脉冲的相位自动补偿帧旋转。

"零误差"原因：不涉及物理脉冲，不受幅度/相位噪声影响。局限：当多个量子比特之间存在互作用时，帧更新不能独立进行（需要物理实现）。

**6.** CZ 门目标。

CZ 门在计算基下的效果：对 $|11\rangle$ 施加 $\pi$ 相位，其他态不变。

矩阵表示：$\text{CZ} = \begin{pmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&-1\end{pmatrix}$

物理实现核心：让两个量子比特的 $|11\rangle$ 态通过耦合获得一个额外的动态相位 $\pi$，同时保证 $|01\rangle$、$|10\rangle$ 不变。

---

### 提高题（7-11题）

**7.** $T_1 = 80$ μs，$T_2 = 100$ μs。

$1/T_2 = 1/(2T_1) + 1/T_\varphi$，所以 $1/T_\varphi = 1/T_2 - 1/(2T_1) = 1/100 - 1/160 = 1/266.7$ μs$^{-1}$。

$T_\varphi \approx 267$ μs。

20 ns X 门的 T1 保真度损失：$\epsilon_{T1} \approx t_g/(3T_1) = 20$ ns $/ (3 \times 80$ μs$) = 8.3 \times 10^{-5}$。

**8.** 拉比振荡失谐分析。

$\frac{\Omega_0^2}{\Omega_0^2 + \Delta^2} = 0.6$，$\Delta = \omega_d - \omega_{01} = 30$ MHz。

$\Omega_0^2 = 0.6\Omega_0^2 + 0.6\Delta^2$，$0.4\Omega_0^2 = 0.6 \times 900$，$\Omega_0^2 = 1350$，$\Omega_0 \approx 36.7$ MHz。

量子比特频率 $\omega_{01}/2\pi = 5.00 - 0.03 = 4.97$ GHz（或 $5.00 + 0.03 = 5.03$ GHz，取决于驱动频率在共振频率的哪一侧）。

**9.** DRAG 脉冲。

标准高斯脉冲 $\Omega_x(t)$ 的频谱旁瓣会激发 $|1\rangle \to |2\rangle$ 跃迁。DRAG 在 $y$ 分量上加入与导数成正比的修正：

$\Omega_y(t) \propto \frac{\dot{\Omega}_x(t)}{\alpha}$

其中 $\alpha$ 是非谐性。修正项在 $|1\rangle \to |2\rangle$ 跃迁频率处产生反相位的驱动，抵消泄漏。

**10.** CZ 门绝热条件。

绝热条件：$\frac{|\langle m|\dot{H}|n\rangle|}{(E_m - E_n)^2} \ll 1$

物理含义：系统哈密顿量的变化速度远小于能级间隙。在 CZ 门中，量子比特频率在脉冲期间被调谐接近，必须缓慢穿过避免交叉，确保系统始终处于瞬时本征态（不发生到非计算能级的 Landau-Zener 跃迁）。

**11.** 频率拥挤。

产生原因：多个量子比特的工作频率因工艺涨落而分散在一个窄带内，导致相邻量子比特的频率接近，产生 ZZ 串扰和微波串扰。

缓解方法：
1. **宽带设计**：增大 Transmon 的非谐性，减少频率碰撞
2. **精确制备**：通过精确的腔体设计控制频率散布
3. **频率分配算法**：在初始校准中为每个量子比特分配最优频率，最小化碰撞
4. **可调耦合器**：通过调谐耦合器来补偿固定频率的不足

---

### 综合题（12-15题）

**12.** CZ 门校准。

$\theta_{CZ} = 0.05 d^2 = \pi$，$d = \sqrt{\pi/0.05} \approx \sqrt{62.83} \approx 7.93$ GHz。

门时间 80 ns。绝热参数：最小能级间隙 $g_{\min}/h = 80$ MHz。

绝热条件要求 $d/dt(\text{调谐}) \ll g_{\min}^2/\hbar$。估算：$80$ ns 内调谐 7.93 GHz，速度快约为 $10^{17}$ Hz/s。$g_{\min}^2/\hbar \sim (2\pi \times 80\text{ MHz})^2/h \sim 10^{17}$。处于边缘——需要更慢或更小的间隙。

**13.** 16 比特芯片校准流程。

1. **频谱扫描**：对所有 16 个量子比特做光谱学，确定频率
2. **读取校准**：调整读出腔频率和功率，优化 IQ 平面分离度
3. **拉比振荡**：确定每个比特的 $\pi$ 脉冲长度
4. **Ramsey 干涉**：测量 $T_2^*$
5. **$T_1$ 测量**：测量能量弛豫时间
6. **单比特 RB**：测量平均单比特门保真度
7. **两比特门校准**：对相邻比特对校准 CZ/CZ 门（条件相位扫描）
8. **两比特 RB**：测量两比特门保真度
9. **串扰检测**：检测相邻比特操作之间的串扰
10. **读出校准**：校准读出误差矩阵
11. **运行验证电路**：运行简单的量子线路（如 Bell 态制备）验证整体性能

**14.** 旋转框架推导。

实验室框架哈密顿量：
$H_{\text{lab}} = -\frac{\hbar\omega_{01}}{2}\sigma_z + \hbar\Omega_0\cos(\omega_d t)\sigma_x$

旋转框架变换：$U = e^{-i\omega_d t\sigma_z/2}$，$|\tilde{\psi}\rangle = U|\psi\rangle$。

$\tilde{H} = U H_{\text{lab}} U^\dagger - i\hbar U\dot{U}^\dagger$

$U\dot{U}^\dagger = -i\frac{\omega_d}{2}\sigma_z$

$\tilde{H} = -\frac{\hbar(\omega_{01} - \omega_d)}{2}\sigma_z + \hbar\Omega_0\cos(\omega_d t)(e^{-i\omega_d t\sigma_z/2}\sigma_x e^{i\omega_d t\sigma_z/2})$

展开余弦并用旋转框架下的 $\sigma_x$ 变换：$\cos(\omega_d t)\sigma_x \to \frac12(\sigma_+ e^{i\omega_d t} + \sigma_- e^{-i\omega_d t})\cdot(e^{i\omega_d t} + e^{-i\omega_d t})$

忽略 $e^{\pm i(\omega_d + \omega_{01})t}$ 项（RWA），只保留近共振项：

$\tilde{H} \approx -\frac{\hbar\Delta}{2}\sigma_z + \frac{\hbar\Omega_0}{2}\sigma_x$

其中 $\Delta = \omega_{01} - \omega_d$。共振时 $\Delta = 0$：$\tilde{H} = \frac{\hbar\Omega_0}{2}\sigma_x$。

**15.** 保真度提升到 99.99%。

**器件角度**：提升介电质量（减少 TLS 缺陷），改进约瑟夫森结制备工艺降低准粒子密度。
**控制角度**：使用更低相位噪声的 AWG，采用实时反馈控制补偿低频漂移，优化脉冲整形进一步抑制泄漏。
**校准角度**：机器学习驱动的自动校准，在线自适应调优，门串扰的实时补偿。
