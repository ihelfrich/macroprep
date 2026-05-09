Notation: bars over autonomous variables ($\overline{C_0}, \overline{T}, \overline{I}, \overline{G}, \overline{X}, \overline{M}$). MPC $= c$. $K_X = \Delta Y^* / \Delta\overline{X}$. $rrr$ is the required reserve ratio. Money multiplier $K_S = 1/rrr$. Exchange rate $E_{\$/\pounds}$ is dollars per pound.

---

## 1. CPI / Inflation Calculation

### Q1.1 (Easy)
A two-good basket has 8 units of bread and 5 units of coffee. Base-year (2020) prices: bread \$3, coffee \$5. In 2023 prices are bread \$4, coffee \$6. Compute CPI for 2023.

**Solution.** Cost of base basket at 2020 prices $= 8(3) + 5(5) = 49$. Cost at 2023 prices $= 8(4) + 5(6) = 62$.
$$\text{CPI}_{2023} = \frac{62}{49}\cdot 100 \approx 126.5.$$

**Key insight.** Quantities are frozen at base-year levels — only re-price.

### Q1.2 (Easy)
Given CPI$_{2022}$ = 110 and CPI$_{2023}$ = 121, compute the inflation rate from 2022 to 2023.

**Solution.**
$$\pi = \frac{121 - 110}{110}\cdot 100 = 10.0\%.$$

**Key insight.** The earlier CPI is always the denominator.

### Q1.3 (Medium)
Basket: 20 units of $A$, 10 units of $B$. Prices $(P_A, P_B)$: 2021 (\$1, \$4), 2022 (\$1.20, \$4.50), 2023 (\$1.50, \$5). Base = 2021. Compute CPI for each year and the 2022→2023 inflation rate.

**Solution.** Base cost $= 20(1) + 10(4) = 60$. CPI$_{2021} = 100$.
2022 cost $= 20(1.20) + 10(4.50) = 69$. CPI$_{2022} = 69/60 \cdot 100 = 115$.
2023 cost $= 20(1.50) + 10(5) = 80$. CPI$_{2023} = 80/60 \cdot 100 \approx 133.33$.
$$\pi_{22\to 23} = \frac{133.33 - 115}{115}\cdot 100 \approx 15.94\%.$$

**Key insight.** Compute the level (CPI), then the percentage change between adjacent levels.

### Q1.4 (Medium)
The base year is 2015. CPI$_{2018}$ = 108, CPI$_{2022}$ = 135. Compute the cumulative inflation from 2018 to 2022 and the average annual rate.

**Solution.** Cumulative: $(135 - 108)/108 = 25\%$. Annualized: $(1.25)^{1/4} - 1 \approx 5.74\%$.

**Key insight.** Cumulative percentage change is not the sum of annual rates — compound it.

### Q1.5 (Medium)
Base 2020 (CPI = 100). CPI$_{2021}$ = 105, CPI$_{2023}$ = 120. Find inflation from 2021 to 2023. Why isn't it 15%?

**Solution.**
$$\pi_{21\to 23} = \frac{120 - 105}{105}\cdot 100 \approx 14.29\%.$$
Subtracting CPI levels (120 − 105 = 15) gives a percentage-point change in the index, not an inflation rate.

**Key insight.** Inflation = percentage change, with the earlier period as the denominator. The base year fixes the level, not the rate.

### Q1.6 (Hard)
A consumer's grocery basket prices rise from \$200 to \$220, but they substitute cheaper items so their actual outlay only rises to \$210. CPI uses fixed quantities. By what percent does CPI overstate the consumer's true cost increase?

**Solution.** CPI inflation $= (220 - 200)/200 = 10\%$. True cost-of-living change $= (210 - 200)/200 = 5\%$. CPI overstates by $10 - 5 = 5$ percentage points (a factor of 2).

**Key insight.** CPI is Laspeyres — fixed base-year quantities — so it ignores substitution and overstates inflation.

### Q1.7 (Hard)
The implicit GDP price deflator (IGDPDI) uses Paasche weights (current-year quantities, base-year prices in the denominator). Explain why IGDPDI typically *underestimates* inflation while CPI *overestimates* it.

**Solution.** Paasche weights are heavy on goods consumers currently buy a lot of — those are the goods whose prices have risen *least* (consumers substituted toward them). Weighting low-inflation goods more heavily understates inflation. CPI does the reverse, weighting yesterday's basket which was tilted toward goods that have since become expensive.

**Key insight.** Index weights bias the result. Laspeyres (CPI) overstates; Paasche (IGDPDI) understates. The truth is in between (Fisher).

### Q1.8 (Hard)
Nominal GDP rose 7% from 2022 to 2023. The GDP deflator rose 4%. What was real GDP growth?

**Solution.**
$$1 + g_{\text{real}} = \frac{1 + g_{\text{nom}}}{1 + \pi} = \frac{1.07}{1.04} \approx 1.0288.$$
Real growth $\approx 2.88\%$. (Approximation $7 - 4 = 3\%$ is close but not exact.)

**Key insight.** Real growth is the *ratio*, not the difference. Approximation is okay for small rates.

### Q1.9 (Twist)
The basket above has 8 units of bread and 5 units of coffee. Bread doubles from \$3 to \$6 between 2020 and 2023. Coffee falls from \$5 to \$2. Compute CPI$_{2023}$ (base 2020). Is inflation positive?

**Solution.** Base $= 8(3) + 5(5) = 49$. 2023 $= 8(6) + 5(2) = 58$. CPI $= 58/49 \cdot 100 \approx 118.4$. Inflation $\approx 18.4\%$ — yes positive, even though one good's price fell sharply.

**Key insight.** CPI is a weighted average. A big rise in one good can outweigh a fall in another depending on base-year quantity weights.

### Q1.10 (Twist)
The Bureau says 2024 CPI = 130 (base = 2019, where CPI = 100). A 2024 worker earns \$60,000 nominal. What is the real wage in 2019 dollars?

**Solution.** Real wage $= 60{,}000 / 1.30 \approx \$46{,}154$.

**Key insight.** To deflate, divide by (CPI / 100). Levels of CPI tell you the price-level ratio between current and base year.

### Q1.11 (Twist)
A union contract pegs nominal wages to lagged CPI: $W_t = W_{t-1} \cdot (\text{CPI}_{t-1} / \text{CPI}_{t-2})$. If actual inflation accelerates from 3% to 8% between $t-1$ and $t$, what happens to the real wage at time $t$?

**Solution.** Nominal wage rises 3% (lagged inflation). Prices rise 8%. Real wage falls by approximately $3 - 8 = -5\%$.

**Key insight.** Lagged indexation hurts workers when inflation accelerates and helps when inflation decelerates.

---

## 2. Unemployment Definitions and Computation

### Q2.1 (Easy)
A country has 120 million employed and 8 million unemployed. Compute the unemployment rate.

**Solution.**
$$u = \frac{U}{E + U} = \frac{8}{120 + 8} = \frac{8}{128} = 6.25\%.$$

**Key insight.** $u$ uses the labor force ($E + U$) in the denominator, not total population.

### Q2.2 (Easy)
Population = 200 million; labor force = 150 million; employed = 142.5 million. Compute the participation rate and the unemployment rate.

**Solution.** Participation $= LF/\text{Pop} = 150/200 = 75\%$. $U = 150 - 142.5 = 7.5$. $u = 7.5/150 = 5\%$.

**Key insight.** Participation has population in the denominator; unemployment has the labor force.

### Q2.3 (Easy)
Distinguish frictional, structural, and cyclical unemployment with one example each.

**Solution.** Frictional: a recent college graduate searching for a first job. Structural: a coal miner whose industry is shrinking permanently. Cyclical: a construction worker laid off during a recession.

**Key insight.** Natural rate $= $ frictional $+$ structural. Cyclical disappears in expansions.

### Q2.4 (Medium)
A discouraged worker stops looking for work and exits the labor force. Holding employment fixed, does the measured unemployment rate rise, fall, or stay the same?

**Solution.** $U$ falls by 1, $LF$ falls by 1, $E$ unchanged. New $u = (U-1)/(E + U - 1)$, smaller than the old $u = U/(E+U)$. The rate **falls** even though the labor market hasn't actually improved.

**Key insight.** The unemployment rate has a known bias: it can fall just because people give up.

### Q2.5 (Medium)
$E = 95$, $U = 5$, not-in-labor-force $= 50$. 5 of the not-in-labor-force decide to start looking for work and remain unemployed. What are the new $u$ and participation rate?

**Solution.** New $U = 10$, $LF = 105$, Pop $= 150$. $u = 10/105 \approx 9.5\%$. Participation $= 105/150 = 70\%$ (was $100/150 \approx 66.7\%$).

**Key insight.** Re-entrants raise both the numerator of $u$ and the labor force; effect on $u$ depends on which dominates.

### Q2.6 (Medium)
Natural rate $= 4\%$. Actual $u = 7\%$. Decompose if frictional is 2% and structural is 2%.

**Solution.** Cyclical $= u - $ natural $= 7 - 4 = 3\%$.

**Key insight.** Cyclical unemployment is the recession-driven gap above the natural rate.

### Q2.7 (Hard)
Define the U-6 measure (broad unemployment) conceptually and explain why U-6 > U-3 always.

**Solution.** U-3 (the headline rate) counts only people actively searching. U-6 adds discouraged workers, marginally attached, and part-time-for-economic-reasons workers. Each addition raises both numerator and an inclusive denominator, but the numerator grows by more, so U-6 > U-3.

**Key insight.** Headline $u$ undercounts labor-market slack. U-6 is closer to a "true" idle-capacity measure.

### Q2.8 (Hard)
A factory closes, displacing 1,000 workers. 600 retrain and find new jobs in 6 months. 300 are still searching after 12 months. 100 leave the labor force. After 12 months, what is the contribution to (a) frictional, (b) structural, (c) measured $u$?

**Solution.** (a) Frictional ≈ 0 (none searching short-term). (b) Structural ≈ 300 (long-term displaced). (c) Measured $u$ contribution: 300 unemployed; the 100 who left labor force don't appear in $u$.

**Key insight.** Long unemployment durations get classified as structural; exits to non-participation don't move the headline rate.

### Q2.9 (Twist)
Country A: $E = 90$, $U = 10$, not-in-LF $= 100$. Country B: $E = 90$, $U = 10$, not-in-LF $= 50$. Both have $u = 10\%$. Which economy is healthier?

**Solution.** Same unemployment rate, but Country A has participation $100/200 = 50\%$ vs. Country B's $100/150 \approx 66.7\%$. Country B mobilizes more of its working-age population. Country A's low $u$ may reflect mass discouragement, not strong labor demand.

**Key insight.** $u$ alone can mislead; pair it with the participation rate.

---

## 3. Equilibrium Income $Y^*$ — Closed Economy

### Q3.1 (Easy)
$C = 60 + 0.75 Y$, $\overline{I} = 40$. Find $Y^*$.

**Solution.**
$$Y^* = \frac{\overline{C_0} + \overline{I}}{1 - c} = \frac{60 + 40}{0.25} = 400.$$

**Key insight.** Closed-economy formula: autonomous spending divided by $(1-c)$.

### Q3.2 (Easy)
$\overline{C_0} = 50$, $c = 0.8$, $\overline{I} = 30$. Find $Y^*$ and equilibrium consumption $C^*$.

**Solution.** $Y^* = (50 + 30)/0.2 = 400$. $C^* = 50 + 0.8(400) = 370$. (Check: $S = 400 - 370 = 30 = \overline{I}$. ✓)

**Key insight.** At equilibrium, $S = I^d$ in the closed-economy frugal model.

### Q3.3 (Easy)
$Y^* = 800$, $\overline{I} = 80$, $c = 0.75$. Recover $\overline{C_0}$.

**Solution.** $800 = (\overline{C_0} + 80)/0.25 \Rightarrow \overline{C_0} + 80 = 200 \Rightarrow \overline{C_0} = 120$.

**Key insight.** Any one of the four (autonomous, MPC, $Y^*$) can be backed out from the other three.

### Q3.4 (Medium)
Saving function $S(Y) = -40 + 0.2 Y$. $\overline{I} = 60$. Find $Y^*$ via the $S = I$ method.

**Solution.** $-40 + 0.2 Y^* = 60 \Rightarrow Y^* = 100/0.2 = 500$.

**Key insight.** $S(Y) = -\overline{C_0} + (1-c)Y$. Setting $S = \overline{I}$ is an equivalent route to $Y^*$.

### Q3.5 (Medium)
At $Y = 600$, $AE^d = 580$. Are firms accumulating or depleting inventory? Which way will $Y$ move?

**Solution.** $Y > AE^d$, so production exceeds desired purchases → unplanned inventory rises → firms cut output → $Y$ falls toward $Y^*$.

**Key insight.** $Y > AE^d$ ⇒ inventory accumulation ⇒ output contracts. Reverse for $Y < AE^d$.

### Q3.6 (Medium)
$\overline{C_0} = 100$, $c = 0.75$, $\overline{I} = 50$. Households become more frugal: $\overline{C_0}$ falls to 80. Compute the change in $Y^*$ and in equilibrium saving.

**Solution.** Old $Y^* = 150/0.25 = 600$. New $Y^* = 130/0.25 = 520$. $\Delta Y^* = -80$. Equilibrium saving was $50$ before and is still $50 = \overline{I}$ after.

**Key insight.** Paradox of thrift: more desire to save lowers $Y^*$ but leaves total saving unchanged because $S = I$ pins it.

### Q3.7 (Medium)
Two economies have the same autonomous spending but $c_A = 0.6$ and $c_B = 0.9$. Which has the larger $Y^*$? By how much?

**Solution.** $K_A = 1/0.4 = 2.5$, $K_B = 1/0.1 = 10$. For the same autonomous spending, $Y_B^* / Y_A^* = 4$.

**Key insight.** The multiplier rises sharply as $c$ approaches 1. Small changes in MPC produce big changes in equilibrium output.

### Q3.8 (Hard)
$C = 80 + 0.8(Y - 0.25 Y)$ (so consumption depends on after-tax income with a proportional tax rate $t = 0.25$). $\overline{I} = 100$. Find $Y^*$.

**Solution.** $C = 80 + 0.8(0.75 Y) = 80 + 0.6 Y$. Effective $c = 0.6$. $Y^* = (80 + 100)/0.4 = 450$.

**Key insight.** Proportional taxes lower the *effective* MPC out of $Y$ from $c$ to $c(1-t)$, shrinking the multiplier.

### Q3.9 (Hard)
Investment depends on $Y$: $I^d = 20 + 0.1 Y$. $C = 50 + 0.75 Y$. Find $Y^*$.

**Solution.** $Y = 50 + 0.75 Y + 20 + 0.1 Y = 70 + 0.85 Y \Rightarrow 0.15 Y = 70 \Rightarrow Y^* = 466.67$.

**Key insight.** Endogenous investment raises the effective slope of $AE^d$ and the implied multiplier.

### Q3.10 (Twist)
Suppose $\overline{I}$ rises by 25 and simultaneously households lose confidence so $\overline{C_0}$ falls by 25. Predict $\Delta Y^*$ at $c = 0.75$.

**Solution.** $\Delta Y^* = K \cdot (\Delta\overline{I} + \Delta\overline{C_0}) = 4 \cdot (25 - 25) = 0$.

**Key insight.** Same multiplier ⇒ offsetting shocks cancel exactly.

---

## 4. Equilibrium Income $Y^*$ — Open Economy with Government

### Q4.1 (Easy)
$\overline{C_0} = 100, c = 0.75, \overline{T} = 40, \overline{I} = 80, \overline{G} = 100, \overline{X} = 60, \overline{M} = 40$. Find $Y^*$.

**Solution.**
$$Y^* = \tfrac{1}{0.25}\big[100 - 0.75(40) + 80 + 100 + 60 - 40\big] = 4 \cdot 270 = 1{,}080.$$

**Key insight.** $\overline{T}$ enters the bracket multiplied by $-c$, not $-1$.

### Q4.2 (Easy)
$\overline{C_0} = 120, c = 0.8, \overline{T} = 50, \overline{I} = 100, \overline{G} = 80, \overline{X} = 0, \overline{M} = 0$. Find $Y^*$.

**Solution.** Bracket $= 120 - 0.8(50) + 100 + 80 = 260$. $Y^* = 5 \cdot 260 = 1{,}300$.

**Key insight.** With no trade, the only difference from the closed-economy formula is the $-c\overline{T} + \overline{G}$ pair.

### Q4.3 (Medium)
Same as Q4.1, but exports rise by 30. Find new $Y^*$.

**Solution.** $\Delta Y^* = K_X \cdot 30 = 4 \cdot 30 = 120$. New $Y^* = 1{,}200$.

**Key insight.** Exports get the spending multiplier $1/(1-c)$.

### Q4.4 (Medium)
$Y^* = 2{,}000, c = 0.6$. By how much must $\overline{G}$ change to raise $Y^*$ to 2,200?

**Solution.** $K_G = 1/0.4 = 2.5$. $\Delta\overline{G} = 200/2.5 = 80$.

**Key insight.** $\Delta\overline{G} = \Delta Y^* / K_G$.

### Q4.5 (Medium)
$c = 0.75$. $\overline{G}$ rises by 50, $\overline{T}$ rises by 30. Find $\Delta Y^*$.

**Solution.** $\Delta Y^* = K_G(50) + K_T(30) = 4(50) + (-3)(30) = 200 - 90 = 110$.

**Key insight.** Add multiplier-weighted contributions for simultaneous changes.

### Q4.6 (Medium)
$c = 0.8$. Imports rise autonomously by 25 and exports rise autonomously by 40. Find $\Delta Y^*$.

**Solution.** $K = 5, K_{IM} = -5$. $\Delta Y^* = 5(40) + (-5)(25) = 200 - 125 = 75$.

**Key insight.** Net export shocks get the spending multiplier with the appropriate sign.

### Q4.7 (Hard)
$Y^* = 1{,}200, c = 0.75$, $Y^{FE} = 1{,}500$. Imports are expected to rise by 50 (autonomous shift). After that, what $\Delta\overline{G}$ closes the recessionary gap?

**Solution.** Without action, imports drag $Y^*$ down by $K_{IM} \cdot 50 = -200$, to $1{,}000$. Gap is then $500$. $\Delta\overline{G} = 500/4 = 125$.

**Key insight.** Always project the equilibrium *with* the new shocks before computing the policy response.

### Q4.8 (Hard)
$\overline{C_0} = 80$, $c = 0.75$, $\overline{T} = 60$, $\overline{I} = 100$, $\overline{G} = 120$, $\overline{X} = 60$, $\overline{M} = 80$. Compute $Y^*$ and the trade balance at equilibrium.

**Solution.** Bracket $= 80 - 45 + 100 + 120 + 60 - 80 = 235$. $Y^* = 4 \cdot 235 = 940$. Trade balance $= \overline{X} - \overline{M} = -20$ (deficit).

**Key insight.** Trade balance in this autonomous-import model is $\overline{X} - \overline{M}$ — independent of $Y^*$ unless imports are made $Y$-dependent.

### Q4.9 (Hard)
Make imports depend on $Y$: $\overline{M} = 20 + 0.1 Y$. Other inputs as in Q4.8. Find $Y^*$.

**Solution.** $Y = \overline{C_0} + c(Y - \overline{T}) + \overline{I} + \overline{G} + \overline{X} - 20 - 0.1Y$.
$Y(1 - 0.75 + 0.1) = 80 - 45 + 100 + 120 + 60 - 20 = 295$.
$0.35 Y = 295 \Rightarrow Y^* = 842.86$.

**Key insight.** Endogenous imports lower the effective multiplier from $1/(1-c)$ to $1/(1 - c + m)$, where $m$ is the marginal propensity to import.

### Q4.10 (Twist)
$c = 0.75$. The government runs a "balanced trade" reform: $\overline{X}$ rises by 50, $\overline{M}$ rises by 50 (because exporters import inputs). Net $\Delta Y^*$?

**Solution.** $\Delta Y^* = K_X(50) + K_{IM}(50) = 4(50) - 4(50) = 0$.

**Key insight.** Equal-magnitude export and import shocks cancel — both get multiplier 4 with opposite signs.

### Q4.11 (Twist)
$c = 0.6$. The government raises $\overline{G}$ by 100 financed by raising $\overline{T}$ by exactly 100 (balanced budget). What is $\Delta Y^*$?

**Solution.** $K_G = 2.5, K_T = -1.5$. $\Delta Y^* = 2.5(100) + (-1.5)(100) = 100$. Equals $K_{BB} \cdot 100 = 1 \cdot 100$.

**Key insight.** $K_{BB} = 1$ for any $c$ in this model.

---

## 5. Multipliers — Identification and Sizing

### Q5.1 (Easy)
$c = 0.8$. Compute $K_G, K_T, K_{BB}, K_{IM}$.

**Solution.** $K_G = 5, K_T = -4, K_{BB} = 1, K_{IM} = -5$.

**Key insight.** Memorize the family: $\frac{1}{1-c}$ for spending, $-\frac{c}{1-c}$ for taxes, sum $= 1$.

### Q5.2 (Easy)
$\Delta Y^* = +60$ when $\overline{I}$ rises by 15. Recover $c$.

**Solution.** $K_I = 60/15 = 4 = 1/(1-c) \Rightarrow c = 0.75$.

**Key insight.** Multiplier $\Rightarrow$ MPC: $c = 1 - 1/K$.

### Q5.3 (Easy)
$\Delta Y^* = -90$ when $\overline{T}$ rises by 30. Recover $c$.

**Solution.** $K_T = -90/30 = -3 = -c/(1-c) \Rightarrow 3(1-c) = c \Rightarrow c = 0.75$.

**Key insight.** $|K_T| = c \cdot K_G$. A 1-pp change in $c$ moves $K_T$ more than 1-pp.

### Q5.4 (Medium)
MPS $= 0.20$, so $K = 5, K_T = -4$. $Y^*$ falls by 100. Which is consistent? (a) $\Delta\overline{C_0} = +20$, (b) $\Delta\overline{I} = -20$, (c) $\Delta\overline{T} = +25$, (d) $\Delta\overline{G} = -25$.

**Solution.** (a) $5 \cdot 20 = +100$. ✗ wrong sign. (b) $5(-20) = -100$. ✓ (c) $-4(25) = -100$. ✓ (d) $5(-25) = -125$. ✗ wrong magnitude.

**Key insight.** Two distinct shocks (b) and (c) produce the same $\Delta Y^*$ — wording matters.

### Q5.5 (Medium)
$c = 0.75$. Both $\overline{G}$ and $\overline{T}$ rise by 80. Find $\Delta Y^*$.

**Solution.** $K_{BB} \cdot 80 = 1 \cdot 80 = 80$.

**Key insight.** Balanced-budget multiplier $= 1$, period.

### Q5.6 (Medium)
$c = 0.6$. The Fed cuts taxes by 100. Politicians simultaneously cut spending by 60 to "show fiscal discipline." Find $\Delta Y^*$.

**Solution.** $K_T = -1.5, K_G = 2.5$. $\Delta Y^* = (-1.5)(-100) + 2.5(-60) = 150 - 150 = 0$.

**Key insight.** Mixed signals can perfectly offset; always sum the multiplier-weighted contributions.

### Q5.7 (Hard)
A textbook says "the multiplier is 4." Real-world studies estimate U.S. fiscal multipliers around 1.4. Name three leakages textbook models ignore that explain the gap.

**Solution.** (1) Income-conditional taxes (proportional tax rate shrinks effective $c$). (2) Imports (marginal propensity to import is a leakage). (3) Monetary offset / crowding-out — rising $Y$ raises $r$, dampening $\overline{I}$.

**Key insight.** Real-world multipliers are smaller because real economies leak in many channels.

### Q5.8 (Hard)
$c = 0.75$. $\Delta Y^* = +50$ following $\Delta\overline{G} = +100$ and an unknown $\Delta\overline{T}$. Find $\Delta\overline{T}$.

**Solution.** $50 = 4(100) + (-3)\Delta\overline{T} \Rightarrow \Delta\overline{T} = 350/3 \approx 116.67$.

**Key insight.** Solve for the unknown after writing $\Delta Y^*$ as the sum of multiplier-weighted shocks.

### Q5.9 (Hard)
Effective MPC out of $Y$ is $c_{\text{eff}} = c(1 - t)$ when there's a proportional tax $t$. With $c = 0.8, t = 0.25$, what is the spending multiplier?

**Solution.** $c_{\text{eff}} = 0.6$. $K_G = 1/(1 - 0.6) = 2.5$.

**Key insight.** Proportional taxes shrink the multiplier. The textbook lump-sum-tax result is an upper bound.

### Q5.10 (Twist)
$c = 0.75$. The Fed says: "We will cut $r$ by enough to offset any expansionary fiscal action." If the government raises $\overline{G}$ by 100, what is $\Delta Y^*$ given the Fed's reaction function?

**Solution.** Zero, by construction. Fed offsets the fiscal expansion via tighter money / higher $r$ — full crowding out.

**Key insight.** When monetary policy is reactive, fiscal multipliers can shrink toward zero.

### Q5.11 (Twist)
A country has $K_G = 2.5$ in normal times but $K_G \approx 1.5$ at the zero lower bound (no monetary offset, but other leakages still operate). Why might $K_G$ be *larger* at the ZLB?

**Solution.** At the ZLB, the central bank cannot raise rates in response to fiscal stimulus, so the crowding-out channel is dead. Only tax and import leakages operate. Multiplier rises relative to a regime with active monetary offset.

**Key insight.** State-dependent multipliers: ZLB raises fiscal potency precisely because monetary offset disappears.

---

## 6. Fiscal Policy — Gap-Closing

### Q6.1 (Easy)
$Y^* = 800, Y^{FE} = 900, c = 0.75$. Close the gap with $G$ alone.

**Solution.** Gap $= 100$. $\Delta\overline{G} = 100/4 = 25$.

**Key insight.** $\Delta\overline{G} = \text{gap}/K_G$.

### Q6.2 (Easy)
Same as Q6.1, but use a tax cut.

**Solution.** $\Delta\overline{T} = 100 / (-3) \approx -33.33$.

**Key insight.** Tax instrument is weaker per dollar than spending — must move it more.

### Q6.3 (Easy)
$Y^* = 1{,}200, Y^{FE} = 1{,}000, c = 0.8$. The economy has an inflationary gap. Close it with $\overline{G}$.

**Solution.** Gap $= -200$ (need to contract). $\Delta\overline{G} = -200/5 = -40$.

**Key insight.** Inflationary gap means $Y^* > Y^{FE}$; sign of $\Delta\overline{G}$ flips.

### Q6.4 (Medium)
$c = 0.75$, recessionary gap $= 150$. Close it with a balanced-budget package.

**Solution.** $K_{BB} = 1$. $\Delta\overline{G} = \Delta\overline{T} = 150$.

**Key insight.** Balanced budget gap-closing requires $\Delta = $ gap (since multiplier is 1).

### Q6.5 (Medium)
$c = 0.6$, recessionary gap $= 240$. The government uses 60% of the gap-closing via $G$ and 40% via tax cuts. Find required $\Delta\overline{G}$ and $\Delta\overline{T}$.

**Solution.** Need 144 of $\Delta Y^*$ from $G$, 96 from $T$. $K_G = 2.5, K_T = -1.5$. $\Delta\overline{G} = 144/2.5 = 57.6$. $\Delta\overline{T} = 96/(-1.5) = -64$.

**Key insight.** Allocate target $\Delta Y^*$ across instruments, then divide by the corresponding multiplier.

### Q6.6 (Medium)
The deficit ($G - T$) was 50 last year. The economy is in a recessionary gap of 200 with $c = 0.75$. The government uses $\overline{G}$ alone. By how much does the deficit rise?

**Solution.** $\Delta\overline{G} = 200/4 = 50$. $T$ unchanged. New deficit $= 50 + 50 = 100$.

**Key insight.** Discretionary fiscal stimulus widens the deficit dollar-for-dollar in $\Delta G$.

### Q6.7 (Hard)
$c = 0.75$. Recessionary gap $= 100$. The government raises $\overline{G}$ by 50 *and* raises $\overline{T}$ by 20. Did it close the gap? If not, by how much did it miss?

**Solution.** $\Delta Y^* = 4(50) + (-3)(20) = 200 - 60 = 140$. Overshoots by 40 — could create an inflationary gap.

**Key insight.** Always sum multiplier-weighted shocks before declaring a gap closed.

### Q6.8 (Hard)
Country runs $G = 500$, $T = 480$ (deficit 20). Recession hits — $Y^*$ falls 200 below $Y^{FE}$ at $c = 0.8$. Politicians refuse to widen the deficit beyond 20. Use balanced-budget policy.

**Solution.** $K_{BB} = 1 \Rightarrow \Delta\overline{G} = \Delta\overline{T} = 200$. New $G = 700, T = 680$. Deficit unchanged at 20. Gap closed.

**Key insight.** Balanced-budget multiplier preserves the deficit while still raising $Y^*$.

### Q6.9 (Hard)
$Y^* = 1{,}500, Y^{FE} = 1{,}700$. Imports just rose autonomously by 40. $c = 0.75$. Find $\Delta\overline{G}$ to close the (post-shock) gap.

**Solution.** Post-shock $Y^* = 1{,}500 + (-4)(40) = 1{,}340$. New gap $= 360$. $\Delta\overline{G} = 360/4 = 90$.

**Key insight.** Project equilibrium *with* shocks before sizing the policy response.

### Q6.10 (Twist)
A senator argues: "Tax cuts always work better than spending increases because they let people choose what to buy." On a per-dollar basis, evaluate this claim using $K_G$ and $K_T$.

**Solution.** $|K_T| = c/(1-c) < 1/(1-c) = K_G$. A \$1 spending increase moves $Y^*$ by $K_G$; a \$1 tax cut moves $Y^*$ by $|K_T| = c \cdot K_G < K_G$. The senator is wrong on per-dollar potency — round 1 of a tax cut leaks $(1-c)$ into saving, while round 1 of $G$ enters $AE^d$ in full.

**Key insight.** Per dollar, spending is more potent than tax cuts in this model.

---

## 7. Money & Banking — Reserves, T-accounts, Money Creation

### Q7.1 (Easy)
$rrr = 10\%$. Bank has $DD_p = \$2{,}000, TR = \$250$. Compute $RR$ and $ER$.

**Solution.** $RR = 0.10(2000) = 200$. $ER = 250 - 200 = 50$.

**Key insight.** $ER = TR - RR$. Banks loan out $ER$.

### Q7.2 (Easy)
$rrr = 25\%$. Compute the money multiplier $K_S$.

**Solution.** $K_S = 1/0.25 = 4$.

**Key insight.** Money multiplier is the reciprocal of the required reserve ratio.

### Q7.3 (Easy)
Fed buys \$30 in securities; $rrr = 10\%$. Find max $\Delta M^S$.

**Solution.** $\Delta M^S = (1/0.10) \cdot 30 = 300$.

**Key insight.** $\Delta M^S = K_S \cdot \Delta R$ assuming no leakage.

### Q7.4 (Medium)
A customer deposits \$1,000 cash. $rrr = 20\%$. The bank creates a single loan of $\$X$ (no chain). What is $X$? What happens to $M^S$ when the loan is spent and re-deposited?

**Solution.** $X = 800$ (the bank lends out $ER = 1000 - 200 = 800$). When redeposited, second bank holds $RR = 0.20 \cdot 800 = 160$, lends 640. The full chain sums to $\Delta DD_p = 5{,}000$.

**Key insight.** Lending creates new deposits — that is how $M^S$ expands.

### Q7.5 (Medium)
Banking system has $DD_p = \$1{,}000$, $TR = \$200$, $rrr = 20\%$. The Fed cuts $rrr$ to 10%. Find max new $\Delta M^S$.

**Solution.** Pre-cut $RR = 200$, $ER = 0$ (loaned up). Post-cut required $RR = 100$, so freed reserves $= 100$. New $K_S = 10$. $\Delta M^S = 10 \cdot 100 = 1{,}000$.

**Key insight.** A cut in $rrr$ does two things: frees existing reserves and raises $K_S$.

### Q7.6 (Medium)
Distinguish M1 and M2.

**Solution.** M1 = currency held by public + checkable deposits + travelers' checks + NOW accounts. M2 = M1 + savings + small time deposits + money market mutual funds + near-monies.

**Key insight.** M1 is "transactions money"; M2 is broader and more stable.

### Q7.7 (Medium)
Show the Fed's balance sheet entries for an OMO purchase of \$50 in Treasuries.

**Solution.** Fed assets: Treasuries +50. Fed liabilities: bank reserves +50. Both sides expand equally.

**Key insight.** OMO purchase swaps bank-held bonds for bank reserves — the latter is high-powered money.

### Q7.8 (Hard)
$rrr = 20\%$. Public holds 10% of any new deposits as cash outside banks. Fed buys \$50. Find effective $\Delta M^S$.

**Solution.**
$$K_S^{\text{leak}} = \frac{1+cr}{rrr+cr} = \frac{1.10}{0.30} \approx 3.67.$$
$\Delta M^S \approx 3.67 \cdot 50 = 183.5$ (vs. 250 with no leakage).

**Key insight.** Cash held outside banks is a leakage that shrinks the multiplier below $1/rrr$.

### Q7.9 (Hard)
Banks voluntarily hold $ER > 0$ as a precaution (post-2008 environment). With $rrr = 10\%$ and banks holding 5% extra ER, what is the effective $K_S$?

**Solution.** Effective reserve ratio $= 15\%$. $K_S = 1/0.15 \approx 6.67$ (vs. 10 with no excess).

**Key insight.** Voluntary excess reserves act like an additional reserve requirement and shrink the multiplier.

### Q7.10 (Hard)
Bank A receives a \$200 deposit; $rrr = 25\%$. Trace the first three rounds of money creation. What is the eventual total expansion?

**Solution.** Round 1: Bank A lends \$150. Round 2: receiving bank lends \$112.50. Round 3: next bank lends \$84.375. Total: $200 \cdot 4 = 800$.

**Key insight.** Geometric series: $200 \cdot \sum_{k=0}^{\infty} 0.75^k = 200/0.25 = 800$.

### Q7.11 (Twist)
The Fed sells \$100 in securities ($rrr = 10\%$). What is the change in $M^S$? Where do the dollars come *from* on the bank-system side?

**Solution.** $\Delta M^S = -1000$. Buyer's bank loses \$100 in reserves, must call in loans to restore $RR$, contracting deposits throughout the system by \$1000.

**Key insight.** OMO sales drain reserves and force the deposit chain to contract — symmetric to the purchase case.

---

## 8. Money Market — $M^S$, $M^D$, Equilibrium $r^*$

### Q8.1 (Easy)
List the three motives for holding money.

**Solution.** Transactions, precautionary, speculative.

**Key insight.** $Y$ shifts $M^D$ via transactions; $r$ moves along $M^D$ via speculative.

### Q8.2 (Easy)
The Fed buys \$50 in bonds. Direction of $r^*$?

**Solution.** $\uparrow M^S \Rightarrow$ excess money supply at old $r \Rightarrow$ people buy bonds $\Rightarrow$ bond prices rise $\Rightarrow r^*$ falls.

**Key insight.** $\uparrow M^S \Rightarrow \downarrow r^*$.

### Q8.3 (Easy)
The economy enters a boom — $Y$ rises sharply. With $M^S$ fixed, what happens to $r^*$?

**Solution.** Transactions $M^D$ shifts right $\Rightarrow r^*$ rises.

**Key insight.** Goods market feeds back into money market through $Y \to M^D$.

### Q8.4 (Medium)
The price level $P$ rises by 5%. With $M^S$ and $Y$ fixed, what happens to $r^*$ in the basic CFO money-market diagram?

**Solution.** Higher $P$ raises nominal transactions demand $\Rightarrow M^D$ shifts right $\Rightarrow r^*$ rises.

**Key insight.** Both $Y$ and $P$ shift the money demand curve to the right.

### Q8.5 (Medium)
$M^S = 600$ and $M^D = 800 - 20 r$. Find $r^*$.

**Solution.** $600 = 800 - 20 r \Rightarrow r^* = 10\%$.

**Key insight.** Solve $M^S = M^D$ for $r$.

### Q8.6 (Medium)
$M^D = 1000 - 50 r + 0.2 Y$. $Y = 2000$, $M^S = 1300$. Find $r^*$.

**Solution.** $1300 = 1000 - 50r + 0.2(2000) = 1400 - 50r \Rightarrow r^* = 2\%$.

**Key insight.** With $Y$ in $M^D$, plug it in before solving for $r^*$.

### Q8.7 (Medium)
At $r > r^*$ in the money market, what disequilibrium exists and how is it resolved?

**Solution.** Excess supply of money ($M^S > M^D$ at the high $r$). People reduce money holdings by buying bonds. Bond prices rise, yields fall, $r$ falls toward $r^*$.

**Key insight.** Money-market disequilibrium clears through the bond market.

### Q8.8 (Hard)
Fed wants to lower $r^*$ from 6% to 4% with $M^D = 1500 - 100 r$. Find required $\Delta M^S$.

**Solution.** At $r = 6$: $M^D = 900$. At $r = 4$: $M^D = 1100$. $\Delta M^S = 200$.

**Key insight.** Required $\Delta M^S$ depends on the slope of $M^D$ — flatter $M^D$ means smaller $\Delta M^S$ to move $r$.

### Q8.9 (Hard)
Fed announces an inflation target. Public expects $P$ to rise. $M^D$ shifts right by 50. Fed wants to keep $r^*$ unchanged. What $\Delta M^S$?

**Solution.** $\Delta M^S = +50$ (accommodate the demand shift).

**Key insight.** To peg $r$, the Fed must let $M^S$ float to absorb $M^D$ shocks.

### Q8.10 (Hard)
Money market: $M^D = 800 - 30 r + 0.4 Y$, $M^S = 1000$. Goods market: $Y = 5(\overline{C_0} + \overline{I} - 10 r)$ (interest-sensitive investment). $\overline{C_0} + \overline{I} = 250$. Find joint equilibrium $(Y^*, r^*)$.

**Solution.** From goods: $Y = 1250 - 50 r$. From money: $1000 = 800 - 30 r + 0.4 Y \Rightarrow 200 = -30 r + 0.4 Y$.
Substitute: $200 = -30r + 0.4(1250 - 50r) = 500 - 50r \Rightarrow r^* = 6$. $Y^* = 1250 - 300 = 950$.

**Key insight.** Joint equilibrium requires solving both equations simultaneously — IS-LM in disguise.

---

## 9. Bond Pricing and Yields

### Q9.1 (Easy)
$FV = \$1{,}000$, $T = 1$, $r = 5\%$. Find $PV$.

**Solution.** $PV = 1000/1.05 \approx 952.38$.

**Key insight.** Single-period PV: just divide by $(1+r)$.

### Q9.2 (Easy)
$FV = \$1{,}000$, $T = 5$, $r = 4\%$. Find $PV$.

**Solution.** $PV = 1000/(1.04)^5 = 1000/1.21665 \approx 821.93$.

**Key insight.** Compounding over multiple periods substantially lowers $PV$.

### Q9.3 (Easy)
A 1-year zero coupon bond has $FV = \$500$ and trades at $\$476.19$. Find $r$.

**Solution.** $r = 500/476.19 - 1 = 0.05 = 5\%$.

**Key insight.** Single-period yield: $r = FV/PV - 1$.

### Q9.4 (Medium)
A 2-year bond has $FV = \$1{,}000$ and $PV = \$890$. Find the yield.

**Solution.** $(1+r)^2 = 1000/890 = 1.1236 \Rightarrow 1+r = 1.06 \Rightarrow r = 6\%$.

**Key insight.** Multi-period yield: $r = (FV/PV)^{1/T} - 1$.

### Q9.5 (Medium)
A 10-year bond's yield rises from 4% to 5%. Compute the percentage drop in its price (assume $FV = \$1000$).

**Solution.** Old price $= 1000/(1.04)^{10} = 675.56$. New price $= 1000/(1.05)^{10} = 613.91$. Change $= -9.13\%$.

**Key insight.** Long-maturity bonds have steep price-yield curves; small yield moves cause big price moves.

### Q9.6 (Medium)
Compare the price impact of a 1pp yield rise (from 4% to 5%) on a 1-year vs. 30-year bond, $FV = 1000$.

**Solution.** 1-year: $1000/1.04 = 961.54 \to 1000/1.05 = 952.38$, $-0.95\%$. 30-year: $1000/1.04^{30} = 308.32 \to 1000/1.05^{30} = 231.38$, $-24.96\%$.

**Key insight.** Duration scales price sensitivity to yield. Long bonds are far more rate-sensitive.

### Q9.7 (Medium)
The Fed buys bonds aggressively — $r^*$ in the money market falls from 5% to 3%. What happens to the price of a 5-year zero coupon bond, $FV = 1000$?

**Solution.** Old: $1000/1.05^5 = 783.53$. New: $1000/1.03^5 = 862.61$. Price rises $\approx 10.1\%$.

**Key insight.** OMO purchase, lower $r$, higher bond prices — they are the same event.

### Q9.8 (Hard)
A 3-year bond pays \$50 coupon annually plus \$1000 face at maturity. $r = 6\%$. Find $PV$.

**Solution.** $PV = 50/1.06 + 50/1.06^2 + 1050/1.06^3 = 47.17 + 44.50 + 881.60 = 973.27$.

**Key insight.** PV of a coupon bond is the sum of PVs of each cash flow.

### Q9.9 (Hard)
Two bonds (zero coupon, $FV = 1000$): A has $T = 5$, B has $T = 10$. Both yield 5%. Yield rises to 6%. Which loses more value in dollars? Why?

**Solution.** A: $783.53 \to 747.26$, $-36.27$. B: $613.91 \to 558.39$, $-55.52$. B loses more.

**Key insight.** Longer $T$ ⇒ bigger $\partial PV / \partial r$.

### Q9.10 (Twist)
Money market is in disequilibrium: $r = 6\%$, $r^* = 5\%$. A 1-year bond, $FV = \$500$, currently prices at $r = 6\%$. As the market re-equilibrates, what happens to the bond price?

**Solution.** At $r = 6\%$: $PV = 500/1.06 \approx 471.70$. At $r = 5\%$: $PV = 500/1.05 \approx 476.19$. Price rises by \$4.49.

**Key insight.** Excess money supply drives bond buying, which pushes prices up and $r$ down toward $r^*$.

### Q9.11 (Twist)
A bond yields 7%; new bonds in the market yield 8%. Why does the price of the old bond fall?

**Solution.** No buyer will pay full face for a 7% coupon when 8% is available — the old bond's price drops until its yield-to-maturity matches 8%.

**Key insight.** Bond prices adjust mechanically to make yields consistent with the prevailing market rate.

---

## 10. Foreign Exchange and PPP

### Q10.1 (Easy)
A basket costs \$600 in the US and £400 in the UK. Find the PPP exchange rate $E_{\$/\pounds}$.

**Solution.** $E_{\$/\pounds} = 600/400 = 1.50$.

**Key insight.** PPP: $E = P_{US}/P_{UK}$.

### Q10.2 (Easy)
US inflation 6%, UK inflation 2%. Predict direction of $E_{\$/\pounds}$.

**Solution.** $E_{\$/\pounds}$ rises — \$ depreciates because US prices rose faster.

**Key insight.** Higher-inflation country's currency depreciates.

### Q10.3 (Easy)
The Fed raises US interest rates while UK rates are unchanged. Direction of $E_{\$/\pounds}$?

**Solution.** Capital flows into US ($D^\pounds$ falls; $S^\pounds$ rises). $E_{\$/\pounds}$ falls — \$ appreciates.

**Key insight.** Higher domestic interest rates appreciate the home currency.

### Q10.4 (Medium)
Starting at $E_{\$/\pounds} = 1.50$, US prices rise 8%, UK prices rise 2%. New PPP rate?

**Solution.** New US basket cost $= 600 \cdot 1.08 = 648$. New UK $= 400 \cdot 1.02 = 408$. $E = 648/408 \approx 1.588$.

**Key insight.** PPP rate moves with the inflation differential.

### Q10.5 (Medium)
\$ depreciates from 1.50 to 1.80 \$/£. A UK textbook costs £30. By how much does its price in dollars change?

**Solution.** Old \$ price: 30 \cdot 1.50 = 45. New: 30 \cdot 1.80 = 54. Up \$9, or 20%.

**Key insight.** Depreciation makes foreign goods more expensive in domestic currency.

### Q10.6 (Medium)
US and Mexico. PPP rate is 20 pesos/\$. A Big Mac costs \$5 in US and 80 pesos in Mexico. Is the peso over- or undervalued?

**Solution.** Big Mac PPP $= 80/5 = 16$ pesos/\$. Actual is 20 pesos/\$. Peso is undervalued (need more pesos per \$ than PPP says).

**Key insight.** When market $E$ exceeds PPP-implied $E$, the foreign currency is undervalued.

### Q10.7 (Hard)
\$ depreciates 10%. Trace the effect on $Y^*$ (qualitatively, assuming $c = 0.75$ and modest export elasticity).

**Solution.** $\uparrow EX, \downarrow IM \Rightarrow \uparrow (X-M) \Rightarrow $ AE shifts up $\Rightarrow Y^*$ rises (multiplier $K = 4$). AD shifts right $\Rightarrow P$ rises too. Effects subject to J-curve in early quarters.

**Key insight.** Depreciation is expansionary (higher $Y$, higher $P$) in the medium run after the J-curve.

### Q10.8 (Hard)
Explain the J-curve. Why does the trade balance worsen before improving?

**Solution.** After depreciation, import prices rise immediately (existing import contracts), but quantities respond slowly. So in the short run, $IM$ in dollar terms rises (price effect) and $EX$ has not yet risen substantially. Net exports fall. Over 2–4 quarters, quantities adjust and $(X-M)$ improves.

**Key insight.** Prices respond fast, quantities slow — that delay produces the J-curve.

### Q10.9 (Hard)
US inflation 5%, Eurozone inflation 1%. US nominal rates 4%, Eurozone 0%. Predict short-run direction of \$/€.

**Solution.** Inflation differential pushes \$ to depreciate. Interest rate differential pushes \$ to appreciate. Net effect ambiguous; PPP holds long-run, capital flows dominate short-run, so \$ likely appreciates short-run.

**Key insight.** Two channels (inflation, interest) often pull opposite ways. Capital flows tend to win short-run; PPP wins long-run.

### Q10.10 (Twist)
A country runs a trade *surplus* but its currency *depreciates*. Reconcile.

**Solution.** Trade surplus generates supply of foreign currency (or demand for home currency). But large capital outflows (residents buying foreign assets) can dominate, pushing the home currency down. Currency value reflects the capital + current account *together*.

**Key insight.** Exchange rate is determined by total supply/demand for currency, not only the trade balance.

### Q10.11 (Twist)
Why does PPP hold poorly in the short run but well in the long run?

**Solution.** Short run: prices are sticky, capital flows dominate, transport costs and trade barriers matter. Long run: arbitrage in goods works through; sticky prices adjust; capital flows are mean-reverting.

**Key insight.** PPP is an arbitrage relationship that needs time to bind.

---

## 11. Monetary Policy under Fixed vs. Flexible Exchange Rates

### Q11.1 (Easy)
Under flexible ER, the Fed cuts rates. Through which two channels does $Y$ rise?

**Solution.** (1) Interest channel: $\downarrow r \Rightarrow \uparrow I^d \Rightarrow \uparrow Y$. (2) Exchange-rate channel: $\downarrow r \Rightarrow$ capital outflow $\Rightarrow$ \$ depreciates $\Rightarrow \uparrow (X-M) \Rightarrow \uparrow Y$.

**Key insight.** Under floating ER, both channels reinforce — monetary policy is potent.

### Q11.2 (Easy)
Under fixed ER, the central bank tries to expand $M^S$. Why is this hard?

**Solution.** Lower $r$ triggers capital outflow, which would depreciate the currency. To defend the peg, the central bank must sell foreign reserves and buy back its own currency, contracting $M^S$. Net change is small.

**Key insight.** Fixed ER kills monetary independence — the FX channel forces $M^S$ back.

### Q11.3 (Easy)
State the trilemma.

**Solution.** A country can have at most two of: (i) free capital flows, (ii) fixed exchange rate, (iii) independent monetary policy.

**Key insight.** Pick two; you cannot have all three.

### Q11.4 (Medium)
Hong Kong pegs to the USD and allows free capital flows. What does the trilemma imply about HK's monetary policy independence?

**Solution.** HK has no monetary policy independence — it imports US monetary policy via the peg. When the Fed raises rates, HK must too.

**Key insight.** A hard peg with open capital outsources monetary policy to the anchor country.

### Q11.5 (Medium)
Under floating ER, the central bank surprises markets with a 1% rate cut. Trace the FX-channel impact on $Y$.

**Solution.** $\downarrow r$ → capital outflows seek higher returns abroad → $S^{\text{FX}}$ rises (citizens supply local currency for foreign), local currency depreciates → $\uparrow (X - M) \Rightarrow \uparrow AE^d \Rightarrow \uparrow Y$ (multiplied by $K$).

**Key insight.** Capital flows respond to rate differentials and move the FX rate; FX moves trade balance; trade balance moves $Y$.

### Q11.6 (Medium)
Under fixed ER, the government runs a fiscal expansion ($\uparrow \overline{G}$). What happens to $r$, capital flows, and $M^S$?

**Solution.** $\uparrow G \Rightarrow \uparrow Y \Rightarrow \uparrow M^D \Rightarrow \uparrow r$. Higher $r$ attracts capital inflow, which would appreciate the currency. To defend the peg, central bank buys foreign currency, expanding $M^S$. Result: monetary policy *automatically* accommodates fiscal expansion under fixed ER. Fiscal multiplier is *bigger* than under floating.

**Key insight.** Mundell-Fleming: fiscal policy is potent under fixed ER (no monetary offset); monetary policy is potent under floating ER.

### Q11.7 (Hard)
Brazil floats its currency and conducts independent monetary policy. The Fed hikes US rates by 200 bp. What pressure does Brazil feel?

**Solution.** Capital flows out of Brazil to chase higher US yields. Real depreciates. Brazil's central bank may hike to slow capital flight, even if domestic conditions don't warrant it. This is the "fear of floating."

**Key insight.** Even floating regimes are not fully insulated from foreign monetary policy.

### Q11.8 (Hard)
Argentina's currency board (a hard peg) collapses when the central bank runs out of foreign reserves. Why?

**Solution.** A peg requires the central bank to defend the rate by selling FX reserves whenever there's pressure to depreciate. If reserves are exhausted (e.g., after persistent capital outflows or trade deficits), the peg breaks. Speculators front-run this.

**Key insight.** Pegs are only as strong as the central bank's foreign-reserve buffer.

### Q11.9 (Twist)
A country with capital controls *can* run a fixed ER and independent monetary policy simultaneously. Explain.

**Solution.** Capital controls block the arbitrage that would otherwise force $r_{\text{home}} = r_{\text{world}}$. Without that constraint, the central bank can set $r$ domestically while pegging the FX rate. China operates roughly this way.

**Key insight.** The trilemma's "free capital flows" leg can be relaxed via controls — at the cost of capital-market efficiency.

---

## 12. AS/AD Synthesis and Miscellaneous

### Q12.1 (Easy)
List four shocks that shift AD right.

**Solution.** $\uparrow \overline{G}$, $\downarrow \overline{T}$, $\uparrow M^S$, currency depreciation, wealth boom, $\uparrow \overline{X}$.

**Key insight.** Anything that raises autonomous spending or eases monetary conditions shifts AD right.

### Q12.2 (Easy)
Give two examples of negative AS shocks.

**Solution.** Oil-price spike, war damaging capital stock, sharp wage push, drought.

**Key insight.** AS shifts left when input costs rise or productive capacity falls.

### Q12.3 (Easy)
A productivity boom shifts AS right. What happens to $Y$ and $P$?

**Solution.** $Y$ rises, $P$ falls.

**Key insight.** Positive AS shock = the rare "good news for both sides" of the AD/AS diagram.

### Q12.4 (Medium)
Stagflation in 1970s: explain in AS/AD terms.

**Solution.** Negative AS shock (oil embargo) shifted AS left. Output fell ($Y \downarrow$), prices rose ($P \uparrow$) — stagflation. Standard demand-side tools couldn't fix both simultaneously.

**Key insight.** AS shocks produce the awkward $Y$ and $P$ moving in opposite directions.

### Q12.5 (Medium)
$\overline{G}$ rises by 100 with $c = 0.75$. In the basic Keynesian model, $P$ is fixed — $Y$ rises by 400. In AS/AD with an upward-sloping AS, why is the actual $\Delta Y$ smaller?

**Solution.** $\uparrow AD$ raises both $Y$ and $P$. Higher $P$ raises $M^D$, raises $r^*$, lowers $\overline{I}$ — partial crowding out. Some of the AD shock is absorbed by higher prices, not higher output.

**Key insight.** Sloped AS dilutes the multiplier; flat AS (zero-lower-bound style) recovers the textbook 4×.

### Q12.6 (Medium)
Distinguish federal *deficit* from federal *debt*.

**Solution.** Deficit is a flow ($G - T$ in one period). Debt is a stock (cumulative past deficits).

**Key insight.** Deficit/year $\to$ debt; you can have a falling debt-to-GDP ratio with a positive deficit if GDP grows fast enough.

### Q12.7 (Medium)
Trade feedback effect: explain in one sentence.

**Solution.** A boom in country A raises A's imports, which are B's exports, raising B's $Y$, which raises B's imports of A's exports, partially feeding the boom back to A.

**Key insight.** International spillovers amplify domestic shocks.

### Q12.8 (Hard)
Beggar-thy-neighbor policies (tariffs, currency manipulation) raise home $Y$ at foreign expense. Why are they self-defeating in equilibrium?

**Solution.** Foreign retaliation. Trade volumes fall on both sides; the beggar gain disappears once partners impose matching restrictions. Equilibrium is lower trade for everyone with no relative gain.

**Key insight.** Trade policy is a coordination game; unilateral defection invites retaliation.

### Q12.9 (Hard)
The Fed simultaneously conducts contractionary monetary policy ($\uparrow r$) while the government runs a fiscal expansion ($\uparrow \overline{G}$). Use AS/AD and the open-economy model to predict effects on $Y$, $P$, and the exchange rate.

**Solution.** Both AD shifts net out — could be unchanged. But $r$ rises sharply (fiscal pressure + monetary tightening). High $r$ attracts capital inflows, currency appreciates, $(X - M)$ falls, dragging on $Y$. This is a stylized version of "Reaganomics" — strong dollar with mixed $Y$ outcome.

**Key insight.** Combined fiscal-monetary stance affects FX through the rate channel; trade balance is collateral damage.

### Q12.10 (Twist)
Crowding out in a closed economy works through $r$. Identify *two* additional crowding channels in an open economy.

**Solution.** (1) Exchange-rate appreciation (capital inflows) reduces net exports. (2) Higher imports leak demand abroad. Both shrink the domestic multiplier further beyond the closed-economy interest-rate channel.

**Key insight.** Open-economy crowding stacks: rate channel + FX channel + import leakage.

### Q12.11 (Twist)
Identify which technique to apply: "MPC = 0.75. Inflationary gap = 200. The Fed tightens by raising rates 1pp; this lowers $\overline{I}$ by 30. By how much must the government cut $\overline{G}$ to close the remaining gap?"

**Solution.** Combine techniques. (i) Project Fed's effect: $\Delta Y^* = 4 \cdot (-30) = -120$. Remaining gap $= 200 - 120 = 80$ (still need to contract by 80). (ii) Fiscal: $\Delta\overline{G} = -80/4 = -20$.

**Key insight.** When multiple shocks act, project all of them on $Y^*$ first, then size the residual policy response.

### Q12.12 (Twist)
The economy is at $Y^{FE}$ with $P$ stable. The currency depreciates 10%. Predict short-run and medium-run effects on $Y$ and $P$.

**Solution.** Short run (J-curve): trade balance worsens, slight drag on $Y$, $P$ rising due to import-price pass-through. Medium run: $(X-M)$ improves, AD shifts right, $Y$ rises above $Y^{FE}$ (inflationary gap), $P$ rises further. AS may eventually shift left as wages catch up to higher prices.

**Key insight.** Same shock, different time horizons, different signs on $Y$. Always specify the horizon.

